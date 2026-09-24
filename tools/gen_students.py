# Generates students hub pages. Run: python tools/gen_students.py
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "students"

TOOLS = [
    ("index.html", "Hub", "Student tools", True),
    ("playbook.html", "Playbook", "Internship playbook"),
    ("templates.html", "Templates", "CV & cover letter"),
    ("court-checklist.html", "Court checklist", "Court observation checklist"),
    ("cheat-sheet.html", "Cheat sheet", "Citation & drafting"),
    ("resources.html", "Resources", "Resource library"),
    ("reading-lists.html", "Reading lists", "Subject reading lists"),
    ("openings.html", "Openings", "Internship openings"),
    ("ask.html", "Ask a senior", "Ask a senior"),
    ("calendar.html", "Calendar", "Campus & career calendar"),
    ("peer-groups.html", "Peer groups", "Peer study groups"),
    ("portfolio-tips.html", "Portfolio tips", "Portfolio & LinkedIn tips"),
    ("digest.html", "Digest", "Law desk digest"),
]


def tool_nav(current: str) -> str:
    bits = []
    for file, label, _title, *rest in [(t[0], t[1], t[2]) for t in TOOLS]:
        cur = ' aria-current="page"' if file == current else ""
        href = file if file != "index.html" else "./"
        if file == "index.html":
            href = "./"
        bits.append(f'<a href="{href}"{cur}>{label}</a>')
    return '<nav class="tool-nav" aria-label="Student tools">\n' + "\n".join(bits) + "\n</nav>"


def chrome(title: str, description: str, current: str, crumb_label: str, body: str, extra_head: str = "") -> str:
    canon = f"https://rushabh023.github.io/drashti-baser-portfolio/students/{'' if current == 'index.html' else current}"
    nav = tool_nav(current)
    crumb_hub = '<li><a href="./">Students</a></li>'
    crumb_page = "" if current == "index.html" else f"<li><span>{crumb_label}</span></li>"
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title} | Drashti Baser — For students</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canon}">
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Manrope:wght@400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/css/styles.css">
  <link rel="stylesheet" href="../assets/css/students.css">
  {extra_head}
