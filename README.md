# ResilienceNetwork.xyz

The official web portal and landing page for **Resilience Network** — an experimental Proof-of-Stake blockchain with native Orchard shielded privacy, EVM execution, and cryptographic finality.

🌐 **Live URL**: [resiliencenetwork.xyz](https://resiliencenetwork.xyz)  
🔗 **Core Blockchain Repository**: [Resilience-Network/Chain](https://github.com/Resilience-Network/Chain)

---

## ✨ Features & Design Highlights

- **Pure Vanilla Stack**: Built with semantic HTML5, modern CSS3 custom properties, and native JavaScript — 0 external npm dependencies required for runtime.
- **Multi-Page Research Portal**: A landing page plus five content sections — Protocol, Research & Assurance, Status & Roadmap, Design Decisions, and Get Started — every claim linking back to a canonical artifact in the Chain repository.
- **Honest Telemetry**: No simulated chain data. The landing lattice is labeled as an interactive simulation, and the displayed genesis protocol commitment is the real value from `configs/genesis.json`.
- **Interactive Mathematical Visualization**: A canvas-rendered Halo-2 constraint lattice with pointer attraction, commitment nodes and ω-power annotations.
- **Light Academic Aesthetic**: Instrument Serif display type, Plus Jakarta Sans body, JetBrains Mono annotations, and a royal-blue/gold brand system on a clean canvas.
- **Accessible & Responsive**: Semantic landmarks, single `<h1>` per page, ARIA-labelled navigation with a mobile menu, Open Graph metadata, sitemap and robots.txt.

---

## 📁 Repository Structure

```text
├── index.html          # Landing page: pillars, portal index, genesis spec
├── protocol.html       # Protocol specification: consensus, EVM, shielded, authorization
├── research.html       # Research & assurance: load qualification, threat models, methodology
├── status.html         # Capability matrix, known limits, milestone roadmap
├── decisions.html      # Architecture decision records (ADRs)
├── get-started.html    # Build, localnet, RPC and wallet onboarding
├── styles.css          # Shared design system (tokens, components, responsive rules)
├── sitemap.xml         # Search engine sitemap
├── robots.txt          # Crawler policy
├── logo.png            # Brand insignia
├── AGENTS.md           # Instructions & rules for autonomous agents and pair-programmers
├── CONTRIBUTING.md     # Branching guidelines, commit standards, and PR workflows
├── docs/               # Technical and design documentation
│   ├── README.md       # Docs index and navigation
│   ├── architecture.md # Design system, tokens, and animation architecture
│   └── deployment.md   # Deployment instructions (GitHub Pages / DNS)
└── .github/            # CI/CD and pull request templates
```

---

## 🚀 Local Development

No build step or package installation is required! You can preview the website using any static HTTP server.

### Using Python 3
```bash
python3 -m http.server 8000
```
Then open [http://localhost:8000](http://localhost:8000) in your browser.

### Using Node / npx
```bash
npx serve .
```

---

## 🤝 Contributing

We follow a strict branch discipline: **never commit directly to `main`**. All modifications must go through dedicated topic branches and pull requests.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before submitting contributions.

---

## 📄 License

Part of the Resilience Network project ecosystem. See repository details for license terms.
