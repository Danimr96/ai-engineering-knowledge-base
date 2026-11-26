/* The whole application, as one classic script.
 *
 * Why one file and no framework: the page must run from a file:// URL, where
 * browsers block ES modules and fetch(). So: one script, data in globals
 * (window.KG_DATA, set by data/graph.js), lesson texts loaded on demand by
 * adding <script> tags.
 *
 * Reading order:
 *   1. helpers and the graph index
 *   2. storage: progress and theme (per reader, in localStorage)
 *   3. on-demand resources (lesson texts, mermaid, figures)
 *   4. shared pieces (stops on a line, related lists, code highlighting)
 *   5. search
 *   6. views, one function per page
 *   7. router
 */
(function () {
  'use strict';

  // ══ 1. helpers and the graph index ═══════════════════════════════════

  const D = window.KG_DATA;
  const SVG_NS = 'http://www.w3.org/2000/svg';

  /** Build a DOM element. Text is always inserted as text, never as HTML. */
  function h(tag, props, ...kids) {
    return fill(document.createElement(tag), props, kids);
  }
  function s(tag, props, ...kids) {
    return fill(document.createElementNS(SVG_NS, tag), props, kids);
  }
  function fill(el, props, kids) {
    for (const key in props || {}) {
      const v = props[key];
      if (v == null || v === false) continue;
      if (key === 'class') el.setAttribute('class', v);
      else if (key === 'html') el.innerHTML = v; // only for HTML produced by the build
      else if (key === 'style') for (const p in v) el.style.setProperty(p, v[p]);
      else if (key.startsWith('on')) el.addEventListener(key.slice(2), v);
      else el.setAttribute(key, v === true ? '' : v);
    }
    for (const kid of kids.flat(Infinity)) {
      if (kid == null || kid === false) continue;
      el.append(kid.nodeType ? kid : document.createTextNode(String(kid)));
    }
    return el;
  }
  const esc = (t) => String(t).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const trunc = (t, n) => (t.length > n ? t.slice(0, n - 1).trimEnd() + '…' : t);
  const plural = (n, one, many) => `${n.toLocaleString('en')} ${n === 1 ? one : many || one + 's'}`;
  function fmtMin(m) {
    if (!m) return '';
    if (m < 60) return `${m} min`;
    const hours = Math.floor(m / 60), rest = m % 60;
    return rest ? `${hours} h ${rest} min` : `${hours} h`;
  }

  // Nodes arrive as a flat list and edges as [srcIndex, dstIndex, typeIndex, attrs].
  // Rebuild the lookups every view needs: by id, by type, edges out of and into a node.
  const NODES = D.nodes;
  const byId = new Map();
  const byType = {};
  NODES.forEach((n, i) => {
    n.i = i;
    byId.set(n.id, n);
    (byType[n.type] = byType[n.type] || []).push(n);
  });
  const OUT = NODES.map(() => []);
  const IN = NODES.map(() => []);
  for (const [si, di, ti, a] of D.edges) {
    const e = { s: NODES[si], d: NODES[di], t: D.edge_types[ti], a: a || {} };
    OUT[si].push(e);
    IN[di].push(e);
  }
  const out = (n, type) => OUT[n.i].filter((e) => e.t === type);
  const inn = (n, type) => IN[n.i].filter((e) => e.t === type);
  const all = (type) => byType[type] || [];
  const uniq = (list) => [...new Set(list)];
  const byRef = (a, b) => a.a.phase - b.a.phase || a.a.num - b.a.num;

  const phaseOf = (lesson) => byId.get('phase:' + lesson.a.phase);
  const lessonsCache = new Map();
  function lessonsOf(phase) {
    if (!lessonsCache.has(phase)) {
      lessonsCache.set(phase, out(phase, 'CONTAINS').map((e) => e.d).filter((n) => n.type === 'lesson').sort(byRef));
    }
    return lessonsCache.get(phase);
  }

  const TYPE_NAME = {
    phase: 'Phase', lesson: 'Lesson', concept: 'Concept', resource: 'Reference', artifact: 'Prompt or skill',
    library: 'Library', learning_path: 'Path', community: 'Topic', category: 'Category', track: 'Track', myth: 'Myth',
  };
  const TYPE_COLOR = {
    phase: 'var(--ink)', lesson: 'var(--line-0, var(--accent))', concept: 'var(--line-2, var(--accent))',
    resource: 'var(--line-5, var(--ink-3))', artifact: 'var(--line-3, var(--ink-3))', library: 'var(--line-1, var(--ink-3))',
    learning_path: 'var(--line-4, var(--ink-3))', community: 'var(--ink-3)', category: 'var(--ink-3)', track: 'var(--ink-2)', myth: 'var(--warn)',
  };
  const LESSON_TYPE = { build: 'Build', learn: 'Learn', 'learn+build': 'Learn and build', capstone: 'Capstone', reference: 'Reference' };

  function nodeLabel(n) {
    if (n.type === 'lesson') return `${n.a.ref} ${n.a.title}`;
    if (n.type === 'community') return String(n.a.name || n.label).replace(/ · /g, ', ');
    if (n.type === 'phase') return `Phase ${n.a.num}: ${n.a.title}`;
    return n.label;
  }
  function nodeHref(n) {
    if (n.type === 'lesson') return `#/lesson/${n.a.ref}`;
    if (n.type === 'phase') return `#/phase/${n.a.num}`;
    if (n.type === 'concept') return `#/concept/${encodeURIComponent(n.id.slice(8))}`;
    if (n.type === 'learning_path') return `#/path/${encodeURIComponent(n.a.key)}`;
    return `#/node/${encodeURIComponent(n.id)}`;
  }
  const graphHref = (n) => `#/graph/${encodeURIComponent(n.id)}`;
  const lineVar = (phaseNum) => `var(--line-${D.phase_line[String(phaseNum)] || 0})`;

  // ══ 2. storage: progress and theme ═══════════════════════════════════

  // localStorage can be unavailable (private mode, locked-down profiles):
  // the site then works without remembering anything.
  const store = {
    get(key, fallback) {
      try { const v = localStorage.getItem(key); return v == null ? fallback : JSON.parse(v); } catch (e) { return fallback; }
    },
    set(key, value) {
      try { localStorage.setItem(key, JSON.stringify(value)); } catch (e) { /* not remembered */ }
    },
  };
  const PROGRESS_KEY = 'kg-progress-v1';
  let progress = store.get(PROGRESS_KEY, {}) || {};
  const isDone = (lesson) => Boolean(progress[lesson.a.ref]);
  const doneCount = (lessons) => lessons.filter(isDone).length;
  function setDone(lesson, on) {
    if (on) progress[lesson.a.ref] = new Date().toISOString().slice(0, 10);
    else delete progress[lesson.a.ref];
    store.set(PROGRESS_KEY, progress);
    updateProgressCount();
  }
  function updateProgressCount() {
    const n = doneCount(all('lesson'));
    document.getElementById('nav-progress').textContent = n ? `${n}/${all('lesson').length}` : '';
  }

  const root = document.documentElement;
  const darkQuery = window.matchMedia('(prefers-color-scheme: dark)');
  const isDark = () => root.dataset.theme === 'dark';
  function applyTheme() {
    const saved = store.get('kg-theme', null);
    root.dataset.theme = saved || (darkQuery.matches ? 'dark' : 'light');
  }
  // One colour per line, in both themes, as CSS variables --line-0, --line-1, ...
  document.head.append(h('style', null,
    ':root{' + D.lines.map((l, i) => `--line-${i}:${l.color}`).join(';') + '}' +
    '[data-theme="dark"]{' + D.lines.map((l, i) => `--line-${i}:${l.dark}`).join(';') + '}'));

  // ══ 3. on-demand resources ═══════════════════════════════════════════

  // A resource is a script that calls window.__kgRes(path, value). In the
  // folder build it is a file; in the single-file build it sits in the page
  // as an inert <script type="text/plain" data-res="path"> block.
  const resValues = new Map();
  const scriptPromises = new Map();
  window.__kgRes = (path, value) => resValues.set(path, value);

  function loadScript(path) {
    if (!scriptPromises.has(path)) {
      scriptPromises.set(path, new Promise((resolve, reject) => {
        const el = document.createElement('script');
        const inline = document.querySelector(`script[type="text/plain"][data-res="${path}"]`);
        if (inline) {
          el.textContent = inline.textContent;
          document.head.append(el); // runs synchronously
          inline.remove();
          resolve();
        } else {
          el.src = path;
          el.onload = resolve;
          el.onerror = () => { scriptPromises.delete(path); reject(new Error('Could not load ' + path)); };
          document.head.append(el);
        }
      }));
    }
    return scriptPromises.get(path);
  }
  const loadRes = (path) => loadScript(path).then(() => resValues.get(path));

  async function renderDiagrams(scope) {
    const sources = [...scope.querySelectorAll('pre.mermaid-src')];
    if (!sources.length) return;
    await loadScript('vendor/mermaid.min.js');
    const css = getComputedStyle(root);
    const v = (name) => css.getPropertyValue(name).trim();
    window.mermaid.initialize({
      startOnLoad: false,
      securityLevel: 'strict',
      theme: 'base',
      fontFamily: v('--font-ui'),
      themeVariables: {
        darkMode: isDark(), background: v('--surface'), fontSize: '14px',
        primaryColor: v('--accent-soft'), primaryTextColor: v('--ink'), primaryBorderColor: v('--accent'),
        secondaryColor: v('--code-bg'), tertiaryColor: v('--surface'), lineColor: v('--ink-3'),
        textColor: v('--ink'), mainBkg: v('--accent-soft'), nodeBorder: v('--accent'),
        clusterBkg: v('--code-bg'), clusterBorder: v('--rule'), edgeLabelBackground: v('--surface'),
        actorBkg: v('--accent-soft'), actorBorder: v('--accent'), noteBkgColor: v('--code-bg'), noteBorderColor: v('--rule'),
      },
      flowchart: { useMaxWidth: true, htmlLabels: true },
    });
    let n = 0;
    for (const pre of sources) {
      try {
        // The lessons write line breaks in labels as a literal \n, which mermaid 11 no longer converts.
        const { svg } = await window.mermaid.render(`diagram-${Date.now()}-${n++}`, pre.textContent.replace(/\\n/g, '<br/>'));
        pre.parentNode.innerHTML = svg; // mermaid output, sanitised by securityLevel: strict
      } catch (e) {
        document.querySelectorAll('body > [id^="ddiagram-"], body > svg[id^="diagram-"]').forEach((x) => x.remove());
      }
    }
  }

  async function mountFigures(scope, providers) {
    if (!providers || !scope.querySelector('.lesson-figure')) return; // an empty list still needs the runtime
    try {
      await loadScript('vendor/figures/lesson-figures.js');
      for (const file of providers) await loadScript('vendor/figures/' + file);
      window.mountLessonFigures(scope);
    } catch (e) { /* a lesson without its figures is still a lesson */ }
  }

  // ══ 4. shared pieces ═════════════════════════════════════════════════

  /** One lesson as a stop on a line: dot, reference, title, type and time. */
  function stop(lesson, opts = {}) {
    const meta = [];
    if (opts.tag) meta.push(h('span', { class: 'tag ' + (opts.tagClass || '') }, opts.tag));
    if (!opts.plain && lesson.a.lesson_type) {
      meta.push(h('span', { class: 'tag ' + (lesson.a.lesson_type === 'capstone' ? 'capstone' : lesson.a.lesson_type === 'build' ? 'build' : '') },
        LESSON_TYPE[lesson.a.lesson_type] || lesson.a.lesson_type));
    }
    if (!opts.plain && lesson.a.time_min) meta.push(h('span', null, fmtMin(opts.minutes || lesson.a.time_min)));
    return h('li', { style: { '--line': lineVar(lesson.a.phase) } },
      h('span', { class: 'dot' + (isDone(lesson) ? ' done' : '') + (opts.minor ? ' minor' : ''), 'aria-hidden': 'true' }),
      h('div', { class: 'stop' },
        h('a', { class: 'stop-title', href: nodeHref(lesson) }, h('span', { class: 'ref' }, lesson.a.ref), lesson.a.title,
          isDone(lesson) ? h('span', { class: 'sr' }, ' (done)') : null),
        meta.length ? h('span', { class: 'stop-meta' }, meta) : null,
        opts.note ? h('p', { class: 'stop-note' }, opts.note) : null));
  }

  function meter(done, total, line) {
    return h('div', { class: 'meter', role: 'img', 'aria-label': `${done} of ${total} done`, style: line ? { '--line': line } : null },
      h('i', { style: { width: (total ? (100 * done) / total : 0) + '%' } }));
  }

  // How each edge type reads, from the source's side and from the target's side.
  const REL = {
    REQUIRES: ['Learn first', 'Needed for'],
    REQUIRES_PHASE: ['Needs all of', 'Lessons that need this whole phase'],
    TEACHES: ['Teaches', 'Taught in'],
    CITES: ['Cites', 'Cited by'],
    CONTAINS: ['Contains', 'Part of'],
    PHASE_REQUIRES: ['Builds on', 'Leads to'],
    RELATED_TO: ['Related concepts', 'Related concepts'],
    IN_CATEGORY: ['Category', 'Concepts in this category'],
    SHIPS: ['Ships', 'Shipped by'],
    INCLUDES: ['Lessons on this path', 'On learning paths'],
    USES: ['Libraries used', 'Used in lessons'],
    IN_COMMUNITY: ['Topic', 'In this topic'],
  };

  /** A node's neighbours, grouped by relationship. dir: 'out' or 'in'. */
  function neighbourGroups(n) {
    const groups = new Map();
    const add = (key, label, dir, node) => {
      if (!groups.has(key)) groups.set(key, { label, dir, nodes: [] });
      const g = groups.get(key);
      if (!g.nodes.includes(node)) g.nodes.push(node);
    };
    for (const e of OUT[n.i]) add(e.t === 'RELATED_TO' ? 'RELATED_TO' : e.t + '>', (REL[e.t] || [e.t])[0], 'out', e.d);
    for (const e of IN[n.i]) {
      if (e.t === 'RELATED_TO') add('RELATED_TO', REL.RELATED_TO[0], 'out', e.s);
      else add(e.t + '<', (REL[e.t] || [e.t, e.t])[1], 'in', e.s);
    }
    const sorted = [...groups.values()];
    for (const g of sorted) g.nodes.sort((a, b) => (a.type === 'lesson' && b.type === 'lesson' ? byRef(a, b) : nodeLabel(a).localeCompare(nodeLabel(b))));
    return sorted;
  }

  /** Sections of links for every relationship of a node, minus the ones a page already shows. */
  function relatedSections(n, skip = []) {
    return neighbourGroups(n).filter((g) => !skip.includes(g.label)).map((g) => {
      const LIMIT = 60;
      const list = h('ul', { class: 'link-cols' });
      const render = (limit) => {
        list.replaceChildren(...g.nodes.slice(0, limit).map((x) =>
          h('li', null, h('a', { href: nodeHref(x) }, trunc(nodeLabel(x), 90)))));
      };
      render(LIMIT);
      const more = g.nodes.length > LIMIT
        ? h('button', { class: 'btn quiet more-btn', type: 'button', onclick: (ev) => { render(Infinity); ev.target.remove(); } }, `Show all ${g.nodes.length}`)
        : null;
      return h('section', { class: 'section' }, h('h2', null, g.label, ' ', h('span', { class: 'muted small' }, g.nodes.length)), list, more);
    });
  }

  // A small tokenizer, enough to tell comments, strings, numbers, keywords
  // and calls apart. Two families: languages with # comments and with // comments.
  const KEYWORDS = {
    python: 'False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield self',
    javascript: 'async await break case catch class const continue default delete do else export extends false finally for from function if import in instanceof let new null of return static super switch this throw true try typeof undefined var void while yield',
    typescript: 'abstract as async await break case catch class const continue default delete do else enum export extends false finally for from function if implements import in instanceof interface let new null of private protected public readonly return static super switch this throw true try type typeof undefined var void while yield',
    rust: 'as async await break const continue crate dyn else enum extern false fn for if impl in let loop match mod move mut pub ref return self Self static struct super trait true type unsafe use where while',
    julia: 'abstract begin break catch const continue do else elseif end export false finally for function global if import in let local macro module mutable nothing quote return struct true try using while',
    bash: 'if then else elif fi for in do done while case esac function return export local set',
    json: 'true false null', yaml: 'true false null yes no', toml: 'true false',
  };
  KEYWORDS.py = KEYWORDS.python; KEYWORDS.ts = KEYWORDS.typescript; KEYWORDS.js = KEYWORDS.javascript;
  KEYWORDS.sh = KEYWORDS.shell = KEYWORDS.bash; KEYWORDS.jsonc = KEYWORDS.json; KEYWORDS.yml = KEYWORDS.yaml;
  const HASH_LANGS = new Set(['python', 'py', 'bash', 'sh', 'shell', 'yaml', 'yml', 'toml', 'julia']);
  const CHAR_LANGS = new Set(['rust', 'julia']); // ' starts a character, not a string
  const NUM = '\\b\\d[\\d_]*(?:\\.[\\d_]+)?(?:[eE][+-]?\\d+)?\\b';
  const IDENT = '[A-Za-z_][A-Za-z0-9_]*';
  const kwSets = {};
  function highlight(code, lang) {
    lang = (lang || '').toLowerCase();
    if (!KEYWORDS[lang] || code.length > 150000) return esc(code);
    const kw = kwSets[lang] || (kwSets[lang] = new Set(KEYWORDS[lang].split(' ')));
    const single = CHAR_LANGS.has(lang) ? "'(?:\\\\.|[^'\\\\\\n])'" : "'(?:\\\\.|[^'\\\\\\n])*'";
    const dbl = '"(?:\\\\.|[^"\\\\\\n])*"';
    const comment = HASH_LANGS.has(lang) ? '#.*$' : '\\/\\/.*$|\\/\\*[\\s\\S]*?\\*\\/';
    const strings = HASH_LANGS.has(lang) ? `"""[\\s\\S]*?"""|'''[\\s\\S]*?'''|${dbl}|${single}` : `${dbl}|${single}|\`(?:\\\\.|[^\`\\\\])*\``;
    const re = new RegExp(`(${comment})|(${strings})|(${NUM})|(${IDENT})`, 'gm');
    let html = '', last = 0, m;
    while ((m = re.exec(code))) {
      html += esc(code.slice(last, m.index));
      last = re.lastIndex;
      const text = esc(m[0]);
      if (m[1]) html += `<span class="tok-c">${text}</span>`;
      else if (m[2]) html += `<span class="tok-s">${text}</span>`;
      else if (m[3]) html += `<span class="tok-n">${text}</span>`;
      else if (kw.has(m[4])) html += `<span class="tok-k">${text}</span>`;
      else if (code[last] === '(') html += `<span class="tok-f">${text}</span>`;
      else html += text;
    }
    return html + esc(code.slice(last));
  }

  function copyText(text, button) {
    const done = () => {
      const before = button.textContent;
      button.textContent = 'Copied';
      setTimeout(() => { button.textContent = before; }, 1400);
    };
    const fallback = () => {
      const ta = h('textarea', { style: { position: 'fixed', opacity: '0' } });
      ta.value = text;
      document.body.append(ta);
      ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { /* nothing to do */ }
      ta.remove();
    };
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(done, fallback);
    else fallback();
  }

  function download(name, text, mime) {
    const url = URL.createObjectURL(new Blob([text], { type: mime }));
    const a = h('a', { href: url, download: name });
    document.body.append(a);
    a.click();
    a.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }

  function codeBlock(text, lang) {
    const box = h('div', { class: 'codefile' });
    box.append(
      h('button', { class: 'copy-btn', type: 'button', onclick: (ev) => copyText(text, ev.currentTarget) }, 'Copy'),
      h('pre', null, h('code', { html: highlight(text, lang) })));
    return box;
  }

  function pageHead(title, lede, kicker) {
    return h('header', { class: 'page-head' }, kicker || null, h('h1', null, title), lede ? h('p', { class: 'lede' }, lede) : null);
  }

  /** A page that is one filterable list: a text box, optional selects, rows, "show more". */
  function listView(o) {
    const state = { q: '', limit: o.limit || 120, sel: (o.selects || []).map((sel) => sel.options[0][0]) };
    const list = h(o.listTag || 'ul', { class: o.listClass || 'rows' });
    const count = h('p', { class: 'count-line', 'aria-live': 'polite' });
    const more = h('button', { class: 'btn quiet more-btn', type: 'button', onclick: () => { state.limit += 300; draw(); } }, 'Show more');
    const haystack = new Map(o.items.map((n) => [n, o.text(n).toLowerCase()]));
    function draw() {
      const words = state.q.toLowerCase().split(/\s+/).filter(Boolean);
      const hits = o.items.filter((n) =>
        words.every((w) => haystack.get(n).includes(w)) &&
        (o.selects || []).every((sel, i) => !state.sel[i] || sel.test(n, state.sel[i])));
      count.textContent = hits.length === o.items.length ? plural(hits.length, o.noun) : `${plural(hits.length, o.noun)} of ${o.items.length.toLocaleString('en')}`;
      list.replaceChildren(...(o.render ? o.render(hits.slice(0, state.limit)) : hits.slice(0, state.limit).map(o.row)));
      more.hidden = hits.length <= state.limit;
      if (!hits.length) list.replaceChildren(h('li', null, h('p', { class: 'desc' }, 'Nothing matches. Try fewer or shorter words.')));
    }
    const controls = h('div', { class: 'controls' },
      h('input', { type: 'search', placeholder: o.placeholder || 'Filter', 'aria-label': o.placeholder || 'Filter', oninput: (ev) => { state.q = ev.target.value; draw(); } }),
      (o.selects || []).map((sel, i) => h('label', null, sel.label,
        h('select', { onchange: (ev) => { state.sel[i] = ev.target.value; draw(); } },
          sel.options.map(([value, label]) => h('option', { value }, label))))));
    draw();
    return h('div', { class: 'page' }, pageHead(o.title, o.lede), controls, count, list, more);
  }

  // ══ 5. search ════════════════════════════════════════════════════════

  let searchIndex = null;
  const TYPE_WEIGHT = { phase: 12, lesson: 9, learning_path: 7, concept: 5, library: 4, resource: 2, artifact: 2, community: 1, track: 3, category: 3, myth: 2 };
  function buildSearchIndex() {
    searchIndex = NODES.map((n) => ({
      n,
      label: nodeLabel(n).toLowerCase(),
      extra: [].concat(n.a.aliases || [], n.a.code_symbols || [], n.a.host || []).join(' ').toLowerCase(),
    }));
  }
  /** Rank nodes for a query: every word must match; label matches beat alias matches. */
  function find(query, limit = 12, types = null) {
    if (!searchIndex) buildSearchIndex();
    const words = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    const q = words.join(' ');
    const scored = [];
    for (const item of searchIndex) {
      if (types && !types.includes(item.n.type)) continue;
      let score = 0;
      for (const w of words) {
        const at = item.label.indexOf(w);
        if (at === 0) score += 60;
        else if (at > 0 && /[^a-z0-9]/.test(item.label[at - 1])) score += 40;
        else if (at > 0) score += 18;
        else if (item.extra.includes(w)) score += 12;
        else { score = -1; break; }
      }
      if (score < 0) continue;
      if (item.label === q || item.label.endsWith(' ' + q)) score += 50;
      score += TYPE_WEIGHT[item.n.type] || 0;
      if (item.n.type === 'concept' && item.n.a.canonical) score += 8;
      score -= Math.min(item.label.length, 80) / 8;
      scored.push([score, item.n]);
    }
    scored.sort((a, b) => b[0] - a[0]);
    return scored.slice(0, limit).map((x) => x[1]);
  }
  function nodeSub(n) {
    if (n.type === 'lesson') return phaseOf(n) ? phaseOf(n).a.title : '';
    if (n.type === 'concept') return n.a.definition || '';
    if (n.type === 'resource') return n.a.host || '';
    if (n.type === 'artifact') return n.a.description || '';
    if (n.type === 'learning_path') return n.a.summary || '';
    if (n.type === 'phase') return plural(lessonsOf(n).length, 'lesson');
    return '';
  }

  function initSearch() {
    const input = document.getElementById('search');
    const box = document.getElementById('search-results');
    let active = -1;
    const close = () => { box.hidden = true; input.setAttribute('aria-expanded', 'false'); active = -1; };
    const select = (i) => {
      const links = [...box.querySelectorAll('a')];
      if (!links.length) return;
      active = (i + links.length) % links.length;
      links.forEach((a, k) => a.setAttribute('aria-selected', k === active ? 'true' : 'false'));
      links[active].scrollIntoView({ block: 'nearest' });
    };
    input.addEventListener('input', () => {
      const q = input.value.trim();
      if (!q) return close();
      const hits = find(q, 14);
      box.replaceChildren(...(hits.length
        ? hits.map((n) => h('a', { href: nodeHref(n), role: 'option', 'aria-selected': 'false' },
            h('span', { class: 'kind' }, TYPE_NAME[n.type] || n.type),
            h('span', null, trunc(nodeLabel(n), 80), nodeSub(n) ? h('span', { class: 'sub' }, trunc(nodeSub(n), 110)) : null)))
        : [h('p', { class: 'search-empty' }, `Nothing found for “${q}”. Try one word, or part of a word.`)]));
      box.hidden = false;
      input.setAttribute('aria-expanded', 'true');
      active = -1;
    });
    input.addEventListener('keydown', (ev) => {
      if (ev.key === 'ArrowDown') { ev.preventDefault(); select(active + 1); }
      else if (ev.key === 'ArrowUp') { ev.preventDefault(); select(active - 1); }
      else if (ev.key === 'Enter') {
        const links = box.querySelectorAll('a');
        const pick = links[Math.max(active, 0)];
        if (pick && !box.hidden) { location.hash = pick.getAttribute('href'); input.blur(); close(); }
      } else if (ev.key === 'Escape') { close(); input.blur(); }
    });
    box.addEventListener('click', (ev) => { if (ev.target.closest('a')) { close(); input.value = ''; } });
    document.addEventListener('click', (ev) => { if (!ev.target.closest('.search')) close(); });
    document.addEventListener('keydown', (ev) => {
      const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement.tagName);
      if (ev.key === '/' && !typing && !ev.metaKey && !ev.ctrlKey) { ev.preventDefault(); input.focus(); input.select(); }
    });
  }

  // ══ 6. views ═════════════════════════════════════════════════════════
  // Each view returns { el, title, nav }.

  // ---- home: the curriculum as a transit map --------------------------

  /** Place every phase on a grid: rows follow prerequisites, columns keep branches apart. */
  function phaseLayout() {
    const phases = all('phase');
    const parents = new Map(phases.map((p) => [p, out(p, 'PHASE_REQUIRES').map((e) => e.d)]));
    const children = new Map(phases.map((p) => [p, inn(p, 'PHASE_REQUIRES').map((e) => e.s)]));
    // Row = longest chain of prerequisites above the phase.
    const row = new Map();
    const place = (p) => {
      if (row.has(p)) return row.get(p);
      row.set(p, 0); // guards against a cycle in the source data
      const r = Math.max(-1, ...parents.get(p).map(place)) + 1;
      row.set(p, r);
      return r;
    };
    phases.forEach(place);
    // A phase that leads somewhere sits right above what it leads to, so its line is short.
    [...phases].sort((a, b) => row.get(b) - row.get(a)).forEach((p) => {
      const kids = children.get(p);
      if (kids.length) row.set(p, Math.max(row.get(p), Math.min(...kids.map((c) => row.get(c))) - 1));
    });
    // How much of the curriculum hangs below each phase: the trunk keeps column 0.
    const below = new Map();
    const reach = (p) => {
      if (!below.has(p)) {
        const seen = new Set();
        const walk = (x) => children.get(x).forEach((c) => { if (!seen.has(c)) { seen.add(c); walk(c); } });
        walk(p);
        below.set(p, seen.size);
      }
      return below.get(p);
    };
    const col = new Map();
    const rows = uniq(phases.map((p) => row.get(p))).sort((a, b) => a - b);
    for (const r of rows) {
      const taken = new Set();
      phases.filter((p) => row.get(p) === r).sort((a, b) => reach(b) - reach(a) || a.a.num - b.a.num).forEach((p) => {
        let c = parents.get(p).length ? Math.min(...parents.get(p).map((q) => col.get(q) || 0)) : 0;
        while (taken.has(c)) c++;
        taken.add(c);
        col.set(p, c);
      });
    }
    return { phases, parents, row, col };
  }

  function roundedPath(points, radius) {
    let d = `M${points[0][0]},${points[0][1]}`;
    for (let i = 1; i < points.length - 1; i++) {
      const [px, py] = points[i - 1], [x, y] = points[i], [nx, ny] = points[i + 1];
      const r = Math.min(radius, Math.hypot(x - px, y - py) / 2, Math.hypot(nx - x, ny - y) / 2);
      const ax = x - Math.sign(x - px) * r, ay = y - Math.sign(y - py) * r;
      const bx = x + Math.sign(nx - x) * r, by = y + Math.sign(ny - y) * r;
      d += ` L${ax},${ay} Q${x},${y} ${bx},${by}`;
    }
    const end = points[points.length - 1];
    return d + ` L${end[0]},${end[1]}`;
  }

  function phaseMap(animate) {
    const { phases, parents, row, col } = phaseLayout();
    const COL = 272, ROW = 66, X0 = 38, Y0 = 38;
    const x = (p) => X0 + col.get(p) * COL, y = (p) => Y0 + row.get(p) * ROW;
    const width = X0 + Math.max(...phases.map((p) => col.get(p))) * COL + 250;
    const height = Y0 + Math.max(...phases.map((p) => row.get(p))) * ROW + 44;
    const occupied = new Set(phases.map((p) => `${col.get(p)},${row.get(p)}`));
    const blocked = (c, r1, r2) => { for (let r = r1 + 1; r < r2; r++) if (occupied.has(`${c},${r}`)) return true; return false; };

    const tracks = [], stations = [];
    for (const child of phases) {
      for (const parent of parents.get(child)) {
        let points;
        if (col.get(parent) === col.get(child)) {
          points = [[x(parent), y(parent)], [x(child), y(child)]];
        } else {
          // Turn next to the child, unless that would run the line through a station.
          const nearChild = !blocked(col.get(parent), row.get(parent), row.get(child)) || blocked(col.get(child), row.get(parent), row.get(child));
          const turnY = nearChild ? y(child) - ROW / 2 : y(parent) + ROW / 2;
          points = [[x(parent), y(parent)], [x(parent), turnY], [x(child), turnY], [x(child), y(child)]];
        }
        tracks.push(s('path', {
          class: 'track', d: roundedPath(points, 16), pathLength: 1,
          style: { stroke: lineVar(child.a.num), '--d': row.get(parent) },
        }));
      }
    }
    for (const p of phases) {
      const lessons = lessonsOf(p), done = doneCount(lessons), complete = lessons.length > 0 && done === lessons.length;
      const meta = [plural(lessons.length, 'lesson'), p.a.hours ? `${Math.round(p.a.hours)} h` : null, done ? `${done} done` : null].filter(Boolean).join(', ');
      stations.push(s('a', { class: 'station', href: nodeHref(p), 'aria-label': `Phase ${p.a.num}: ${p.a.title}. ${meta}`, style: { '--d': row.get(p), color: lineVar(p.a.num) } },
        s('rect', { class: 'st-hit', x: x(p) - 20, y: y(p) - 24, width: 240, height: 48 }),
        s('circle', { class: 'st-ring' + (complete ? ' done' : ''), cx: x(p), cy: y(p), r: 16, style: { stroke: lineVar(p.a.num) } }),
        s('text', { class: 'st-num' + (complete ? ' done' : ''), x: x(p), y: y(p) + 5 }, p.a.num),
        s('text', { class: 'st-title', x: x(p) + 28, y: y(p) - 1 }, p.a.title),
        s('text', { class: 'st-meta', x: x(p) + 28, y: y(p) + 16 }, meta)));
    }
    return s('svg', { class: 'map' + (animate ? ' draw' : ''), viewBox: `0 0 ${width} ${height}`, role: 'group', 'aria-label': 'Curriculum map: phases and what each one builds on' }, tracks, stations);
  }

  let mapDrawn = false;
  function viewHome() {
    const lessons = all('lesson');
    const glossary = all('concept').filter((c) => c.a.canonical).length;
    const routePath = all('learning_path').find((p) => p.a.kind === 'custom-route');
    const picks = [
      lessons.length && ['From the beginning', nodeHref(lessons[0]), 'Start at the first lesson. Every phase builds on the ones above it on the map.'],
      routePath && ['Already working with machine learning', nodeHref(routePath), routePath.a.summary],
      ['With a goal in mind', '#/planner', 'Choose the lesson you want to reach and get the ordered list of everything it depends on.'],
      ['Looking something up', '#/concepts', `${glossary} glossary concepts, each with what people say and what it means.`],
    ].filter(Boolean);

    // Where to continue: the first unfinished lesson of each phase already started.
    const next = [];
    for (const p of all('phase')) {
      const ls = lessonsOf(p);
      if (doneCount(ls) && doneCount(ls) < ls.length) next.push(ls.find((l) => !isDone(l)));
    }

    const el = h('div', { class: 'page' },
      h('header', { class: 'page-head hero' },
        h('h1', null, D.title),
        h('p', { class: 'lede' }, D.tagline),
        h('p', { class: 'muted' }, [
          plural(lessons.length, 'lesson') + ` in ${plural(all('phase').length, 'phase')}`,
          plural(all('concept').length, 'concept'),
          plural(all('resource').length, 'paper and link', 'papers and links'),
          plural(all('artifact').length, 'reusable prompt and skill', 'reusable prompts and skills'),
        ].join(', ') + '. Select a station to open a phase.')),
      h('div', { class: 'card map-card' },
        phaseMap(!mapDrawn),
        h('ul', { class: 'legend', 'aria-label': 'Lines' }, D.lines.map((l, i) => h('li', null, h('i', { style: { '--line': `var(--line-${i})` } }), l.name)))),
      h('ol', { class: 'line-list phase-list-mobile' }, all('phase').map((p) =>
        h('li', { style: { '--line': lineVar(p.a.num) } },
          h('span', { class: 'dot', 'aria-hidden': 'true' }),
          h('div', { class: 'stop' },
            h('a', { class: 'stop-title', href: nodeHref(p) }, h('span', { class: 'ref' }, p.a.num), p.a.title),
            h('span', { class: 'stop-meta' }, plural(lessonsOf(p).length, 'lesson')))))),
      h('div', { class: 'home-cols' },
        next.length ? h('section', { class: 'card' }, h('h2', null, 'Continue'),
          h('ol', { class: 'line-list compact' }, next.slice(0, 5).map((l) => stop(l, { plain: true })))) : null,
        h('section', { class: 'card' }, h('h2', null, 'Where to start'),
          h('ul', { class: 'pick-list' }, picks.map(([title, href, text]) => h('li', null, h('a', { href }, title), h('p', null, text))))),
        h('section', { class: 'card' }, h('h2', null, 'Learning paths'),
          h('ul', { class: 'pick-list' }, sortedPaths().slice(0, 4).map((p) =>
            h('li', null, h('a', { href: nodeHref(p) }, p.a.title), h('p', null, `${plural(out(p, 'INCLUDES').length, 'lesson')}, ${fmtMin(p.a.minutes)}`)))),
          h('p', { class: 'small' }, h('a', { href: '#/paths' }, `All ${all('learning_path').length} paths`)))));
    mapDrawn = true;
    return { el, title: null, nav: 'home' };
  }

  // ---- phase -----------------------------------------------------------

  function viewPhase(num) {
    const p = byId.get('phase:' + Number(num));
    if (!p) return notFound();
    const lessons = lessonsOf(p), done = doneCount(lessons);
    const line = lineVar(p.a.num);
    const minutes = lessons.reduce((sum, l) => sum + (l.a.time_min || 0), 0);
    const tracks = all('track').filter((t) => t.a.phase === p.a.num).sort((a, b) => a.a.start - b.a.start);
    const trackOf = (l) => tracks.find((t) => l.a.num >= t.a.start && l.a.num <= t.a.end);

    const items = [];
    let current;
    for (const l of lessons) {
      const t = trackOf(l);
      if (tracks.length && t !== current) {
        current = t;
        items.push(h('li', { class: 'group', style: { '--line': line } },
          t ? `Track ${t.a.letter}: ${t.a.title}` : 'Standalone lessons',
          t && t.a.note ? h('p', { class: 'stop-note' }, t.a.note) : null));
      }
      items.push(stop(l, { note: l.a.hook ? trunc(l.a.hook, 150) : null }));
    }
    const phaseChips = (edges, pick) => h('ul', { class: 'chips' }, edges.map((e) => h('li', null, h('a', { href: nodeHref(pick(e)) }, nodeLabel(pick(e))))));
    const before = out(p, 'PHASE_REQUIRES'), after = inn(p, 'PHASE_REQUIRES');

    const el = h('div', { class: 'page', style: { '--line': line } },
      h('header', { class: 'page-head' },
        h('a', { class: 'kicker', href: '#/' }, 'Curriculum map'),
        h('h1', { style: { display: 'flex', gap: '16px', 'align-items': 'center' } },
          h('span', { class: 'roundel big' + (done === lessons.length && done ? ' done' : '') }, p.a.num), ' ', p.a.title),
        h('ul', { class: 'facts' },
          h('li', null, h('b', null, lessons.length), lessons.length === 1 ? 'lesson' : 'lessons'),
          minutes ? h('li', null, h('b', null, fmtMin(minutes)), 'of lesson time') : null,
          h('li', null, h('b', null, D.lines[D.phase_line[String(p.a.num)] || 0].name), 'line'),
          done ? h('li', null, h('b', null, `${done} of ${lessons.length}`), 'done') : null),
        done ? h('div', { style: { 'max-width': '420px', 'margin-top': '14px' } }, meter(done, lessons.length)) : null),
      before.length ? h('section', { class: 'section', style: { 'margin-top': '0' } }, h('h2', null, 'Builds on'), phaseChips(before, (e) => e.d)) : null,
      h('section', { class: 'section' }, h('h2', null, 'Lessons'), h('ol', { class: 'line-list' }, items)),
      after.length ? h('section', { class: 'section' }, h('h2', null, 'Leads to'), phaseChips(after, (e) => e.s)) : null,
      h('p', { class: 'section small' }, h('a', { href: graphHref(p) }, 'See this phase in the graph')));
    return { el, title: `Phase ${p.a.num}: ${p.a.title}`, nav: 'home' };
  }

  // ---- lesson ------------------------------------------------------------

  function viewLesson(pp, ll) {
    const l = byId.get(`lesson:${pp}/${ll}`);
    if (!l) return notFound();
    const phase = phaseOf(l);
    const line = lineVar(l.a.phase);
    const siblings = phase ? lessonsOf(phase) : [l];
    const at = siblings.indexOf(l);
    const terms = out(l, 'TEACHES'), reads = out(l, 'CITES'), libs = out(l, 'USES');

    const doneBtn = h('button', { class: 'btn', type: 'button' });
    const paintDone = () => {
      doneBtn.className = 'btn' + (isDone(l) ? ' is-done' : ' primary');
      doneBtn.textContent = isDone(l) ? 'Done. Mark as not done' : 'Mark as done';
      doneBtn.setAttribute('aria-pressed', isDone(l) ? 'true' : 'false');
    };
    doneBtn.addEventListener('click', () => { setDone(l, !isDone(l)); paintDone(); });
    paintDone();

    // The route through this lesson: what comes first, this lesson, what it opens up.
    const before = uniq(out(l, 'REQUIRES').map((e) => e.d)).sort(byRef);
    const wholePhases = uniq(out(l, 'REQUIRES_PHASE').map((e) => e.d));
    const after = uniq(inn(l, 'REQUIRES').map((e) => e.s)).sort(byRef);
    const label = (text) => h('li', { class: 'muted small', style: { '--line': line } }, text);
    const route = h('ol', { class: 'line-list compact' },
      before.length || wholePhases.length ? label('Learn first') : null,
      wholePhases.map((ph) => h('li', { style: { '--line': lineVar(ph.a.num) } },
        h('span', { class: 'dot minor', 'aria-hidden': 'true' }),
        h('div', { class: 'stop' }, h('a', { class: 'stop-title', href: nodeHref(ph) }, `All of phase ${ph.a.num}: ${ph.a.title}`)))),
      before.map((x) => stop(x, { plain: true, minor: true })),
      h('li', { style: { '--line': line } }, h('span', { class: 'dot here', 'aria-hidden': 'true' }), h('div', { class: 'stop' }, h('b', null, 'This lesson'))),
      after.length ? label('Then you can take') : null,
      after.slice(0, 6).map((x) => stop(x, { plain: true, minor: true })),
      after.length > 6 ? h('li', { class: 'small', style: { '--line': line } }, h('a', { href: graphHref(l) }, `and ${after.length - 6} more`)) : null);

    const tocSection = h('section', { class: 'toc-section', hidden: true }, h('h2', null, 'On this page'), h('ul', { class: 'toc' }));
    const community = l.a.community != null ? byId.get('community:' + l.a.community) : null;
    const aside = h('aside', { class: 'lesson-aside', 'aria-label': 'Route and contents' },
      h('section', null, h('h2', null, 'Route'), route),
      h('section', null, h('h2', null, 'Go further'), h('div', { class: 'aside-links' },
        before.length ? h('a', { href: `#/planner?to=${l.a.ref}` }, 'Plan the full route to this lesson') : null,
        h('a', { href: graphHref(l) }, 'See this lesson in the graph'),
        community ? h('a', { href: nodeHref(community) }, 'Related topic: ' + trunc(nodeLabel(community), 48)) : null)),
      tocSection);

    const tabs = h('div', { class: 'tabs', role: 'tablist', 'aria-label': 'Parts of the lesson' });
    const panels = h('div', null, h('p', { class: 'panel-empty' }, l.a.text ? 'Loading the lesson…' : null));
    const el = h('article', { class: 'page', style: { '--line': line } },
      h('header', { class: 'page-head lesson-head' },
        phase ? h('a', { class: 'kicker', href: nodeHref(phase) }, h('span', { class: 'roundel' }, phase.a.num), `${phase.a.title}, lesson ${at + 1} of ${siblings.length}`) : null,
        h('h1', null, l.a.title),
        l.a.hook ? h('p', { class: 'hook' }, l.a.hook) : null,
        h('ul', { class: 'facts' },
          l.a.lesson_type ? h('li', null, h('b', null, LESSON_TYPE[l.a.lesson_type] || l.a.lesson_type)) : null,
          l.a.time_min ? h('li', null, h('b', null, fmtMin(l.a.time_min))) : null,
          l.a.languages ? h('li', null, l.a.languages.join(', ')) : null,
          libs.length ? h('li', null, 'Uses ', libs.map((e, i) => [i ? ', ' : '', h('a', { href: nodeHref(e.d) }, e.d.a.name)])) : null),
        h('div', { class: 'lesson-actions btn-row' }, doneBtn)),
      tabs,
      h('div', { class: 'lesson-grid' }, panels, aside),
      h('nav', { class: 'prevnext', 'aria-label': 'Previous and next lesson' },
        at > 0 ? h('a', { href: nodeHref(siblings[at - 1]) }, h('span', null, 'Previous'), h('b', null, nodeLabel(siblings[at - 1]))) : null,
        at < siblings.length - 1 ? h('a', { class: 'next', href: nodeHref(siblings[at + 1]) }, h('span', null, 'Next'), h('b', null, nodeLabel(siblings[at + 1]))) : null));

    const build = (content) => {
      content = content || {};
      const defs = [];
      if (content.html) defs.push(['Lesson', null, () => lessonTextPanel(content, tocSection)]);
      if (content.code) defs.push(['Code', content.code.length, () => codePanel(content.code)]);
      if (content.quiz) defs.push(['Quiz', content.quiz.length, () => quizPanel(content.quiz)]);
      if (terms.length) defs.push(['Key terms', terms.length, () => termsPanel(terms)]);
      if (reads.length) defs.push(['Reading', reads.length, () => readingPanel(reads)]);
      if (content.artifacts) defs.push(['Prompts and skills', content.artifacts.length, () => artifactsPanel(content.artifacts)]);
      if (!defs.length) {
        panels.replaceChildren(h('p', { class: 'panel-empty' }, 'This lesson has no text in this export. Its place in the curriculum is shown in the route.'));
        return;
      }
      const built = new Map();
      const show = (i) => {
        [...tabs.children].forEach((b, k) => { b.setAttribute('aria-selected', k === i ? 'true' : 'false'); b.tabIndex = k === i ? 0 : -1; });
        if (!built.has(i)) built.set(i, h('div', { role: 'tabpanel', 'aria-label': defs[i][0] }, defs[i][2]()));
        panels.replaceChildren(built.get(i));
        tocSection.hidden = !(i === 0 && content.html && tocSection.querySelector('a'));
      };
      tabs.replaceChildren(...defs.map(([name, n], i) =>
        h('button', { type: 'button', role: 'tab', onclick: () => show(i) }, name, n != null ? h('span', { class: 'n' }, n) : null)));
      tabs.addEventListener('keydown', (ev) => {
        const i = [...tabs.children].indexOf(document.activeElement);
        const move = ev.key === 'ArrowRight' ? 1 : ev.key === 'ArrowLeft' ? -1 : 0;
        if (i < 0 || !move) return;
        const j = (i + move + defs.length) % defs.length;
        show(j);
        tabs.children[j].focus();
      });
      show(0);
    };
    if (l.a.text) {
      loadRes(`data/lessons/${l.a.ref.replace('/', '-')}.js`).then(build, () => {
        panels.replaceChildren(h('p', { class: 'panel-empty' },
          'The text of this lesson could not be loaded. If you opened a single HTML file copied out of its folder, open index.html from the complete folder, or use the single-file build.'));
      });
    } else build(null);

    return { el, title: nodeLabel(l), nav: 'home' };
  }

  function lessonTextPanel(content, tocSection) {
    const body = h('div', { class: 'prose', html: content.html });
    body.querySelectorAll('pre.code[data-lang] > code').forEach((code) => {
      code.innerHTML = highlight(code.textContent, code.parentNode.dataset.lang);
    });
    const jump = (id) => { const target = body.querySelector('#' + CSS.escape(id)); if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' }); };
    body.addEventListener('click', (ev) => {
      const a = ev.target.closest('a.anchor-link');
      if (a) { ev.preventDefault(); jump(a.dataset.anchor); }
    });
    const toc = tocSection.querySelector('.toc');
    toc.replaceChildren(...content.toc.filter((t) => t[0] === 2).map(([, id, text]) =>
      h('li', null, h('a', { tabindex: 0, role: 'link', onclick: () => jump(id), onkeydown: (ev) => { if (ev.key === 'Enter') jump(id); } }, text))));
    // Diagrams and figures need the element to be in the page before they can measure it.
    setTimeout(() => { renderDiagrams(body); mountFigures(body, content.figures); }, 0);
    return body;
  }

  function codePanel(files) {
    const view = h('div');
    const tabs = h('div', { class: 'file-tabs', role: 'group', 'aria-label': 'Files' });
    const show = (i) => {
      [...tabs.children].forEach((b, k) => b.setAttribute('aria-pressed', k === i ? 'true' : 'false'));
      const f = files[i];
      view.replaceChildren(codeBlock(f.text, f.lang),
        f.truncated ? h('p', { class: 'code-note' }, 'This file is long, so only its first part is shown here. The full file is in the curriculum folder.') : null,
        f.more ? h('p', { class: 'code-note' }, `${plural(f.more, 'more file')} in the lesson's code folder.`) : null);
    };
    files.forEach((f, i) => tabs.append(h('button', { type: 'button', onclick: () => show(i) }, f.name)));
    show(0);
    return h('div', null, files.length > 1 ? tabs : h('p', { class: 'code-note', style: { margin: '0 0 10px' } }, files[0].name), view);
  }

  function quizPanel(questions) {
    let answered = 0, right = 0;
    const score = h('p', { class: 'quiz-score', 'aria-live': 'polite' }, `${plural(questions.length, 'question')}. Answers are checked here and are not stored.`);
    const groups = [['pre', 'Before you start'], ['post', 'After the lesson'], ['', 'Questions']];
    const box = h('div', { class: 'quiz' }, score);
    const known = new Set(groups.map((g) => g[0]));
    for (const [stage, title] of groups) {
      const qs = questions.filter((q) => (known.has(q.stage) ? q.stage : '') === stage);
      if (!qs.length) continue;
      if (stage || box.children.length > 1) box.append(h('h3', null, title));
      for (const q of qs) {
        const why = h('p', { class: 'why', hidden: true });
        const options = h('div', { class: 'options' }, q.options.map((text, i) =>
          h('button', { type: 'button', onclick: (ev) => {
            const buttons = [...options.children];
            buttons.forEach((b, k) => { b.disabled = true; if (k === q.correct) b.classList.add('right'); });
            const ok = i === q.correct;
            if (!ok) ev.currentTarget.classList.add('wrong');
            answered++; right += ok ? 1 : 0;
            why.replaceChildren(h('b', null, ok ? 'Correct. ' : 'Not quite. '), q.why);
            why.hidden = false;
            score.textContent = `${right} of ${answered} correct so far, ${questions.length - answered} to go.`;
            if (answered === questions.length) score.textContent = `${right} of ${questions.length} correct.`;
          } }, text)));
        box.append(h('div', { class: 'question', role: 'group', 'aria-label': q.q }, h('p', { class: 'q-text' }, q.q), options, why));
      }
    }
    return box;
  }

  function termsPanel(edges) {
    const seen = new Set();
    const rows = [];
    for (const e of edges) {
      if (seen.has(e.d)) continue;
      seen.add(e.d);
      const folk = e.a.folk_definition || e.d.a.folk_definition;
      rows.push(h('tr', null,
        h('td', null, h('a', { href: nodeHref(e.d) }, e.a.term_as_written || e.d.a.name || e.d.label)),
        h('td', { class: 'folk' }, folk ? String(folk).replace(/^"|"$/g, '') : ''),
        h('td', null, e.a.definition || e.d.a.definition || '')));
    }
    return h('div', { class: 'table-wrap' }, h('table', { class: 'terms-table' },
      h('thead', null, h('tr', null, h('th', null, 'Term'), h('th', null, 'What people say'), h('th', null, 'What it means'))),
      h('tbody', null, rows)));
  }

  function readingPanel(edges) {
    return h('ul', { class: 'read-list' }, edges.map((e) => h('li', null,
      h('a', { class: 'title', href: e.d.a.url, target: '_blank', rel: 'noopener' }, e.d.a.title || e.d.label),
      h('p', null, [e.a.note ? e.a.note.replace(/^[\s—–:-]+/, '') : null].filter(Boolean)),
      h('p', { class: 'small' }, e.d.a.host || '', ' ', h('a', { href: nodeHref(e.d) }, `Cited in ${plural(inn(e.d, 'CITES').length, 'place')}`)))));
  }

  function artifactsPanel(items) {
    return h('div', null,
      h('p', { class: 'panel-empty' }, 'Ready-to-use material that ships with this lesson. Copy it into your own assistant or agent setup.'),
      items.map((a) => h('div', { class: 'artifact' },
        h('h3', null, a.name, a.kind ? h('span', { class: 'tag' }, a.kind) : null),
        codeBlock(a.text, 'markdown'))));
  }

  // ---- concepts ----------------------------------------------------------

  function viewConcepts() {
    const concepts = [...all('concept')].sort((a, b) => a.label.localeCompare(b.label, 'en', { sensitivity: 'base' }));
    const cats = uniq(concepts.map((c) => c.a.category).filter(Boolean)).sort();
    const el = listView({
      title: 'Concepts',
      lede: 'Every term the curriculum defines. Glossary terms come with what people usually say, what the term means, and where the two differ.',
      items: concepts,
      noun: 'concept',
      placeholder: 'Filter concepts',
      limit: 400,
      listTag: 'div', listClass: 'concept-index',
      text: (c) => [c.label, (c.a.aliases || []).join(' ')].join(' '),
      selects: [
        { label: 'Show', options: [['glossary', 'Glossary terms'], ['', 'All terms, including lesson-only']], test: (c) => c.a.canonical },
        { label: 'Category', options: [['', 'All categories']].concat(cats.map((c) => [c, c])), test: (c, v) => c.a.category === v },
      ],
      render: (hits) => {
        const blocks = [];
        let letter, list;
        for (const c of hits) {
          const first = /[a-z]/i.test(c.label[0]) ? c.label[0].toUpperCase() : '0–9';
          if (first !== letter) {
            letter = first;
            list = h('ul', { class: 'link-cols' });
            blocks.push(h('h2', { class: 'letter' }, letter), list);
          }
          list.append(h('li', null, h('a', { href: nodeHref(c) }, c.label),
            c.a.canonical ? null : h('span', { class: 'sub' }, ' ' + (c.a.first_seen_in || ''))));
        }
        return blocks;
      },
    });
    return { el, title: 'Concepts', nav: 'concepts' };
  }

  function viewConcept(slug) {
    const c = byId.get('concept:' + slug);
    if (!c) return notFound();
    const taught = inn(c, 'TEACHES');
    const definition = c.a.definition || (taught.find((e) => e.a.definition) || { a: {} }).a.definition;
    const folk = c.a.folk_definition ? String(c.a.folk_definition).replace(/^"|"$/g, '') : null;
    const category = out(c, 'IN_CATEGORY')[0];
    const related = uniq(out(c, 'RELATED_TO').map((e) => e.d).concat(inn(c, 'RELATED_TO').map((e) => e.s))).sort((a, b) => a.label.localeCompare(b.label));
    const cites = out(c, 'CITES');
    const byLesson = new Map();
    for (const e of taught) if (!byLesson.has(e.s)) byLesson.set(e.s, e);
    const lessons = [...byLesson.keys()].sort(byRef);
    const notes = [['Why it matters', c.a.why_it_matters], ['In practice', c.a.in_practice], ['Where people get confused', c.a.confusion]].filter((x) => x[1]);

    const el = h('div', { class: 'page' },
      h('header', { class: 'page-head' },
        h('a', { class: 'kicker', href: '#/concepts' }, 'Concepts', category ? ', ' + category.d.label : ''),
        h('h1', null, c.label),
        c.a.aliases && c.a.aliases.length ? h('p', { class: 'muted' }, 'Also written ', c.a.aliases.join(', ')) : null,
        !folk && definition ? h('p', { class: 'definition' }, definition) : null),
      folk ? h('div', { class: 'say-means' },
        h('div', { class: 'said' }, h('h2', null, 'What people say'), h('p', null, folk)),
        h('div', null, h('h2', null, 'What it means'), h('p', null, definition || ''))) : null,
      notes.length ? h('div', { class: 'notes' }, notes.map(([title, text]) => h('section', null, h('h2', null, title), h('p', null, text)))) : null,
      lessons.length ? h('section', { class: 'section' }, h('h2', null, 'Taught in'),
        h('ol', { class: 'line-list' }, lessons.map((l) => {
          const own = byLesson.get(l).a.definition;
          return stop(l, { note: own && own !== definition ? `In this lesson: ${own}` : null });
        }))) : null,
      related.length ? h('section', { class: 'section' }, h('h2', null, 'Related concepts'),
        h('ul', { class: 'chips' }, related.map((r) => h('li', null, h('a', { href: nodeHref(r) }, r.label))))) : null,
      cites.length ? h('section', { class: 'section' }, h('h2', null, 'References'), readingPanel(cites)) : null,
      h('p', { class: 'section small' }, h('a', { href: graphHref(c) }, 'See this concept in the graph')));
    return { el, title: c.label, nav: 'concepts' };
  }

  // ---- learning paths ------------------------------------------------------

  const PATH_KIND = { 'custom-route': 'Custom route', 'career-route': 'Career route' };
  function sortedPaths() {
    const rank = (p) => (p.a.kind === 'custom-route' ? 0 : p.a.kind === 'career-route' ? 1 : 2);
    return [...all('learning_path')].sort((a, b) => rank(a) - rank(b) || a.a.title.localeCompare(b.a.title));
  }
  const pathSteps = (p) => out(p, 'INCLUDES').sort((a, b) => (a.a.order || 0) - (b.a.order || 0));

  function viewPaths() {
    const el = h('div', { class: 'page' },
      pageHead('Learning paths', 'Routes through the curriculum for a goal or a role. A path picks lessons from several phases and puts them in a working order.'),
      h('ul', { class: 'rows' }, sortedPaths().map((p) => {
        const lessons = pathSteps(p).map((e) => e.d), done = doneCount(lessons);
        return h('li', null,
          h('a', { class: 'title', href: nodeHref(p) }, p.a.title),
          h('span', { class: 'side' },
            PATH_KIND[p.a.kind] ? h('span', { class: 'tag' }, PATH_KIND[p.a.kind]) : null,
            `${plural(lessons.length, 'lesson')}, ${fmtMin(p.a.minutes)}`,
            done ? meter(done, lessons.length) : null),
          h('p', { class: 'desc' }, p.a.summary || ''));
      })),
      h('p', { class: 'section' }, 'None of these fit? ', h('a', { href: '#/planner' }, 'Plan your own syllabus'), ' from any lesson you want to reach.'));
    return { el, title: 'Learning paths', nav: 'paths' };
  }

  function viewPath(key) {
    const p = all('learning_path').find((x) => x.a.key === key);
    if (!p) return notFound();
    const steps = pathSteps(p), lessons = steps.map((e) => e.d), done = doneCount(lessons);
    const el = h('div', { class: 'page' },
      h('header', { class: 'page-head' },
        h('a', { class: 'kicker', href: '#/paths' }, 'Learning paths'),
        h('h1', null, p.a.title),
        p.a.summary ? h('p', { class: 'lede' }, p.a.summary) : null,
        h('ul', { class: 'facts' },
          h('li', null, h('b', null, lessons.length), 'lessons'),
          p.a.minutes ? h('li', null, h('b', null, fmtMin(p.a.minutes))) : null,
          h('li', null, h('b', null, uniq(lessons.map((l) => l.a.phase)).length), 'phases'),
          done ? h('li', null, h('b', null, `${done} of ${lessons.length}`), 'done') : null),
        done ? h('div', { style: { 'max-width': '420px', 'margin-top': '14px' } }, meter(done, lessons.length)) : null),
      h('ol', { class: 'line-list' }, steps.map((e) => stop(e.d, {
        tag: e.a.required === false ? 'Optional' : null,
        note: e.a.note || null,
        minutes: e.a.minutes,
      }))));
    return { el, title: p.a.title, nav: 'paths' };
  }

  // ---- planner: from a goal to an ordered syllabus --------------------------

  /** Everything the targets depend on, in an order that never puts a lesson before its prerequisites. */
  function planFor(targets, wholePhases) {
    const need = new Set();
    const stack = [...targets];
    while (stack.length) {
      const l = stack.pop();
      if (need.has(l)) continue;
      need.add(l);
      for (const e of out(l, 'REQUIRES')) stack.push(e.d);
      if (wholePhases) for (const e of out(l, 'REQUIRES_PHASE')) stack.push(...lessonsOf(e.d));
    }
    const pending = [...need].sort(byRef);
    const placed = new Set();
    const order = [];
    while (pending.length) {
      // The earliest lesson in curriculum order whose prerequisites are all placed.
      let i = pending.findIndex((l) => out(l, 'REQUIRES').every((e) => !need.has(e.d) || placed.has(e.d)));
      if (i < 0) i = 0; // a cycle in the source data: do not get stuck
      const [l] = pending.splice(i, 1);
      placed.add(l);
      order.push(l);
    }
    const assumed = uniq([...need].flatMap((l) => out(l, 'REQUIRES_PHASE').map((e) => e.d)))
      .filter((ph) => !lessonsOf(ph).every((x) => need.has(x))).sort((a, b) => a.a.num - b.a.num);
    return { order, assumed };
  }

  function viewPlanner(query) {
    const targets = uniq((query.get('to') || '').split(',').map((r) => byId.get('lesson:' + r.trim())).filter(Boolean));
    const opts = { skipDone: query.get('done') !== 'keep', whole: query.get('phases') === 'all' };
    const go = (list, o = opts) => {
      const q = new URLSearchParams();
      if (list.length) q.set('to', list.map((l) => l.a.ref).join(','));
      if (!o.skipDone) q.set('done', 'keep');
      if (o.whole) q.set('phases', 'all');
      location.hash = '#/planner' + (q.toString() ? '?' + q.toString().replace(/%2F/g, '/').replace(/%2C/g, ',') : '');
    };

    const input = h('input', { type: 'text', list: 'planner-lessons', placeholder: 'Type a lesson, for example 10/04 or attention', 'aria-label': 'Lesson to reach' });
    const addTarget = () => {
      const ref = (input.value.match(/^\s*(\d{1,2}\/\d{1,2})/) || [])[1];
      const lesson = ref ? byId.get('lesson:' + ref.split('/').map((x) => x.padStart(2, '0')).join('/')) : find(input.value, 1, ['lesson'])[0];
      if (lesson) go(uniq(targets.concat(lesson)));
    };
    input.addEventListener('change', addTarget);
    input.addEventListener('keydown', (ev) => { if (ev.key === 'Enter') addTarget(); });

    const el = h('div', { class: 'page' },
      pageHead('Plan a syllabus', 'Choose the lessons you want to reach. You get every lesson they depend on, in an order that never asks for something not yet covered.'),
      h('div', { class: 'card' },
        targets.length ? h('ul', { class: 'targets', 'aria-label': 'Lessons to reach' }, targets.map((t) => h('li', null, nodeLabel(t),
          h('button', { type: 'button', 'aria-label': `Remove ${nodeLabel(t)}`, onclick: () => go(targets.filter((x) => x !== t)) }, '×')))) : null,
        h('div', { class: 'controls', style: { 'margin-bottom': '0' } },
          input,
          h('datalist', { id: 'planner-lessons' }, all('lesson').map((l) => h('option', { value: nodeLabel(l) }))),
          h('button', { class: 'btn primary', type: 'button', onclick: addTarget }, 'Add lesson'),
          h('label', null, h('input', { type: 'checkbox', checked: opts.skipDone, onchange: (ev) => go(targets, { ...opts, skipDone: ev.target.checked }) }), 'Leave out lessons I have done'),
          h('label', null, h('input', { type: 'checkbox', checked: opts.whole, onchange: (ev) => go(targets, { ...opts, whole: ev.target.checked }) }), 'Include whole-phase prerequisites'))));

    if (!targets.length) {
      el.append(h('section', { class: 'section' }, h('h2', null, 'Try one of these'),
        h('ul', { class: 'chips' }, ['10/04', '14/01', '11/01', '07/05', '17/01'].map((r) => byId.get('lesson:' + r)).filter(Boolean)
          .map((l) => h('li', null, h('a', { href: `#/planner?to=${l.a.ref}` }, nodeLabel(l)))))));
      return { el, title: 'Plan a syllabus', nav: 'planner' };
    }

    const plan = planFor(targets, opts.whole);
    const skipped = opts.skipDone ? plan.order.filter(isDone) : [];
    const order = plan.order.filter((l) => !skipped.includes(l));
    const minutes = order.reduce((sum, l) => sum + (l.a.time_min || 0), 0);
    const items = [];
    let phaseNum;
    for (const l of order) {
      if (l.a.phase !== phaseNum) {
        phaseNum = l.a.phase;
        items.push(h('li', { class: 'group', style: { '--line': lineVar(phaseNum) } }, nodeLabel(phaseOf(l))));
      }
      items.push(stop(l, targets.includes(l) ? { tag: 'Goal', tagClass: 'target' } : {}));
    }
    const asMarkdown = () => `# Syllabus: ${targets.map(nodeLabel).join(', ')}\n\n${plural(order.length, 'lesson')}, ${fmtMin(minutes)}\n\n` +
      order.map((l, i) => `${i + 1}. ${l.a.ref} ${l.a.title}${l.a.time_min ? ` (${fmtMin(l.a.time_min)})` : ''}`).join('\n') + '\n';
    const cell = (v) => `"${String(v == null ? '' : v).replace(/"/g, '""')}"`;
    const asCsv = () => 'order,ref,title,phase,type,minutes,goal\n' + order.map((l, i) =>
      [i + 1, l.a.ref, l.a.title, phaseOf(l).a.title, l.a.lesson_type || '', l.a.time_min || '', targets.includes(l) ? 'yes' : ''].map(cell).join(',')).join('\n') + '\n';

    el.append(
      h('p', { class: 'plan-summary' }, h('b', null, plural(order.length, 'lesson')), ', ', h('b', null, fmtMin(minutes) || '0 min'), ' of lesson time, across ',
        plural(uniq(order.map((l) => l.a.phase)).length, 'phase'), '.',
        skipped.length ? ` ${plural(skipped.length, 'lesson')} you have done ${skipped.length === 1 ? 'is' : 'are'} left out.` : ''),
      h('div', { class: 'btn-row' },
        h('button', { class: 'btn', type: 'button', onclick: (ev) => copyText(asMarkdown(), ev.currentTarget) }, 'Copy as Markdown'),
        h('button', { class: 'btn', type: 'button', onclick: () => download('syllabus.csv', asCsv(), 'text/csv') }, 'Download CSV')),
      plan.assumed.length ? h('p', { class: 'muted', style: { 'max-width': '70ch' } }, 'Some lessons also assume a whole phase, which is not expanded here: ',
        plan.assumed.map((ph, i) => [i ? ', ' : '', h('a', { href: nodeHref(ph) }, nodeLabel(ph))]), '.') : null,
      h('ol', { class: 'line-list', style: { 'margin-top': '10px' } }, items));
    return { el, title: 'Plan a syllabus', nav: 'planner' };
  }

  // ---- graph explorer ----------------------------------------------------------

  const expanded = new Set(); // "nodeId|group label" pairs shown in full

  function viewGraph(id) {
    const center = byId.get(id || '') || byId.get('concept:attention') || all('phase')[0];
    const groups = neighbourGroups(center);
    const LIMIT = 8, ROW = 25, HEAD = 26, GAP = 16, W = 1120, CX = W / 2, BOX_W = 250, BOX_H = 58;

    const sides = { in: [], out: [] };
    for (const g of groups) {
      const key = center.id + '|' + g.label;
      const open = expanded.has(key);
      const shown = open ? g.nodes : g.nodes.slice(0, LIMIT);
      sides[g.dir].push({ g, key, shown, hidden: g.nodes.length - shown.length });
    }
    const sideHeight = (list) => list.reduce((sum, x) => sum + HEAD + (x.shown.length + (x.hidden ? 1 : 0)) * ROW + GAP, 0);
    const H = Math.max(sideHeight(sides.in), sideHeight(sides.out), 200) + 40;
    const cy = H / 2;
    const svg = s('svg', { class: 'nbr', viewBox: `0 0 ${W} ${H}`, role: 'group', 'aria-label': `Neighbourhood of ${nodeLabel(center)}` });
    const links = s('g'), labels = s('g');
    svg.append(links, labels);

    for (const dir of ['in', 'out']) {
      const left = dir === 'in';
      const xDot = left ? CX - 270 : CX + 270;
      const xText = left ? xDot - 12 : xDot + 12;
      const anchor = left ? 'end' : 'start';
      const xFrom = left ? CX - BOX_W / 2 : CX + BOX_W / 2;
      let y = (H - sideHeight(sides[dir])) / 2 + 14;
      for (const item of sides[dir]) {
        labels.append(s('text', { class: 'grp', x: xText, y: y + 4, 'text-anchor': anchor }, `${item.g.label} (${item.g.nodes.length})`));
        y += HEAD;
        const row = (yy) => links.append(s('path', { class: 'link', d: `M${xFrom},${cy} C${xFrom + (left ? -90 : 90)},${cy} ${xDot + (left ? 90 : -90)},${yy} ${xDot},${yy}` }));
        for (const n of item.shown) {
          row(y);
          labels.append(s('a', { href: graphHref(n), 'aria-label': `${TYPE_NAME[n.type]}: ${nodeLabel(n)}. Center the graph here.` },
            s('title', null, nodeLabel(n)),
            s('circle', { cx: xDot, cy: y, r: 5.5, fill: TYPE_COLOR[n.type] || 'var(--ink-3)' }),
            s('text', { class: 'lbl', x: xText, y: y + 4.5, 'text-anchor': anchor }, trunc(nodeLabel(n), 36))));
          y += ROW;
        }
        if (item.hidden) {
          row(y);
          labels.append(s('a', { class: 'more', tabindex: 0, role: 'button', onclick: () => { expanded.add(item.key); render(); }, onkeydown: (ev) => { if (ev.key === 'Enter') { expanded.add(item.key); render(); } } },
            s('circle', { cx: xDot, cy: y, r: 4, fill: 'none', stroke: 'var(--accent)', 'stroke-width': 2 }),
            s('text', { class: 'lbl', x: xText, y: y + 4.5, 'text-anchor': anchor }, `Show ${item.hidden} more`)));
          y += ROW;
        }
        y += GAP;
      }
    }
    svg.append(s('a', { href: nodeHref(center), 'aria-label': `Open the page for ${nodeLabel(center)}` },
      s('rect', { class: 'center-box', x: CX - BOX_W / 2, y: cy - BOX_H / 2, width: BOX_W, height: BOX_H, rx: 29 }),
      s('text', { class: 'center-kind', x: CX, y: cy - 7 }, TYPE_NAME[center.type] || center.type),
      s('text', { class: 'center-lbl', x: CX, y: cy + 13 }, trunc(nodeLabel(center), 28))));

    const pickBox = h('ul', { class: 'chips', style: { 'margin-top': '8px' } });
    const pick = h('input', { type: 'search', placeholder: 'Center the graph on a lesson, concept, paper or library', 'aria-label': 'Center the graph on', oninput: (ev) => {
      pickBox.replaceChildren(...find(ev.target.value, 10).map((n) => h('li', null, h('a', { href: graphHref(n) }, `${TYPE_NAME[n.type]}: ${trunc(nodeLabel(n), 50)}`))));
    } });
    const types = uniq(groups.flatMap((g) => g.nodes.map((n) => n.type)));
    const el = h('div', { class: 'page' },
      pageHead('Explore the graph', 'One node and everything connected to it. On the left, what points to it; on the right, what it points to. Select a neighbour to move there, or the centre to open its page.'),
      h('div', { class: 'controls' }, pick), pickBox,
      h('div', { class: 'card graph-card', style: { 'margin-top': '14px' } }, svg),
      h('ul', { class: 'type-legend', 'aria-label': 'Node types' }, types.map((t) => h('li', null, h('i', { style: { '--c': TYPE_COLOR[t] || 'var(--ink-3)' } }), TYPE_NAME[t] || t))),
      !groups.length ? h('p', { class: 'muted' }, 'This node has no connections.') : null);
    return { el, title: 'Graph: ' + nodeLabel(center), nav: 'graph' };
  }

  // ---- reference lists ---------------------------------------------------------

  function viewResources() {
    const cited = (r) => inn(r, 'CITES').length;
    const items = [...all('resource')].sort((a, b) => cited(b) - cited(a) || a.label.localeCompare(b.label));
    const KIND = { arxiv: 'arXiv paper', doi: 'Paper (DOI)', web: 'Web page' };
    return { title: 'Papers and links', nav: 'resources', el: listView({
      title: 'Papers and links',
      lede: 'Everything the lessons and the glossary cite, most cited first. Use it as the reading list behind the curriculum.',
      items, noun: 'reference', placeholder: 'Filter by title or site',
      text: (r) => `${r.label} ${r.a.host || ''}`,
      selects: [{ label: 'Kind', options: [['', 'All kinds']].concat(Object.entries(KIND)), test: (r, v) => r.a.kind === v }],
      row: (r) => h('li', null,
        h('a', { class: 'title', href: nodeHref(r) }, trunc(r.label, 120)),
        h('span', { class: 'side' }, KIND[r.a.kind] || r.a.kind || '', h('span', null, `cited ${cited(r)}×`)),
        h('p', { class: 'desc' }, h('a', { href: r.a.url, target: '_blank', rel: 'noopener' }, trunc(String(r.a.url || '').replace(/^https?:\/\//, ''), 80)))),
    }) };
  }

  function viewArtifacts() {
    const kinds = uniq(all('artifact').map((a) => a.a.kind).filter(Boolean)).sort();
    return { title: 'Prompts and skills', nav: 'artifacts', el: listView({
      title: 'Prompts and skills',
      lede: 'Reusable material the lessons ship: prompts, agent skills and agent definitions. Open the lesson to read and copy the full text.',
      items: [...all('artifact')].sort((a, b) => a.label.localeCompare(b.label)), noun: 'item', placeholder: 'Filter by name or description',
      text: (a) => `${a.label} ${a.a.description || ''} ${(a.a.tags || []).join(' ')}`,
      selects: [{ label: 'Kind', options: [['', 'All kinds']].concat(kinds.map((k) => [k, k[0].toUpperCase() + k.slice(1)])), test: (a, v) => a.a.kind === v }],
      row: (a) => {
        const lesson = (inn(a, 'SHIPS')[0] || {}).s;
        return h('li', null,
          h('a', { class: 'title', href: lesson ? nodeHref(lesson) : nodeHref(a) }, a.label),
          h('span', { class: 'side' }, a.a.kind ? h('span', { class: 'tag' }, a.a.kind) : null, lesson ? `lesson ${lesson.a.ref}` : ''),
          h('p', { class: 'desc' }, a.a.description || ''));
      },
    }) };
  }

  function viewLibraries() {
    const used = (lib) => inn(lib, 'USES').length;
    return { title: 'Libraries', nav: 'libraries', el: listView({
      title: 'Libraries',
      lede: 'Third-party libraries the lesson code imports. Most lessons use only the standard library; these are the exceptions.',
      items: [...all('library')].sort((a, b) => used(b) - used(a) || a.label.localeCompare(b.label)), noun: 'library', placeholder: 'Filter libraries',
      text: (lib) => lib.label,
      row: (lib) => h('li', null,
        h('a', { class: 'title', href: nodeHref(lib) }, lib.a.name),
        h('span', { class: 'side' }, lib.a.language, h('span', null, `used in ${plural(used(lib), 'lesson')}`))),
    }) };
  }

  function viewTopics() {
    return { title: 'Topics', nav: 'topics', el: listView({
      title: 'Topics',
      lede: 'Groups of lessons and concepts that belong together, found automatically from shared concepts and prerequisites. They cut across phases, so they show which lessons talk about the same thing.',
      items: [...all('community')].sort((a, b) => (b.a.size || 0) - (a.a.size || 0)), noun: 'topic', placeholder: 'Filter topics',
      text: (c) => nodeLabel(c),
      row: (c) => h('li', null,
        h('a', { class: 'title', href: nodeHref(c) }, nodeLabel(c)),
        h('span', { class: 'side' }, `${plural(c.a.lessons || 0, 'lesson')}, ${plural(c.a.concepts || 0, 'concept')}`),
        c.a.main_phase != null && byId.get('phase:' + c.a.main_phase) ? h('p', { class: 'desc' }, 'Mostly in ', h('a', { href: `#/phase/${c.a.main_phase}` }, nodeLabel(byId.get('phase:' + c.a.main_phase)))) : null),
    }) };
  }

  function viewMyths() {
    const el = h('div', { class: 'page page-narrow' },
      pageHead('Myths', 'Things people say about AI that do not hold up, what is true instead, and why the difference matters when you build with it.'),
      all('myth').map((m) => h('article', { class: 'myth' },
        h('h2', null, m.a.claim),
        m.a.reality ? h('p', null, h('b', null, 'What is true'), m.a.reality) : null,
        m.a.why_it_matters ? h('p', null, h('b', null, 'Why it matters'), m.a.why_it_matters) : null)));
    return { el, title: 'Myths', nav: 'myths' };
  }

  // ---- generic node page -----------------------------------------------------

  function viewNode(id) {
    const n = byId.get(id);
    if (!n) return notFound();
    if (['lesson', 'phase', 'concept', 'learning_path'].includes(n.type)) { location.replace(nodeHref(n)); return null; }
    const NAV = { resource: 'resources', artifact: 'artifacts', library: 'libraries', community: 'topics', myth: 'myths' };
    const facts = [];
    let lede = null, action = null;
    if (n.type === 'resource') {
      facts.push(n.a.host, { arxiv: 'arXiv paper', doi: 'Paper (DOI)', web: 'Web page' }[n.a.kind]);
      action = h('a', { class: 'btn primary', href: n.a.url, target: '_blank', rel: 'noopener' }, 'Open the source');
    } else if (n.type === 'artifact') {
      lede = n.a.description;
      facts.push(n.a.kind, ...(n.a.tags || []));
    } else if (n.type === 'library') {
      facts.push(n.a.language);
    } else if (n.type === 'community') {
      lede = 'A group of lessons and concepts that belong together, found automatically from shared concepts and prerequisites.';
      facts.push(plural(n.a.lessons || 0, 'lesson'), plural(n.a.concepts || 0, 'concept'));
    } else if (n.type === 'track') {
      lede = n.a.note;
      facts.push(`Lessons ${n.a.start} to ${n.a.end}`);
    } else if (n.type === 'myth') {
      lede = n.a.reality;
    }
    const el = h('div', { class: 'page' },
      h('header', { class: 'page-head' },
        h('span', { class: 'kicker' }, TYPE_NAME[n.type] || n.type),
        h('h1', null, nodeLabel(n)),
        lede ? h('p', { class: 'lede' }, lede) : null,
        facts.filter(Boolean).length ? h('ul', { class: 'facts' }, facts.filter(Boolean).map((f) => h('li', null, f))) : null,
        action ? h('div', { class: 'btn-row', style: { 'margin-top': '18px' } }, action) : null),
      relatedSections(n),
      h('p', { class: 'section small' }, h('a', { href: graphHref(n) }, 'See this in the graph')));
    return { el, title: nodeLabel(n), nav: NAV[n.type] || null };
  }

  // ---- progress -----------------------------------------------------------------

  function viewProgress() {
    const lessons = all('lesson');
    const done = lessons.filter(isDone);
    const minutes = done.reduce((sum, l) => sum + (l.a.time_min || 0), 0);
    const fileInput = h('input', { type: 'file', accept: 'application/json,.json', hidden: true, onchange: (ev) => {
      const file = ev.target.files[0];
      if (!file) return;
      file.text().then((text) => {
        const data = JSON.parse(text);
        const incoming = data && data.lessons;
        if (!incoming || typeof incoming !== 'object') throw new Error('no lessons');
        for (const ref in incoming) if (byId.has('lesson:' + ref)) progress[ref] = String(incoming[ref]).slice(0, 10);
        store.set(PROGRESS_KEY, progress);
        updateProgressCount();
        render();
      }).catch(() => { status.textContent = 'That file is not a progress export from this site. Choose a file saved with "Save my progress".'; });
    } });
    const status = h('p', { class: 'muted', role: 'status' });
    const el = h('div', { class: 'page page-narrow' },
      pageHead('My progress', 'Lessons you marked as done. This is kept in this browser only: nothing is sent anywhere. Save it to a file to move it to another computer or to share it with whoever runs your course.'),
      h('ul', { class: 'totals' },
        h('li', null, h('b', null, done.length), `of ${lessons.length} lessons`),
        h('li', null, h('b', null, fmtMin(minutes) || '0 min'), 'of lesson time'),
        h('li', null, h('b', null, all('phase').filter((p) => doneCount(lessonsOf(p))).length), 'phases started')),
      h('div', { class: 'btn-row' },
        h('button', { class: 'btn', type: 'button', onclick: () => download('ai-knowledge-base-progress.json',
          JSON.stringify({ exported_at: new Date().toISOString(), lessons: progress }, null, 2), 'application/json') }, 'Save my progress'),
        h('button', { class: 'btn', type: 'button', onclick: () => fileInput.click() }, 'Load a saved file'),
        done.length ? h('button', { class: 'btn quiet', type: 'button', onclick: () => {
          if (window.confirm(`Clear all ${done.length} lessons marked as done? This cannot be undone unless you saved a file.`)) {
            progress = {}; store.set(PROGRESS_KEY, progress); updateProgressCount(); render();
          }
        } }, 'Clear my progress') : null,
        fileInput),
      status,
      h('section', { class: 'section' }, h('h2', null, 'By phase'),
        all('phase').map((p) => {
          const ls = lessonsOf(p), d = doneCount(ls);
          return h('div', { class: 'progress-phase', style: { '--line': lineVar(p.a.num) } },
            h('span', { class: 'roundel' + (d === ls.length && d ? ' done' : '') }, p.a.num),
            h('a', { href: nodeHref(p) }, p.a.title),
            meter(d, ls.length),
            h('span', { class: 'num' }, `${d}/${ls.length}`));
        })),
      !done.length ? h('p', { class: 'section muted' }, 'Nothing marked yet. Open a lesson and select "Mark as done" when you finish it.') : null);
    return { el, title: 'My progress', nav: 'progress' };
  }

  function notFound() {
    return { title: 'Not found', nav: null, el: h('div', { class: 'page page-narrow' },
      pageHead('This page does not exist', 'The link points to something that is not in this version of the knowledge base. It may have been renamed or removed upstream.'),
      h('div', { class: 'btn-row' }, h('a', { class: 'btn primary', href: '#/' }, 'Go to the curriculum map'))) };
  }

  // ══ 7. router ════════════════════════════════════════════════════════

  const ROUTES = [
    [/^\/?$/, viewHome],
    [/^\/phase\/(\d+)$/, viewPhase],
    [/^\/lesson\/(\d+)\/(\d+)$/, viewLesson],
    [/^\/concepts$/, viewConcepts],
    [/^\/concept\/(.+)$/, viewConcept],
    [/^\/paths$/, viewPaths],
    [/^\/path\/(.+)$/, viewPath],
    [/^\/planner$/, viewPlanner],
    [/^\/graph(?:\/(.+))?$/, viewGraph],
    [/^\/resources$/, viewResources],
    [/^\/artifacts$/, viewArtifacts],
    [/^\/libraries$/, viewLibraries],
    [/^\/topics$/, viewTopics],
    [/^\/myths$/, viewMyths],
    [/^\/progress$/, viewProgress],
    [/^\/node\/(.+)$/, viewNode],
  ];
  const main = document.getElementById('main');
  const rail = document.getElementById('rail');
  const scrim = document.getElementById('scrim');
  const menuBtn = document.getElementById('menu-btn');
  let lastPath = null;

  function render() {
    const raw = location.hash.replace(/^#/, '') || '/';
    const cut = raw.indexOf('?');
    const path = cut < 0 ? raw : raw.slice(0, cut);
    const query = new URLSearchParams(cut < 0 ? '' : raw.slice(cut + 1));
    let view = null;
    for (const [pattern, fn] of ROUTES) {
      const m = path.match(pattern);
      if (m) {
        let args;
        try { args = m.slice(1).map((x) => (x == null ? x : decodeURIComponent(x))); } catch (e) { break; }
        view = fn === viewPlanner ? fn(query) : fn(...args);
        if (view === null) return; // the view redirected
        break;
      }
    }
    view = view || notFound();
    main.replaceChildren(view.el);
    document.title = view.title ? `${view.title} · ${D.title}` : D.title;
    rail.querySelectorAll('a').forEach((a) => {
      if (a.dataset.nav === view.nav) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current');
    });
    closeMenu();
    if (path !== lastPath) window.scrollTo(0, 0);
    lastPath = path;
  }

  function closeMenu() { rail.classList.remove('open'); scrim.hidden = true; menuBtn.setAttribute('aria-expanded', 'false'); }
  menuBtn.addEventListener('click', () => {
    const open = !rail.classList.contains('open');
    rail.classList.toggle('open', open);
    scrim.hidden = !open;
    menuBtn.setAttribute('aria-expanded', String(open));
  });
  scrim.addEventListener('click', closeMenu);
  document.getElementById('skip-link').addEventListener('click', (ev) => { ev.preventDefault(); main.focus(); });
  document.getElementById('theme-btn').addEventListener('click', () => {
    store.set('kg-theme', isDark() ? 'light' : 'dark');
    applyTheme();
    render(); // diagrams pick their colours when they are drawn
  });
  darkQuery.addEventListener('change', () => { applyTheme(); render(); });

  document.getElementById('brand-title').textContent = D.title;
  document.getElementById('rail-foot').textContent =
    `Curriculum: AI Engineering from Scratch by Rohit Ghumare, MIT licence${D.meta.upstream_commit ? ', version ' + D.meta.upstream_commit : ''}. Everything runs on your machine.`;
  applyTheme();
  updateProgressCount();
  initSearch();
  window.addEventListener('hashchange', render);
  render();
})();