</head>
<body class="students-page">
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header">
    <div class="wrap header-bar">
      <a class="brand" href="../index.html">
        <svg width="28" height="28" viewBox="0 0 32 32" aria-hidden="true" focusable="false">
          <circle cx="16" cy="16" r="16" fill="#0A0A0B"/>
          <text x="16" y="21" text-anchor="middle" fill="#FFFFFF" font-size="11" font-family="Archivo, Arial, sans-serif" font-weight="700">DB</text>
        </svg>
        Drashti Baser
      </a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <ul class="nav">
        <li><a href="../index.html">Portfolio</a></li>
        <li><a href="./" aria-current="true">Students</a></li>
        <li><a href="../index.html#contact">Contact</a></li>
      </ul>
      <a class="btn header-cta" href="../index.html#contact">Get in touch</a>
    </div>
  </header>
  <div id="menu" class="menu" hidden>
    <button class="menu-close" type="button">Close</button>
    <a href="../index.html">Portfolio</a>
    <a href="./">Students hub</a>
    <a href="playbook.html">Playbook</a>
    <a href="templates.html">Templates</a>
    <a href="openings.html">Openings</a>
    <a href="ask.html">Ask a senior</a>
    <a href="digest.html">Digest</a>
    <a href="../index.html#contact">Contact</a>
  </div>

  <main id="content" tabindex="-1">
    <div class="hero-mini">
      <div class="wrap">
        <ul class="crumb">
          <li><a href="../index.html">Portfolio</a></li>
          {crumb_hub}
          {crumb_page}
        </ul>
        {nav}
      </div>
    </div>
{body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <div>
        <a class="footer-brand" href="../index.html">Drashti Baser</a>
        <p class="mt-md">Student tools shared for classmates and juniors. Not legal advice. Public resources only.</p>
        <p>© 2026 Drashti Baser</p>
      </div>
      <ul class="footer-nav">
        <li><a href="./">Students hub</a></li>
        <li><a href="../index.html">Portfolio</a></li>
        <li><a href="../index.html#contact">Contact</a></li>
        <li><a href="../assets/docs/Drashti-Baser-CV.pdf" download>CV</a></li>
      </ul>
    </div>
  </footer>
  <script src="../assets/js/students.js"></script>
</body>
</html>
"""


PAGES = {}

PAGES["index.html"] = (
    "Student tools for law classmates",
    "Playbooks, checklists, templates, openings, and live law-student headlines — shared by Drashti Baser for fellow BA LLB students.",
    "Hub",
    """
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <div>
            <p class="label">For students</p>
            <h1>Tools for classmates and juniors</h1>
          </div>
          <p class="lede">Built so fellow law students can prepare for internships, court observation, and a clean portfolio — without paying for gated advice.</p>
        </div>
        <div class="tool-grid reveal">
          <a class="tool-card" href="playbook.html"><span class="index">01</span><h3>Internship playbook</h3><p>How to approach chambers, what to ask in District Court, and how to write a cold email.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="templates.html"><span class="index">02</span><h3>CV &amp; cover letter</h3><p>Printable law-intern templates with fill-in structure.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="court-checklist.html"><span class="index">03</span><h3>Court checklist</h3><p>What to note in civil and criminal hearings.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="cheat-sheet.html"><span class="index">04</span><h3>Citation &amp; drafting</h3><p>Quick habits for case briefs and common drafts.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="resources.html"><span class="index">05</span><h3>Resource library</h3><p>Curated free research desks by subject.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="reading-lists.html"><span class="index">06</span><h3>Reading lists</h3><p>First cases and Acts for Criminal, Civil, and Constitutional Law.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="openings.html"><span class="index">07</span><h3>Internship openings</h3><p>Curated public calls plus a way to suggest an opening.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="ask.html"><span class="index">08</span><h3>Ask a senior</h3><p>Send a short question about internships, legal aid, or portfolios.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="calendar.html"><span class="index">09</span><h3>Campus calendar</h3><p>Moots, AIBE orientation, and student-relevant dates.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="peer-groups.html"><span class="index">10</span><h3>Peer groups</h3><p>Opt-in circles for research, moots, and legal aid.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="portfolio-tips.html"><span class="index">11</span><h3>Portfolio tips</h3><p>How to describe internships safely and keep one clean page.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
          <a class="tool-card" href="digest.html"><span class="index">12</span><h3>Law desk digest</h3><p>Live headlines plus a short weekly briefing for students.</p><span class="text-link">Open <span class="btn-arrow" aria-hidden="true">→</span></span></a>
        </div>
        <div class="share-bar reveal" style="margin-top:48px">
          <div>
            <h3>Share the hub</h3>
            <p class="meta">Send this corner to your batch before internship season.</p>
          </div>
          <div class="share-actions">
            <button type="button" class="btn" id="copy-link" data-copied="Link copied">Copy link</button>
            <a class="btn btn-ghost" id="share-whatsapp" href="#" target="_blank" rel="noopener noreferrer">WhatsApp</a>
            <a class="btn btn-ghost" id="share-linkedin" href="#" target="_blank" rel="noopener noreferrer">LinkedIn</a>
          </div>
        </div>
      </div>
    </section>
""",
)

PAGES["playbook.html"] = (
    "Internship playbook for law students",
    "Practical steps for chambers outreach, District Court internships, and cold emails.",
    "Playbook",
    """
    <section class="section">
      <div class="wrap prose reveal">
        <p class="label">01 — Playbook</p>
        <h1>Internship playbook</h1>
        <p class="lede">A short path you can follow in the semester before you apply — and in the first week inside a court or chambers.</p>

        <h3>1. Before you write to anyone</h3>
        <ol>
          <li>Update one CV page: education, two strongest experiences, languages, and contact.</li>
          <li>Pick a focus for this break: litigation observation, research, or legal aid — not all three.</li>
          <li>List 8–12 targets: local chambers, District Court advocates, university cells, and one think tank.</li>
          <li>Prepare a 4-line intro: who you are, year/college, what you want to learn, and when you are free.</li>
        </ol>

        <h3>2. Cold email structure</h3>
        <ol>
          <li>Subject: Internship enquiry — BA LLB, [Month Year], [City].</li>
          <li>Line 1: name, year, university.</li>
          <li>Line 2: why this chambers/court (one specific reason).</li>
          <li>Line 3: what you can help with (research notes, filing support, hearing notes).</li>
          <li>Line 4: dates available + CV attached. Keep it under 150 words.</li>
        </ol>

        <h3>3. First week in District Court</h3>
        <ul>
          <li>Learn how the cause list is called and where filings are received.</li>
          <li>Sit through full hearings, not only “interesting” arguments.</li>
          <li>Ask permission before photographing any paper; usually take handwritten notes only.</li>
          <li>Never publish client names, case numbers tied to parties, or sensitive facts on social media.</li>
        </ul>

        <h3>4. After the internship</h3>
        <ul>
          <li>Write a thank-you note within 48 hours.</li>
          <li>Update your portfolio with role, dates, and skills — in general terms.</li>
          <li>Ask for a certificate early if the office issues them at month-end.</li>
        </ul>

        <p class="mt-xl"><a class="btn" href="templates.html">Get CV templates</a>
        <a class="text-link" href="court-checklist.html" style="margin-left:18px">Court checklist <span class="btn-arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>
""",
)

PAGES["templates.html"] = (
    "Law internship CV and cover letter templates",
    "Printable CV and cover letter templates for BA LLB internship applications.",
    "Templates",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">02 — Templates</p>
        <h1>CV &amp; cover letter</h1>
        <p class="lede">Use these as starting structures. Replace every bracketed line with your own facts. Print to PDF from the browser.</p>

        <h3>Law intern CV</h3>
        <div class="template-actions">
          <a class="btn" href="../assets/templates/cv-template.html" target="_blank" rel="noopener noreferrer">Open CV template</a>
          <a class="btn btn-ghost" href="../assets/templates/cv-template.html" target="_blank" rel="noopener noreferrer">Print / Save PDF</a>
        </div>
        <div class="template-frame">
          <iframe title="CV template preview" src="../assets/templates/cv-template.html" loading="lazy"></iframe>
        </div>

        <h3 class="mt-xl">Cover letter</h3>
        <div class="template-actions">
          <a class="btn" href="../assets/templates/cover-letter.html" target="_blank" rel="noopener noreferrer">Open cover letter</a>
          <a class="btn btn-ghost" href="../assets/templates/cover-letter.html" target="_blank" rel="noopener noreferrer">Print / Save PDF</a>
        </div>
        <div class="template-frame">
          <iframe title="Cover letter template preview" src="../assets/templates/cover-letter.html" loading="lazy"></iframe>
        </div>

        <p class="meta mt-lg">Tip: keep the CV to one page for student internships unless a chambers asks for more.</p>
      </div>
    </section>
""",
)

