# Website Architecture & Design System

This document outlines the visual structure, design tokens, and technical implementation of the Resilience Network research web portal (`resiliencenetwork.xyz`).

---

## 1. Design Philosophy

The site embodies an authoritative, intellectual, and peer-reviewed cryptographic research institute aesthetic (analogous to Paradigm, Flashbots, and Ethereum Research).
- **Sole Mark Principle**: The official Resilience Shield (`logo.png`) is featured strictly once in the navigation header as an institutional hallmark.
- **Editorial Gravitas**: Headings styled in `Instrument Serif` contrasted against geometric sans (`Plus Jakarta Sans`) and monospace code notation (`JetBrains Mono`).
- **Mathematical Interactive Visualization**: A dynamic 2D canvas arithmetization model simulating Halo 2 polynomial constraint lattices and Merkle note commitments with mouse gravitation physics.
- **Zero Framework Footprint**: Pure semantic HTML5, CSS custom properties, and vanilla ES6 JavaScript.

---

## 2. Design Tokens (`:root`)

```css
:root {
  /* Brand Accents */
  --color-blue: #002fa6;
  --color-blue-dark: #001f73;
  --color-blue-tint: #f0f4ff;
  --color-gold: #b45309;
  --color-gold-bright: #d97706;

  /* Editorial Light Canvas */
  --color-canvas: #ffffff;
  --color-canvas-alt: #f8fafc;
  --color-border: #e2e8f0;

  /* Typography */
  --font-serif: 'Instrument Serif', Georgia, serif;
  --font-sans: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

## 3. Structural Components

1. **Academic Top Navigation**: Displays the single official emblem, protocol metadata badge, and direct links to GitHub, architecture documentation, and live epoch status.
2. **Hero Abstract & Thesis**: Large serif declaration ("Something is cooking in the cryptography lab") followed by an academic abstract detailing the state machine mechanics.
3. **Interactive Halo 2 Constraint Mesh**: Real-time canvas rendering polynomial commitment nodes, algebraic root indicators ($\omega^i$), and interactive mouse gravitational vector fields.
4. **Architectural Research Pillars (Tracks 01—04)**: Technical breakdowns covering Orchard Zero-Knowledge Shielded Pools, Deterministic PoS Consensus, Native EVM Execution, and Guardian Social Recovery.
5. **Protocol Specification Manifest**: A formal parameter table detailing the consensus quorum, curve cycles, hash algorithms, and genesis commitments.
6. **Academic Footer**: Links to research tracks, protocol security index, reference vectors, and formal test harness specifications.
