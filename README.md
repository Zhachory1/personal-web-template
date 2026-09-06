# Personal Web Template

Minimal static resume and portfolio site with all personal content and assets replaced by placeholders.

Use **Use this template** on GitHub to create your own repository, then personalize content in `src/` before deploying. Released under [MIT License](LICENSE).

## Local development

Requires Node.js and Python 3.

```bash
npm ci
npm test
npm run build
npm run serve
```

Open <http://localhost:8000>. Edit `src/`; `public/` is generated and ignored by Git.

| Command | Purpose |
| --- | --- |
| `npm test` | Checks local links, images, metadata, anchors, and mobile navigation markup. |
| `npm run build` | Copies `src/` to `public/` and minifies JavaScript. |
| `npm run serve` | Serves built files locally. |

## Personalize

1. Replace sample text, URLs, metadata, and `example.com` in `src/index.html`.
2. Update `src/resume.md` or replace it with your own résumé.
3. Replace files in `src/images/` with your portrait, project screenshots, favicon, and social-preview image.
4. Update `src/sitemap.xml` with your production URL.
5. Run `npm test`, then `npm run build` and preview locally.

Detailed content, résumé, asset, and contact-form guidance: [`docs/customization.md`](docs/customization.md).

## Deploy on Render

### Blueprint

1. Push your personalized repository to GitHub.
2. In Render, select **New** → **Blueprint** and connect repository.
3. Render reads [`render.yaml`](render.yaml), builds with `npm ci && npm run build`, and publishes `public/`.
4. Change `name` in `render.yaml` to a unique Render service name before creating service.
5. Add custom domain in service **Settings** → **Custom Domains** after first deploy.

### Manual static site

1. In Render, select **New** → **Static Site**, then connect repository and choose branch.
2. Set build command to `npm ci && npm run build`.
3. Set publish directory to `public`.
4. Create static site. Pushes to selected branch automatically redeploy it.

See [`docs/customization.md#render`](docs/customization.md#render) for verification and deployment notes.

## Structure

```text
src/
  index.html       Site content and SEO metadata
  resume.md        Browser-readable résumé
  css/styles.css   Visual design and responsive layout
  js/scripts.js    Navigation behavior
  images/          Replaceable placeholder assets
public/            Generated deployment output
render.yaml        Render Blueprint configuration
```
