"""Project ``graph.json`` and the lesson texts into a static HTML site.

Why a second exporter
---------------------
The Obsidian vault needs Obsidian. The site needs a browser and nothing else:
no server, no install, no network. It opens from a ``file://`` URL, so it can
be unzipped from a shared drive or handed over as one self-contained file.

That single constraint drives every technical decision here:

* **No ``fetch``.** Browsers block it on ``file://``. Data is shipped as
  JavaScript files that assign to a global; lesson texts are loaded on demand
  by adding a ``<script>`` tag (the JSONP trick).
* **No CDN.** Mermaid and the interface font are vendored in ``vendor/``.
* **No ES modules.** They are also blocked on ``file://``. One classic script.
* **Markdown is rendered at build time**, in Python, where it can be tested;
  the browser only receives escaped HTML.

Modules
-------
render_md.py  markdown -> safe HTML (headings, lists, tables, code, mermaid, figures)
data.py       graph.json -> the compact payload the page loads at start-up
lessons.py    one lesson folder -> its on-demand payload (text, code, quiz, artifacts)
export.py     the orchestrator: writes the folder site and the single-file build
assets/       the page itself: index.html template, app.css, app.js
vendor/       third-party files bundled into every export
"""
