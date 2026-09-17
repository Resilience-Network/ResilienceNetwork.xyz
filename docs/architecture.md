# Website Architecture & Design System

This document outlines the visual structure, design tokens, and animation systems powering `ResilienceNetwork.xyz`.

---

## 1. Design Philosophy

The site embodies a crisp, modern, light-mode cryptographic aesthetic centered on the theme **"Something is cooking."** It harmonizes:
- **The Official Resilience Shield (`logo.png`)**: A bold royal cobalt blue background (`#002fa6`), striking golden yellow shield contour (`#fdc703`), and angular white monogram 'R'.
- **Clean Swiss / Fintech Light Palette**: Pristine off-white backdrop (`#f8fafc`) accented by soft luminous radial auras in royal blue and warm gold.
- **Zero-Dependency Philosophy**: High performance, instant loading, and smooth 60fps animations utilizing only vanilla browser capabilities (HTML5, CSS3, 2D Canvas).

---

## 2. Design Tokens (`:root`)

The interface styles are governed by centralized CSS custom properties in `index.html`:

```css
:root {
  /* Brand Colors from logo.png */
  --brand-blue: #002fa6;
  --brand-blue-deep: #001f73;
  --brand-blue-light: #e8edff;
  --brand-gold: #fdc703;
  --brand-gold-warm: #f59e0b;
  --brand-gold-soft: #fffbeb;

  /* Light Canvas & Cards */
  --bg-canvas: #f8fafc;
  --bg-card: rgba(255, 255, 255, 0.88);
  --text-heading: #0b1528;
  --text-body: #334155;
  --text-muted: #64748b;

  /* Typography */
  --font-display: 'Outfit', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

---

## 3. Core Visual Components

### A. The 3D Resilience Shield Chamber
- **Emblem Card**: Displays `logo.png` inside an elevated card with multi-stage drop shadows.
- **Parallax Tilt**: Real-time cursor coordinates apply smooth 3D perspective transforms:
  ```javascript
  const tiltX = -yPercent * 14;
  const tiltY = xPercent * 14;
  emblem.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
  ```
- **Rising Steam Vapors**: Soft gold and blue blurred nodes simulating convective energy.
- **Dual Orbital Rings**: Counter-rotating dashed and dotted orbital tracks carrying cryptographic badges (`Orchard ZK`, `EVM State`, `PoS Consensus`, `Guardian Auth`).

### B. Ambient Background Canvas
- **Sparks & Embers**: 40 royal blue and golden spores floating upward with gentle horizontal drift.
- **Constellation Mesh**: Soft connective lines dynamically drawn between nearby particles within a 90px threshold.

### C. Live Telemetry Strip
- A clean glassmorphism pill displaying live metrics:
  - Dynamic block height incrementing periodically.
  - Active PoS consensus health.
  - Native Orchard ZK privacy marker.
  - Ambient crucible heat sensor fluctuating around 1,337°C.