PAGES["court-checklist.html"] = (
    "Court observation checklist for law students",
    "Interactive checklist for civil and criminal hearing notes in District Court.",
    "Court checklist",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">03 — Court checklist</p>
        <h1>Court observation checklist</h1>
        <p class="lede">Tick items as you learn them. Progress saves on this device. Print the page if you prefer paper.</p>
        <p class="template-actions"><button type="button" class="btn btn-ghost" onclick="window.print()">Print checklist</button></p>

        <h3>Before you enter</h3>
        <ul class="check-list">
          <li><input type="checkbox" data-key="c1" id="c1"><label for="c1">Know which courtroom and cause-list board to check</label></li>
          <li><input type="checkbox" data-key="c2" id="c2"><label for="c2">Carry notebook, pen, and college ID — ask before using a phone</label></li>
          <li><input type="checkbox" data-key="c3" id="c3"><label for="c3">Dress for court; arrive before the first call</label></li>
        </ul>

        <h3>Civil hearing notes</h3>
        <ul class="check-list">
          <li><input type="checkbox" data-key="c4" id="c4"><label for="c4">Stage of suit (admission, framing of issues, evidence, arguments, judgment)</label></li>
          <li><input type="checkbox" data-key="c5" id="c5"><label for="c5">Who spoke for plaintiff / defendant and what was prayed</label></li>
          <li><input type="checkbox" data-key="c6" id="c6"><label for="c6">Documents referred to (without copying private details)</label></li>
          <li><input type="checkbox" data-key="c7" id="c7"><label for="c7">Next date and purpose of adjournment</label></li>
        </ul>

        <h3>Criminal hearing notes</h3>
        <ul class="check-list">
          <li><input type="checkbox" data-key="c8" id="c8"><label for="c8">Stage (remand, bail, charge, evidence, arguments, sentence)</label></li>
          <li><input type="checkbox" data-key="c9" id="c9"><label for="c9">Whether accused was produced / represented</label></li>
          <li><input type="checkbox" data-key="c10" id="c10"><label for="c10">Nature of application heard (bail, discharge, etc.) in general terms</label></li>
          <li><input type="checkbox" data-key="c11" id="c11"><label for="c11">Order passed and next listing</label></li>
        </ul>

        <h3>Ethics</h3>
        <ul class="check-list">
          <li><input type="checkbox" data-key="c12" id="c12"><label for="c12">No client names or identifiable facts on social media</label></li>
          <li><input type="checkbox" data-key="c13" id="c13"><label for="c13">No photos of case papers without explicit permission</label></li>
        </ul>
      </div>
    </section>
""",
)

PAGES["cheat-sheet.html"] = (
    "Citation and drafting cheat sheet for law students",
    "Practical citation habits and drafting notes for Indian law students.",
    "Cheat sheet",
    """
    <section class="section">
      <div class="wrap prose reveal">
        <p class="label">04 — Cheat sheet</p>
        <h1>Citation &amp; drafting</h1>
        <p class="lede">Habits that keep research notes usable when a senior asks for a one-page brief.</p>

        <h3>Case brief in 8 lines</h3>
        <ol>
          <li>Case name and court</li>
          <li>Citation / year</li>
          <li>Facts in 2 sentences</li>
          <li>Issue(s)</li>
          <li>Holding</li>
          <li>Reasoning (2–3 points)</li>
          <li>Order / relief</li>
          <li>Why it matters for your topic</li>
        </ol>

        <h3>Citation hygiene</h3>
        <ul>
          <li>Prefer neutral citations and official reporters when available.</li>
          <li>Always note the paragraph you rely on, not only the case name.</li>
          <li>Separate “quoted” language from your paraphrase in notes.</li>
          <li>Cross-check the Act section on India Code before citing an amendment.</li>
        </ul>

        <h3>Common student drafts (general)</h3>
        <ul>
          <li><strong>Case note</strong> — facts, issue, holding, comment.</li>
          <li><strong>Research memo</strong> — question, short answer, authorities, conclusion.</li>
          <li><strong>Hearing note</strong> — date, stage, what happened, next step.</li>
          <li><strong>Legal awareness flyer</strong> — one topic, plain language, no advice tone.</li>
        </ul>

        <p class="meta mt-lg">This is study guidance only — not a substitute for your college citation manual or chambers style.</p>
        <p class="mt-xl"><a class="text-link" href="resources.html">Open resource library <span class="btn-arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>
""",
)

PAGES["resources.html"] = (
    "Free legal research resources for Indian law students",
    "Curated free desks for case law, statutes, courts, and legal education.",
    "Resources",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">05 — Resources</p>
        <h1>Resource library</h1>
        <p class="lede">Public reference desks. Start here before paying for databases — then use college subscriptions when you need deeper coverage.</p>

        <h3>Case law &amp; statutes</h3>
        <ul class="resource-list">
          <li><a href="https://indiankanoon.org/" target="_blank" rel="noopener noreferrer">Indian Kanoon <span class="btn-arrow" aria-hidden="true">→</span></a><span>Judgments and statutes search</span></li>
          <li><a href="https://www.indiacode.nic.in/" target="_blank" rel="noopener noreferrer">India Code <span class="btn-arrow" aria-hidden="true">→</span></a><span>Central Acts and amendments</span></li>
          <li><a href="https://legislative.gov.in/" target="_blank" rel="noopener noreferrer">Legislative Department <span class="btn-arrow" aria-hidden="true">→</span></a><span>Bills and legislative materials</span></li>
        </ul>

        <h3>Courts</h3>
        <ul class="resource-list">
          <li><a href="https://www.sci.gov.in/" target="_blank" rel="noopener noreferrer">Supreme Court of India <span class="btn-arrow" aria-hidden="true">→</span></a><span>Judgments, cause lists, notices</span></li>
          <li><a href="https://ecourts.gov.in/" target="_blank" rel="noopener noreferrer">eCourts Services <span class="btn-arrow" aria-hidden="true">→</span></a><span>District and taluka case status</span></li>
        </ul>

        <h3>Profession &amp; education</h3>
        <ul class="resource-list">
          <li><a href="https://www.barcouncilofindia.org/" target="_blank" rel="noopener noreferrer">Bar Council of India <span class="btn-arrow" aria-hidden="true">→</span></a><span>Legal education and professional rules</span></li>
          <li><a href="https://www.livelaw.in/" target="_blank" rel="noopener noreferrer">LiveLaw <span class="btn-arrow" aria-hidden="true">→</span></a><span>Legal news (verify against primary sources)</span></li>
          <li><a href="https://www.barandbench.com/" target="_blank" rel="noopener noreferrer">Bar &amp; Bench <span class="btn-arrow" aria-hidden="true">→</span></a><span>Courts, colleges, profession</span></li>
        </ul>
        <p class="meta mt-md">Not affiliated with this portfolio. Always prefer primary text of the law.</p>
      </div>
    </section>
""",
)

