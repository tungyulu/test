# UI Contract: Root Navigation Hub

**Feature**: 002-root-nav-hub | **Date**: 2026-06-21

---

## Page Structure

```
<body>
  <header>          ← Site title + tagline
  <main>
    <section.cards> ← 3-column grid of NavCards
  </main>
  <footer>          ← Attribution / static note
```

---

## Header Contract

| Element | Content | Styling notes |
|---------|---------|---------------|
| `<h1>` | "我的小工具" (or similar site name) | `font-black`, large, indigo accent |
| `<p>` (tagline) | "選擇想前往的頁面" | `text-slate-400`, small |
| Wrapper background | Gradient `from-indigo-900 via-slate-900 to-slate-950` | Matches betting.html header |

---

## NavCard Contract

Each card is a block `<a>` element with the following structure:

```html
<a href="{href}" class="nav-card ...">
  <div class="card-emoji">  {emoji}  </div>
  <h2 class="card-title">   {title}  </h2>
  <p  class="card-desc">    {desc}   </p>
  <div class="card-arrow">  →        </div>
</a>
```

### Visual States

| State | Appearance |
|-------|-----------|
| Default | `bg-white/5`, `border border-white/10`, `rounded-2xl`, padding `p-6` |
| Hover (pointer device) | Lifted `y: -6px`, `scale: 1.03`, indigo box-shadow — animated by GSAP |
| Focus (keyboard) | Browser default focus ring; no custom style required |
| Active (click) | `active:scale-95` via Tailwind utility |

### Layout Breakpoints

| Breakpoint | Columns | Min card width |
|------------|---------|---------------|
| `< 768px` (mobile) | 1 | 100% |
| `≥ 768px` (md) | 3 | ~280px |

---

## Animation Contract

### Entrance (page load)

| Property | Start | End | Duration | Stagger | Easing |
|----------|-------|-----|----------|---------|--------|
| `opacity` | 0 | 1 | 0.5s | 0.12s | `power2.out` |
| `y` (translateY) | 32px | 0 | 0.5s | 0.12s | `power2.out` |

Trigger: after `DOMContentLoaded`, wrapped in `gsap.matchMedia()` non-reduced branch.

**Reduced-motion branch**: `gsap.set('.nav-card', { autoAlpha: 1 })` — cards appear instantly at full opacity.

### Hover (pointer devices only — `(hover: hover) and (pointer: fine)`)

| Event | Tween | Duration |
|-------|-------|----------|
| `mouseenter` | `y: -6, scale: 1.03, boxShadow: '0 16px 40px rgba(79,70,229,0.3)'` | 0.25s |
| `mouseleave` | `y: 0, scale: 1, boxShadow: '...'` | 0.25s |

Hover bindings must use `overwrite: 'auto'` to prevent animation stacking on rapid mouse movements.

---

## Accessibility Contract

| Requirement | Implementation |
|-------------|---------------|
| Keyboard navigation | All cards are native `<a>` elements; Tab key cycles through them |
| Screen reader | `<h2>` inside each card provides semantic label; no `aria-label` needed |
| Color contrast | Text on dark background meets WCAG AA (Tailwind `slate-100` on `bg-white/5`) |
| No motion | `prefers-reduced-motion: reduce` suppresses all GSAP tweens |

---

## Color & Typography

Follows existing site palette (matching `betting.html`):

| Token | Value |
|-------|-------|
| Page background | `bg-slate-950` |
| Card background | `bg-white/5` |
| Card border | `border-white/10` |
| Primary text | `text-slate-100` |
| Secondary text | `text-slate-400` |
| Accent | `text-indigo-400` |
| Font | Noto Sans TC (Google Fonts CDN), fallback `sans-serif` |

---

## Non-Goals (explicitly out of scope)

- Search or filtering of destination pages.
- User-configurable card order or favorites.
- Dark/light mode toggle (already dark-only).
- Analytics or click tracking.
