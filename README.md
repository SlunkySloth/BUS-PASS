# Student Transport Registration frontend

An editable recovery of the supplied transport registration frontend, with the original assets and verified visual match. See [frontend/README.md](frontend/README.md) for local editing and recovery details.

## Deploy to Vercel

1. In Vercel, choose **Add New → Project**, then import **SlunkySloth/BUS-PASS**.
2. Use the repository root as **Root Directory** (leave it empty or `.`). Choose **Other** as the framework preset. The root `vercel.json` selects `frontend/dist` as the output directory and disables installation and builds; no build is needed.
3. Choose a project name and click **Deploy**. Use the project's stable production domain, such as `your-project.vercel.app`, for sharing and QR codes.

The public page URL has this format:

```text
https://YOUR-PROJECT.vercel.app/srmtrichystudentportal/students/report/studentTransportBookingVerify.jsp?token=YOUR-TOKEN
```

The path and query format mirror the original page. The hostname is your own Vercel domain or a custom domain you control. The `.jsp` page is static HTML here; `vercel.json` supplies the HTML content type so it opens in the browser. The token parameter is preserved in the address but does not perform backend validation or select a different student record.

This deployment publishes only `frontend/dist`; the receipt PDF, source archive, and visual verification files outside that directory are not part of the hosted site.

## Generate the QR code after deployment

Use the actual production address after the deployment succeeds:

```sh
python -m venv .venv-qr
.venv-qr/bin/python -m pip install -r requirements-qrcode.txt
.venv-qr/bin/python tools/generate_qr.py https://YOUR-PROJECT.vercel.app
```

The generator adds the transport page path and a fresh URL token, then saves `qr-code/transport-qr.png`, `qr-code/transport-qr.svg`, and `qr-code/transport-url.txt`. Supplying an existing full transport URL preserves its token. The SVG is suitable for printing at any size. Check the URL on a phone before printing the QR code. If your Vercel project requires visitors to sign in, adjust deployment protection for the intended public production site.