PAGES["reading-lists.html"] = (
    "Starter reading lists for Criminal, Civil, and Constitutional Law",
    "First cases and Acts Indian law students should know early.",
    "Reading lists",
    """
    <section class="section">
      <div class="wrap prose reveal">
        <p class="label">06 — Reading lists</p>
        <h1>Subject reading lists</h1>
        <p class="lede">Starter maps — not exhaustive syllabi. Read the judgment or Act text, then a short note of your own.</p>

        <h3>Criminal Law</h3>
        <ul>
          <li>Structure of offences and general exceptions — read the relevant Code chapters your college assigns (BNS / IPC transition as taught).</li>
          <li>Bail principles — a leading Supreme Court discussion your faculty recommends this term.</li>
          <li>One evidentiary concept: burden, confession, or dying declaration — as taught.</li>
          <li>Practice: sit one remand / bail day and write a hearing note.</li>
        </ul>

        <h3>Civil Law</h3>
        <ul>
          <li>CPC spine: jurisdiction, pleadings, temporary injunctions, execution — as in your syllabus.</li>
          <li>Contract essentials: offer, acceptance, consideration, breach.</li>
          <li>One property or tort case used in class — brief it in 8 lines.</li>
          <li>Practice: watch a civil evidence day and note stages only.</li>
        </ul>

        <h3>Constitutional Law</h3>
        <ul>
          <li>Articles on equality, freedom, life and personal liberty — text first.</li>
          <li>Basic structure idea — one classic case your course uses.</li>
          <li>Writs under Article 32 / 226 — purpose of each in one line.</li>
          <li>Practice: summarise one recent constitutional news item using primary court text if available.</li>
        </ul>

        <p class="meta mt-lg">Ask your faculty which reporter / edition they want. Course books still come first.</p>
      </div>
    </section>
""",
)

