/* ==========================================================================
   Campus Placement — "Admissions Ledger" design system
   Ink navy + warm paper + emerald approval-stamp accent.
   Display: Fraunces (serif, ink-trap character) · Body: Inter · Mono: IBM Plex Mono
   ========================================================================== */

:root {
  --ink: #16213A;
  --ink-soft: #2C3A5C;
  --paper: #F3F4EF;
  --paper-raised: #FFFFFF;
  --paper-line: #DEDCCB;
  --accent: #1F7A5C;       /* approval-stamp emerald */
  --accent-dark: #155A43;
  --accent-soft: #E4F0EA;
  --warn: #B23A2E;         /* rejection-stamp red */
  --warn-soft: #F6E4E1;
  --gold: #B68A2E;         /* TPO / official accent, used sparingly */
  --gold-soft: #F2EAD3;
  --text: #1B2330;
  --text-muted: #5B6473;
  --radius: 6px;
  --shadow: 0 1px 2px rgba(22, 33, 58, 0.06);
  --font-display: 'Fraunces', 'Iowan Old Style', 'Georgia', serif;
  --font-body: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'IBM Plex Mono', 'SFMono-Regular', Consolas, monospace;
}

* { box-sizing: border-box; }

html, body {
  margin: 0;
  background: var(--paper);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 15.5px;
  line-height: 1.55;
}

h1, h2, h3, h4 {
  font-family: var(--font-display);
  color: var(--ink);
  font-weight: 600;
  letter-spacing: -0.01em;
  margin: 0 0 0.5em;
}

h1 { font-size: 2rem; }
h2 { font-size: 1.5rem; }
h3 { font-size: 1.2rem; }

a { color: var(--accent-dark); text-decoration: none; }
a:hover { text-decoration: underline; }

.eyebrow {
  font-family: var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.72rem;
  color: var(--text-muted);
  margin-bottom: 0.4em;
  display: block;
}

/* ---------- Layout ---------- */
.shell { min-height: 100vh; display: flex; flex-direction: column; }

.letterhead {
  background: var(--ink);
  color: var(--paper);
  padding: 0 1.5rem;
}
.letterhead-inner {
  max-width: 1080px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
}
.brand {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  font-family: var(--font-display);
  font-size: 1.15rem;
  color: var(--paper);
  font-weight: 600;
}
.brand-mark {
  width: 34px; height: 34px;
  border: 1.5px solid var(--paper);
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  letter-spacing: 0.02em;
}
.nav-links { display: flex; align-items: center; gap: 1.4rem; }
.nav-links a { color: var(--paper); opacity: 0.85; font-size: 0.92rem; }
.nav-links a:hover { opacity: 1; text-decoration: none; border-bottom: 1px solid var(--gold); }
.role-chip {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.25em 0.6em;
  border: 1px solid var(--gold);
  color: var(--gold);
  border-radius: 3px;
}

.container {
  max-width: 1080px;
  margin: 0 auto;
  padding: 2.2rem 1.5rem 4rem;
  width: 100%;
  flex: 1;
}

.container-narrow { max-width: 680px; }

footer.ledger-footer {
  border-top: 1px solid var(--paper-line);
  padding: 1.2rem 1.5rem;
  text-align: center;
  font-size: 0.82rem;
  color: var(--text-muted);
  font-family: var(--font-mono);
}

/* ---------- Cards ---------- */
.card {
  background: var(--paper-raised);
  border: 1px solid var(--paper-line);
  border-radius: var(--radius);
  padding: 1.4rem 1.6rem;
  box-shadow: var(--shadow);
  margin-bottom: 1.4rem;
}
.card-flush { padding: 0; overflow: hidden; }
.card-header-row {
  display: flex; align-items: baseline; justify-content: space-between;
  margin-bottom: 1rem;
}

.grid { display: grid; gap: 1.2rem; }
.grid-2 { grid-template-columns: repeat(2, 1fr); }
.grid-3 { grid-template-columns: repeat(3, 1fr); }
@media (max-width: 720px) {
  .grid-2, .grid-3 { grid-template-columns: 1fr; }
}

/* ---------- Stat tiles ---------- */
.stat-tile {
  border: 1px solid var(--paper-line);
  border-radius: var(--radius);
  background: var(--paper-raised);
  padding: 1.1rem 1.3rem;
}
.stat-tile .num {
  font-family: var(--font-mono);
  font-size: 1.9rem;
  color: var(--ink);
  font-weight: 600;
  display: block;
}
.stat-tile .label {
  font-size: 0.82rem;
  color: var(--text-muted);
}

/* ---------- Buttons ---------- */
.btn {
  display: inline-block;
  font-family: var(--font-body);
  font-weight: 600;
  font-size: 0.9rem;
  padding: 0.55em 1.2em;
  border-radius: var(--radius);
  border: 1.5px solid var(--ink);
  background: var(--ink);
  color: var(--paper) !important;
  cursor: pointer;
  text-decoration: none !important;
  transition: opacity 0.15s ease;
}
.btn:hover { opacity: 0.85; }
.btn-outline {
  background: transparent;
  color: var(--ink) !important;
  border: 1.5px solid var(--ink);
}
.btn-accent {
  background: var(--accent);
  border-color: var(--accent);
}
.btn-warn {
  background: var(--warn);
  border-color: var(--warn);
}
.btn-sm { padding: 0.35em 0.85em; font-size: 0.8rem; }
.btn-block { display: block; width: 100%; text-align: center; }

