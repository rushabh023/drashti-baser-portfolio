# Drashti Baser — portfolio

A single-page static site. Open `index.html` in a browser, or deploy the folder as-is.

The files in `assets/docs/` are stand-ins. Replace them with the real CV and certificates before publishing. Each PDF says PLACEHOLDER inside so it is not mistaken for the real document.

## Replace placeholders

1. Open `index.html` and search for `class="todo"`.
2. Replace each yellow `[PLACEHOLDER: …]` with the real detail. Keep the surrounding sentence.
3. For the email, replace both the visible text and the `mailto:` address on that button.
4. Confirm the LinkedIn URL. It is currently `https://www.linkedin.com/in/drashti-baser`. If the real profile differs, update the visible text, the `href`, and `sameAs` in the JSON-LD block in the page head.
5. When no `class="todo"` remains, delete the `.todo` rule in `assets/css/styles.css`.
6. Replace `https://drashtibaser.com/` in the canonical link, Open Graph tags, and JSON-LD in `index.html`, plus `robots.txt` and `sitemap.xml`.

## Add a portrait

Best: a cutout with a transparent background, saved as `assets/img/drashti-cutout.png`. The page places it at the bottom of the grey hero panel. You can make a cutout with remove.bg, Canva’s background remover, or Photoshop.

Fallback: save a normal photo as `assets/img/drashti.jpg`. If the cutout file is missing, the page uses this photo as a rectangle inside the panel.

Reload the page after adding either file. If neither file is there, the panel shows the DB monogram.

Optional second photo for the About section: `assets/img/drashti-2.jpg`, portrait orientation. If it is missing, that block stays a grey panel with the monogram.

## Show Writing and Recommendations

Both sections are hidden until the placeholders are real.

Writing:

1. Replace the type, title, summary, and Read PDF link in the Writing section.
2. Remove `hidden` from `<section id="writing">`.
3. Remove `hidden` from the Writing link in the header (`<li hidden>`) and from the Writing link in the mobile menu.

Recommendations:

1. Replace the quote, name, and role only with a real quote you have permission to publish.
2. Remove `hidden` from `<section id="recommendations">`.

Do not invent a quote.

## Swap the CV

Replace `assets/docs/Drashti-Baser-CV.pdf` with the real CV, using the same file name. Do the same for:

- `assets/docs/usi-internship-certificate.pdf`
- `assets/docs/district-court-indore-certificate.pdf`

## Update “Last updated”

In the footer, replace `[PLACEHOLDER: Month Year]` with the month and year of the edit, for example September 2026. Set `<lastmod>` in `sitemap.xml` to that date as `YYYY-MM-DD`.

## Deploy on Netlify

1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop).
2. Drag this folder onto the page.
3. Netlify gives you a free address ending in `.netlify.app`.

There is no build command. The publish folder is the one that contains `index.html`.

## Deploy on GitHub Pages

1. Create a repository and upload these files. `index.html` stays at the repository root.
2. Open Settings, then Pages.
3. Set Source to Deploy from a branch.
4. Choose the branch (usually `main`) and the folder `/ (root)`, then save.
5. The site appears at `https://<user>.github.io/<repository>/`.

If the site lives in a project subpath, update the canonical URL, Open Graph image URL, `robots.txt`, and `sitemap.xml` to that full address.

## Connect a custom domain

A name such as `drashtibaser.com` or `drashtibaser.in` is registered with a registrar, then pointed at the host.

Netlify: open Domain management, add the domain, and follow the DNS instructions. Turn on HTTPS when the certificate is offered.

GitHub Pages: under Settings, then Pages, enter the custom domain. At the registrar, add the A records and CNAME that GitHub shows. Enforce HTTPS after DNS settles.

Then replace `https://drashtibaser.com/` in `index.html`, `robots.txt`, and `sitemap.xml` with the real address, including `https://` and a trailing slash on the canonical URL.