PAGES["openings.html"] = (
    "Internship openings for law students",
    "Curated public internship-style opportunities and a form to suggest openings for classmates.",
    "Openings",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">07 — Openings</p>
        <h1>Internship openings</h1>
        <p class="lede">Starting points classmates can check. Always verify on the organisation’s own site. This page does not place students or collect fees.</p>

        <article class="opening">
          <div class="opening-top">
            <h3>Supreme Court / High Court internship notices</h3>
            <p class="meta">Rolling · verify dates</p>
          </div>
          <p class="org">Official court websites</p>
          <p>Many courts publish student internship circulars each year. Check the court’s “Internship” or “Students” page and follow their form exactly.</p>
          <p><a class="text-link" href="https://www.sci.gov.in/" target="_blank" rel="noopener noreferrer">Supreme Court site <span class="btn-arrow" aria-hidden="true">→</span></a></p>
        </article>

        <article class="opening">
          <div class="opening-top">
            <h3>Think-tank &amp; research desks</h3>
            <p class="meta">Seasonal</p>
          </div>
          <p class="org">Public research organisations</p>
          <p>Watch careers pages of policy and security institutes your seniors recommend. Applications usually ask for a short writing sample and CV.</p>
        </article>

        <article class="opening">
          <div class="opening-top">
            <h3>Legal aid &amp; campus cells</h3>
            <p class="meta">Ongoing</p>
          </div>
          <p class="org">University legal aid cells</p>
          <p>Join your college LAC / clinic drives. Good training for communication and research — describe the work in general terms on your CV.</p>
        </article>

        <article class="opening">
          <div class="opening-top">
            <h3>Local chambers (Surat / Indore / your city)</h3>
            <p class="meta">Network</p>
          </div>
          <p class="org">Advocates &amp; small firms</p>
          <p>Use the playbook cold email. Prefer introductions from faculty or seniors when possible.</p>
          <p><a class="text-link" href="playbook.html">Open playbook <span class="btn-arrow" aria-hidden="true">→</span></a></p>
        </article>

        <h3 class="mt-xl">Suggest an opening for the batch</h3>
        <p class="meta">Share a public link only — no private client work.</p>
        <form class="suggest-form" id="suggest-form" data-subject="Internship opening suggestion" data-linkedin="https://www.linkedin.com/in/drashti-baser">
          <label>Your name<input name="Name" required autocomplete="name"></label>
          <label>Organisation<input name="Organisation" required></label>
          <label>Public link<input name="Link" type="url" placeholder="https://"></label>
          <label>Why it helps students<textarea name="Why" required maxlength="600"></textarea></label>
          <p class="form-note">Opens LinkedIn so you can paste the draft. Email can replace this when published on the portfolio.</p>
          <button class="btn" type="submit">Share suggestion</button>
        </form>
      </div>
    </section>
""",
)

PAGES["ask.html"] = (
    "Ask a senior — questions for fellow law students",
    "Send a short question about internships, legal aid, or building a law portfolio.",
    "Ask a senior",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">08 — Ask</p>
        <h1>Ask a senior</h1>
        <p class="lede">Short, practical questions work best — internships, court first weeks, legal aid, or how to describe experience on a CV.</p>

        <form class="ask-form" id="ask-form" data-subject="Ask a senior — law student question" data-linkedin="https://www.linkedin.com/in/drashti-baser">
          <label>Your name<input name="Name" required autocomplete="name"></label>
          <label>College / year<input name="College" required placeholder="e.g. BA LLB Year 2"></label>
          <label>Topic
            <select name="Topic" required>
              <option value="">Select</option>
              <option>Internships</option>
              <option>Court observation</option>
              <option>Legal aid</option>
              <option>Portfolio / CV</option>
              <option>Research writing</option>
              <option>Other</option>
            </select>
          </label>
          <label>Your question<textarea name="Question" required maxlength="800" placeholder="Keep it to one clear question."></textarea></label>
          <p class="form-note">Not legal advice. Answers are informal peer guidance. Until an email is published, this opens LinkedIn with your draft ready to paste.</p>
          <button class="btn" type="submit">Send via LinkedIn</button>
        </form>

        <div class="faq" style="margin-top:48px">
          <h3>Already answered</h3>
          <details open>
            <summary>How do I start a law portfolio as a student?</summary>
            <p>Keep one page with education, internships, leadership roles, and a CV download. Add certificates as PDFs. Update dates after every internship. Avoid client names and case details.</p>
          </details>
          <details>
            <summary>What should I learn from a District Court internship?</summary>
            <p>Focus on how filings move, how hearings are called, and how advocates manage procedure. Take notes on formats and stages of trial.</p>
          </details>
          <details>
            <summary>Is legal aid cell work useful for litigation?</summary>
            <p>Yes. Outreach and research train you to explain law clearly — skills that transfer to chambers and firms.</p>
          </details>
        </div>
      </div>
    </section>
""",
)

