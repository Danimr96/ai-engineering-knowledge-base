# Third-party files bundled into the HTML site

The site must work offline and from a `file://` URL, so nothing is loaded
from a CDN. These files are copied into every export.

| File | What | Version | Licence |
|---|---|---|---|
| `mermaid.min.js` | Mermaid, renders the lessons' diagrams | 11.4.1 | MIT, © Knut Sveidqvist |
| `overpass-latin.woff2` | Overpass variable font (latin subset), interface typeface | v19 | SIL Open Font License 1.1, © Red Hat / Delve Fonts |

The interactive lesson figures (`lesson-figures.js`, `figures-*.js`) are not
stored here: the exporter copies them from the curriculum's own `site/`
folder (MIT, same licence as the lessons).