/* ---------- Forms ---------- */
label { font-weight: 600; font-size: 0.86rem; display: block; margin-bottom: 0.3em; color: var(--ink-soft); }
input[type=text], input[type=email], input[type=password], input[type=number],
input[type=date], input[type=file], textarea, select {
  width: 100%;
  font-family: var(--font-body);
  font-size: 0.95rem;
  padding: 0.55em 0.7em;
  border: 1px solid var(--paper-line);
  border-radius: var(--radius);
  background: var(--paper-raised);
  color: var(--text);
  margin-bottom: 0.2em;
}
select[multiple] { padding: 0.4em; }
textarea { resize: vertical; }
.field { margin-bottom: 1.1rem; }
.help-text { font-size: 0.78rem; color: var(--text-muted); margin-top: 0.2em; }
.errorlist { list-style: none; padding: 0; margin: 0.2em 0; color: var(--warn); font-size: 0.82rem; }
fieldset { border: none; padding: 0; margin: 0 0 1.2rem; }
.radio-option { display: flex; gap: 0.5em; align-items: baseline; padding: 0.35em 0; border-bottom: 1px dotted var(--paper-line); }
.radio-option input { width: auto; margin: 0; }

/* ---------- Tables ---------- */
table.ledger { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
table.ledger th {
  text-align: left;
  font-family: var(--font-mono);
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 0.06em;
  color: var(--text-muted);
  border-bottom: 1.5px solid var(--ink);
  padding: 0.6em 0.8em;
}
table.ledger td {
  padding: 0.65em 0.8em;
  border-bottom: 1px solid var(--paper-line);
  vertical-align: middle;
}
table.ledger tr:hover td { background: var(--paper); }

/* ---------- Stamp badges ---------- */
.stamp {
  display: inline-block;
  font-family: var(--font-mono);
  text-transform: uppercase;
  font-size: 0.68rem;
  letter-spacing: 0.08em;
  padding: 0.3em 0.7em;
  border: 1.5px solid currentColor;
  border-radius: 3px;
  transform: rotate(-1.5deg);
}
.stamp-selected { color: var(--accent-dark); background: var(--accent-soft); }
.stamp-rejected { color: var(--warn); background: var(--warn-soft); }
.stamp-pending  { color: var(--gold); background: var(--gold-soft); }

.chip {
  display: inline-block;
  font-size: 0.78rem;
  padding: 0.22em 0.65em;
  border: 1px solid var(--paper-line);
  border-radius: 20px;
  margin: 0.12em 0.2em 0.12em 0;
  background: var(--paper);
  color: var(--ink-soft);
}

.match-badge {
  width: 56px; height: 56px;
  border-radius: 50%;
  border: 2px solid var(--accent);
  color: var(--accent-dark);
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  font-family: var(--font-mono);
  font-weight: 600;
  flex-shrink: 0;
}
.match-badge .pct { font-size: 1.05rem; line-height: 1; }
.match-badge .pct-label { font-size: 0.5rem; text-transform: uppercase; letter-spacing: 0.04em; }

/* ---------- Alerts / messages ---------- */
.alert {
  padding: 0.85em 1.1em;
  border-radius: var(--radius);
  margin-bottom: 1.1rem;
  font-size: 0.9rem;
  border: 1px solid transparent;
}
.alert-success { background: var(--accent-soft); color: var(--accent-dark); border-color: var(--accent); }
.alert-danger  { background: var(--warn-soft); color: var(--warn); border-color: var(--warn); }
.alert-warning { background: var(--gold-soft); color: var(--gold); border-color: var(--gold); }
.alert-info    { background: #E5EAF1; color: var(--ink-soft); border-color: var(--ink-soft); }

.empty-state {
  text-align: center;
  padding: 2.5rem 1rem;
  color: var(--text-muted);
}
.empty-state h3 { color: var(--ink-soft); }

.muted { color: var(--text-muted); }
.text-mono { font-family: var(--font-mono); }
.divider { border: none; border-top: 1px solid var(--paper-line); margin: 1.4rem 0; }

/* ---------- Landing hero ---------- */
.hero {
  background: var(--ink);
  color: var(--paper);
  padding: 4rem 1.5rem 3.5rem;
}
.hero-inner { max-width: 1080px; margin: 0 auto; }
.hero h1 { color: var(--paper); font-size: 2.6rem; max-width: 30ch; }
.hero p.lede { max-width: 48ch; color: #C9CFDC; font-size: 1.05rem; }
.hero-actions { display: flex; gap: 0.8rem; margin-top: 1.6rem; flex-wrap: wrap; }
.hero-stats { display: flex; gap: 2.2rem; margin-top: 2.6rem; flex-wrap: wrap; }
.hero-stats .num { font-family: var(--font-mono); font-size: 1.7rem; color: var(--gold); }
.hero-stats .label { font-size: 0.78rem; color: #B9C0CF; text-transform: uppercase; letter-spacing: 0.06em; }

.role-cards { padding: 3rem 1.5rem; max-width: 1080px; margin: 0 auto; }
.role-card {
  border: 1px solid var(--paper-line);
  border-radius: var(--radius);
  background: var(--paper-raised);
  padding: 1.6rem;
}
.role-card .eyebrow { color: var(--accent-dark); }