PAGES["calendar.html"] = (
    "Campus and career calendar for law students",
    "Student-relevant dates: moots, AIBE orientation, internship seasons.",
    "Calendar",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">09 — Calendar</p>
        <h1>Campus &amp; career calendar</h1>
        <p class="lede">Orientation dates for planning — always confirm on official notices. Add your college moot / LAC dates locally.</p>
        <ul class="cal-list">
          <li>
            <p class="cal-date">Winter break</p>
            <div>
              <h3>Winter internship window</h3>
              <p class="meta">Typical Dec–Jan applications for Dec–Jan / Jan–Feb seats</p>
              <p>Finish CV and 8–12 cold emails 4–6 weeks before exams end.</p>
            </div>
          </li>
          <li>
            <p class="cal-date">Summer break</p>
            <div>
              <h3>Summer internship window</h3>
              <p class="meta">Typical Apr–May applications for May–Jul seats</p>
              <p>Court and chambers seats fill early — apply while semester is still on.</p>
            </div>
          </li>
          <li>
            <p class="cal-date">Monsoon / autumn</p>
            <div>
              <h3>Moot &amp; memorial season</h3>
              <p class="meta">College calendars vary</p>
              <p>Block research weeks before memorial deadlines; reuse the citation cheat sheet.</p>
            </div>
          </li>
          <li>
            <p class="cal-date">Final years</p>
            <div>
              <h3>AIBE orientation</h3>
              <p class="meta">After graduation — check BCI notices</p>
              <p>Track Bar Council of India announcements for exam windows and enrolments.</p>
              <p><a class="text-link" href="https://www.barcouncilofindia.org/" target="_blank" rel="noopener noreferrer">BCI site <span class="btn-arrow" aria-hidden="true">→</span></a></p>
            </div>
          </li>
          <li>
            <p class="cal-date">Ongoing</p>
            <div>
              <h3>Legal aid drives</h3>
              <p class="meta">Campus LAC</p>
              <p>Volunteer for at least one awareness drive per semester if your cell runs them.</p>
            </div>
          </li>
        </ul>
      </div>
    </section>
""",
)

PAGES["peer-groups.html"] = (
    "Peer study and moot groups for law students",
    "Opt-in circles for research, moots, and legal aid — connect via LinkedIn.",
    "Peer groups",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">10 — Peer groups</p>
        <h1>Peer study groups</h1>
        <p class="lede">Small circles beat large noisy groups. Use LinkedIn to say which circle you want — WhatsApp/Telegram links can be added when the batch creates them.</p>
        <ul class="peer-list">
          <li>
            <h3>Research circle</h3>
            <p>Weekly case briefs — Criminal / Constitutional focus. Share notes, not leaked papers.</p>
            <a class="btn btn-ghost" href="https://www.linkedin.com/in/drashti-baser" target="_blank" rel="noopener noreferrer">Message to join interest list</a>
          </li>
          <li>
            <h3>Moot prep pod</h3>
            <p>Memorial structure checks and oral rounds practice for those registered in a moot.</p>
            <a class="btn btn-ghost" href="https://www.linkedin.com/in/drashti-baser" target="_blank" rel="noopener noreferrer">Message to join interest list</a>
          </li>
          <li>
            <h3>Legal aid volunteers</h3>
            <p>Coordinate campus awareness content and research support for LAC drives.</p>
            <a class="btn btn-ghost" href="https://www.linkedin.com/in/drashti-baser" target="_blank" rel="noopener noreferrer">Message to join interest list</a>
          </li>
        </ul>
        <p class="meta mt-lg">Groups are peer-led and informal. No fees. Conduct stays professional.</p>
      </div>
    </section>
""",
)

