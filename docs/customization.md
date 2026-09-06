# Customize site

All site content lives in `src/`. Do not edit `public/`; build regenerates it.

## Content

Edit `src/index.html` before publishing:

- `<title>`, description, Open Graph, and Twitter metadata
- name, role, positioning statement, location, and email
- GitHub, LinkedIn, blog, project, and other external URLs
- experience, education, project, and skill entries

Use specific outcomes and real project links. Remove sections and project cards you do not need rather than leaving sample content.

## Images

Replace `src/images/` placeholders:

| File | Use |
| --- | --- |
| `avatar-placeholder.svg` | About-section portrait |
| `project-placeholder.svg` | Project card image |
| `favicon.svg` | Browser icon |

After adding a replacement image, update matching `src` and `alt` text in `src/index.html`. For social previews, use an absolute HTTPS image URL in `og:image` and `twitter:image` after deploy.

## Résumé

`src/resume.md` is linked from site and served as plain Markdown. Replace its content or remove every link to it from `src/index.html`.

To publish a PDF instead:

1. Add `src/resume.pdf`.
2. Change the résumé links in `src/index.html` from `./resume.md` to `./resume.pdf`.
3. Add `https://your-domain.example/resume.pdf` to `src/sitemap.xml` if you want it indexed.
4. Run `npm test` to confirm link exists.

Avoid publishing home address, personal phone number, or anything not intended for public internet.

## Contact form

Template uses a `mailto:` link only. For a form, create account with form provider such as Formspree, then add a semantic `<form>` in contact section using provider's endpoint. Never commit API keys or secret tokens; browser form endpoints are public by design.

## Render

### Before first deploy

- Replace `name` in `render.yaml` with unique service name.
- Commit `render.yaml`, `package.json`, `package-lock.json`, and `src/` changes.
- Confirm `npm ci && npm test && npm run build` succeeds locally.

### Blueprint deploy

1. In Render dashboard, select **New** → **Blueprint**.
2. Connect GitHub repository and select branch.
3. Confirm detected build command: `npm ci && npm run build`.
4. Confirm publish directory: `public`.
5. Create service and wait for deploy to finish.

### Manual deploy

Create **Static Site** instead of a Web Service. Set build command to `npm ci && npm run build` and publish directory to `public`.

### Verify

- Visit Render URL on desktop and mobile.
- Open résumé, project, and social links.
- Inspect page source for unresolved placeholders or `example.com`.
- Add custom domain from **Settings** → **Custom Domains**. Render provisions HTTPS after DNS verifies.

Pushes to configured branch redeploy automatically. If build fails, read Render build log locally first with `npm ci && npm run build`.
