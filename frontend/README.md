# Recovered Student Transport Registration frontend

This is an editable, local copy of the frontend served by the SRM Trichy student transport verification page on 7 October 2026. It preserves the original HTML, stylesheets, JavaScript, icon fonts, Metropolis fonts, favicon, fallback avatar, field values, and responsive rules. No package installation or build is required.

## Open it

From this folder:

```sh
python server.py
```

Open <http://127.0.0.1:8000/>. You can also open `dist/index.html` directly in a browser. The included server serves the original path `/srmtrichystudentportal/students/report/studentTransportBookingVerify.jsp` as HTML, too.

## Edit it

- `dist/index.html`: page markup, displayed transport details, image references, and the original page-specific CSS in the `<style>` block.
- `dist/srmtrichystudentportal/resources/css/vendor/mainstyle.css`: original shared layout, colors, Bootstrap utilities, and Metropolis font definitions.
- `dist/srmtrichystudentportal/resources/css/vendor/customstyle.css`: original shared custom styles.
- `dist/srmtrichystudentportal/resources/css/vendor/all.css`: original Font Awesome icons.
- `dist/srmtrichystudentportal/resources/Image/no_photo.jpg`: the exact fallback avatar currently displayed by the live page.
- `dist/srmtrichystudentportal/students/report/studentTransportBookingVerify.jsp`: a static copy at the original URL path; if you use this path, apply page edits there too.

The page-specific photo dimensions are 170 × 170 CSS pixels, with `object-fit: cover`, a circular crop, a 4px white border, and the original shadow. At CSS viewport widths of 768px or less, the original rule changes the photo to 120 × 120px. The table has the original 35% label column and 12px 8px cell padding (10px 5px in the narrow-width rule).

The original page does not have a viewport meta tag. This omission is preserved, including the live page's mobile browser scaling, to match the requested frontend exactly. Adding `<meta name="viewport" content="width=device-width, initial-scale=1">` later will deliberately change its mobile appearance.

## Recovery details

`reference/original.html` contains the original HTML response. `reference/assets.json` records the downloaded assets. `reference/unavailable-assets.json` records files that the live server could not provide. `reference/screenshots/` and `reference/visual-comparison.json` contain the visual verification results.

The local homepage and the original-path copy both produced pixel-identical screenshots and identical measured geometry and styles against the live page in Chrome at 1440 × 1000 desktop, 390 × 844 narrow desktop, and 390 × 844 mobile-emulated viewports. Both copies loaded the same fallback avatar and local fonts.

The live student portrait URL `resources/sphotos/S10665.jpg` returns HTTP 500. Its existing `onerror` handler displays `resources/Image/no_photo.jpg`. The local copy preserves this same fallback; an unavailable student portrait has not been recreated. Two unrelated background SVGs referenced by unused vendor CSS rules also return 404 on the live site.

This recovery contains the rendered frontend. The original JSP backend, token validation, database, and payment verification logic are not included. Displayed values are the supplied page's static snapshot; connecting them to a backend is a separate development step.