PAGES["portfolio-tips.html"] = (
    "Portfolio and LinkedIn tips for law students",
    "How to describe internships safely and keep a clean one-page portfolio.",
    "Portfolio tips",
    """
    <section class="section">
      <div class="wrap prose reveal">
        <p class="label">11 — Portfolio tips</p>
        <h1>Portfolio &amp; LinkedIn</h1>
        <p class="lede">One clear page beats five decorative ones. Protect confidentiality while still showing what you learned.</p>

        <h3>What to publish</h3>
        <ul>
          <li>Role title, organisation, city, dates, and duration.</li>
          <li>Skills: research, drafting support, hearing notes, outreach — in general terms.</li>
          <li>Certificates as PDFs when you have permission to share them.</li>
        </ul>

        <h3>What to avoid</h3>
        <ul>
          <li>Client names, party names, and case numbers that identify people.</li>
          <li>Photos of case papers or courtroom parties.</li>
          <li>Claims that you “represented” clients as a student.</li>
          <li>Skill bars and buzzwords that you cannot explain in an interview.</li>
        </ul>

        <h3>LinkedIn hygiene</h3>
        <ul>
          <li>Headline: year + focus (e.g. BA LLB · Litigation &amp; research).</li>
          <li>About: 4–5 lines, same voice as your portfolio.</li>
          <li>Feature the portfolio link and CV once — keep them updated together.</li>
        </ul>

        <p class="mt-xl"><a class="btn" href="../index.html">See this portfolio structure</a>
        <a class="text-link" href="templates.html" style="margin-left:18px">CV templates <span class="btn-arrow" aria-hidden="true">→</span></a></p>
      </div>
    </section>
""",
)

