# Personal dashboard — GitHub Pages setup

One-time setup:

1. Create a new GitHub repository (public or private, doesn't matter — e.g. `personal-dashboard`).
2. Push the contents of this folder to the repo root, keeping the folder
   structure intact (`index.html`, `CNAME`, and `.github/workflows/deploy.yml`).
3. In the repo: **Settings → Pages → Build and deployment → Source** →
   set to **GitHub Actions**.
4. Still in **Settings → Pages → Custom domain**, enter:
   `dashboard.stalledtime.com` → **Save**.
5. At your DNS provider for `stalledtime.com`, add a CNAME record:
   - **Host/Name:** `dashboard`
   - **Value/Target:** `<your-github-username>.github.io`
   - **TTL:** default is fine
6. Wait for DNS to propagate (usually minutes, sometimes a couple of
   hours). GitHub will auto-issue an HTTPS certificate for the custom
   domain once it verifies — you'll see a green check in the Pages
   settings when it's ready.

After that, every push to `main` auto-deploys via the included Action —
no manual upload step.

## Getting updates from Claude after this is live

Whenever you ask for a refresh, Claude will hand you an updated
`index.html`. Replace the file in the repo and push (or paste the new
content into GitHub's web editor and commit directly) — the Action
picks it up and redeploys automatically.
