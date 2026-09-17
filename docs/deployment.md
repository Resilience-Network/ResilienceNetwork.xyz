# Deployment Guide

This guide details the hosting options and continuous delivery configuration for `ResilienceNetwork.xyz`.

---

## 1. Static Hosting Options

Since the website is entirely static (HTML, CSS, JS), it can be deployed with zero backend dependencies on:
- **GitHub Pages** (Default)
- **Cloudflare Pages**
- **Vercel**
- **AWS S3 + CloudFront**

---

## 2. GitHub Pages Configuration

### Automated Deployment via GitHub Actions
Create a `.github/workflows/deploy.yml` file to deploy on push to `main`:

```yaml
name: Deploy Static Website to GitHub Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 3. Custom Domain Setup (`resiliencenetwork.xyz`)

To link the custom domain:

1. Add a `CNAME` file in the root directory:
   ```text
   resiliencenetwork.xyz
   ```
2. Configure DNS A Records with your domain registrar:
   - `185.199.108.153`
   - `185.199.109.153`
   - `185.199.110.153`
   - `185.199.111.153`
3. Configure CNAME Record for `www`:
   - `www` -> `<username>.github.io`
4. In GitHub Repository Settings -> Pages, enable **Enforce HTTPS**.