PAGES["digest.html"] = (
    "Law desk digest for law students",
    "Weekly student briefing plus live headlines from LiveLaw, Bar & Bench, and campus coverage.",
    "Digest",
    """
    <section class="section">
      <div class="wrap reveal">
        <p class="label">12 — Digest</p>
        <h1>Law desk digest</h1>
        <p class="lede">A short briefing for classmates, plus live headlines. Read news critically — always prefer the judgment or circular itself.</p>

        <div class="digest-week">
          <h3>This week for students</h3>
          <p class="meta">Editorial note · update when you refresh the hub</p>
          <ul>
            <li>Watch legal-education and Bar Council coverage — it affects colleges and enrolments.</li>
            <li>If a Supreme Court or High Court internship circular is open, apply early with a one-page CV.</li>
            <li>Use one hearing this week to practise the court checklist (stages only, no client details).</li>
          </ul>
          <p class="mt-md"><a class="text-link" href="court-checklist.html">Open checklist <span class="btn-arrow" aria-hidden="true">→</span></a></p>
        </div>

        <div class="law-desk" id="law-desk" aria-labelledby="law-desk-heading">
          <div class="law-desk-head">
            <div>
              <h3 id="law-desk-heading">Live headlines</h3>
              <p class="meta">LiveLaw, Bar &amp; Bench, and campus / CLAT coverage via free APIs.</p>
            </div>
            <p class="meta law-desk-status" id="law-desk-status" aria-live="polite">Updating…</p>
          </div>
          <ul class="news-list" id="law-news" hidden></ul>
          <div class="news-fallback" id="law-news-fallback" hidden>
            <p class="meta">Headlines could not load. Try these desks:</p>
            <ul class="resource-list">
              <li><a href="https://www.livelaw.in/" target="_blank" rel="noopener noreferrer">LiveLaw <span class="btn-arrow" aria-hidden="true">→</span></a><span>Legal news</span></li>
              <li><a href="https://www.barandbench.com/" target="_blank" rel="noopener noreferrer">Bar &amp; Bench <span class="btn-arrow" aria-hidden="true">→</span></a><span>Courts &amp; colleges</span></li>
            </ul>
          </div>
        </div>
      </div>
    </section>
""",
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for file, (title, desc, crumb, body) in PAGES.items():
        html = chrome(title, desc, file, crumb, body)
        (OUT / file).write_text(html, encoding="utf-8")
        print("wrote", file)
    print("done", len(PAGES))


if __name__ == "__main__":
    main()
