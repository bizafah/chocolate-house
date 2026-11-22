# The Chocolate House — Hero Only

This folder contains only the promotional strip, rounded navigation bar, and hero section inspired by the supplied reference.

## Files
- `index.html` — hero-only markup
- `styles.css` — pastel pink/yellow styling and responsive layout
- `script.js` — mobile navigation toggle
- `assets/dessert-cutouts.png` — generated transparent PNG collage of isolated brownies, cookies, truffles, a chocolate pastry and cake

## Run
Open `index.html` in a browser, or use VS Code Live Server.

## Integrating into the existing website
Copy the `<div class="promo-bar">`, `<header class="hero-header">`, and `<section class="hero">` markup into your existing page. Copy `styles.css`, `script.js`, and the `assets` folder as well. The hero button points to `#menu`; it will scroll to the menu section when integrated with the full website. The nav links similarly expect the corresponding section IDs in the full page.

The dessert image is a transparent PNG (RGBA alpha channel), not a rectangular food photograph. The generated collage is positioned as one cutout composition to match the floating-food look in the reference.
