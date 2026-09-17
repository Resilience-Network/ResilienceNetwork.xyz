# Website Architecture & Design System

This document outlines the visual structure, design tokens, and animation systems powering `ResilienceNetwork.xyz`.

---

## 1. Design Philosophy

The site embodies a futuristic, cryptographic aesthetic centered on the theme **"Something is cooking."** It merges:
- **Culinary Alchemy & Blockchain Genesis**: The central crucible acts as an oven/furnace forging cryptographic blocks, state transitions, and zero-knowledge privacy pools.
- **OLED Void Palette**: Deep background shades (`#05070b`) accented by thermal gradients (`#ff5e36`, `#f59e0b`) and cybernetic highlights (`#00f0ff`, `#8b5cf6`).
- **Zero-Dependency Philosophy**: High performance, instant loading, and 60fps animations utilizing only vanilla browser capabilities (HTML5, CSS3, 2D Canvas).

---

## 2. Design Tokens (`:root`)

The interface styles are governed by centralized CSS custom properties in `index.html`:

```css
:root {
  /* Color Canvas */
  --bg-dark: #05070b;
  --text-main: #f8fafc;
  --text-muted: #94a3b8;
  --text-dim: #475569;

  /* Radiant Accents */
  --accent-flame: #ff5e36;
  --accent-amber: #f59e0b;
  --accent-cyan: #00f0ff;
  --accent-violet: #8b5cf6;

  /* Typography */
  --font-display: 'Outfit', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

## 3. Core Visual Components

### A. The 3D Cryptographic Crucible
- **Structure**: Multi-layered container with an SVG crucible body, bubbling molten core, and base heat flames.
- **Parallax Tilt**: Uses real-time pointer coordinates to apply perspective transforms:
  ```javascript
  const tiltX = -yPercent * 16;
  const tiltY = xPercent * 16;
  core.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
  ```
- **Rising Steam Vapors**: Four staggered CSS-animated blur nodes simulating heat convection.
- **Dual Orbital Rings**: Counter-rotating dashed and dotted orbital tracks carrying cryptographic badges (`Orchard ZK`, `EVM State`, `PoS Consensus`, `Guardian Auth`).

### B. Ambient Background Canvas
- **Sparks & Embers**: 48 particles drifting upward with random horizontal jitter and individual alpha decay.
- **Constellation Mesh**: Dynamic line rendering between any two particles within a 100px proximity radius.

### C. Live Telemetry Strip
- A glassmorphism pill displaying live metrics:
  - Simulated block height incrementing periodically.
  - Constant PoS consensus health indicator.
  - Shielded privacy and EVM compatibility markers.
  - Dynamic ambient crucible temperature fluctuating around 1,337°C.

---

## 4. Responsive Layout Breakpoints

- **Desktop (1024px+)**: Full viewport height (100vh) single-screen presentation without scrollbars.
- **Tablet / Mobile (<680px)**: Natural vertical stacking, scaled-down crucible chamber, and centered footer elements to accommodate small screens comfortably.
