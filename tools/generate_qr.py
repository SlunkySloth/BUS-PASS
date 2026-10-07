"""Generate printable PNG and SVG QR codes for the deployed transport page."""

import argparse
from pathlib import Path
import secrets
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import qrcode
from qrcode.image.svg import SvgPathImage

PAGE_PATH = '/srmtrichystudentportal/students/report/studentTransportBookingVerify.jsp'


def transport_url(address):
    parts = urlsplit(address)
    if parts.scheme != 'https' or not parts.netloc or parts.username or parts.password:
        raise ValueError('Use the public HTTPS address of your deployed site.')
    if parts.hostname == 'student.srmtrichy.edu.in':
        raise ValueError('Use your own deployed domain, rather than the original SRM domain.')
    if parts.path not in ('', '/', PAGE_PATH):
        raise ValueError('Supply the site homepage or the transport verification URL.')
    parameters = dict(parse_qsl(parts.query, keep_blank_values=True))
    if not parameters.get('token'):
        parameters['token'] = secrets.token_urlsafe(24)
    return urlunsplit(('https', parts.netloc, PAGE_PATH, urlencode(parameters), ''))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('address', help='Your deployed HTTPS domain or full transport URL')
    parser.add_argument('--output', type=Path, default=Path('qr-code'))
    args = parser.parse_args()
    try:
        url = transport_url(args.address)
    except ValueError as error:
        parser.error(str(error))
    args.output.mkdir(parents=True, exist_ok=True)
    code = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=12, border=4)
    code.add_data(url)
    code.make(fit=True)
    code.make_image(fill_color='black', back_color='white').save(args.output / 'transport-qr.png')
    code.make_image(image_factory=SvgPathImage).save(args.output / 'transport-qr.svg')
    (args.output / 'transport-url.txt').write_text(url + '\n')
    print(url)
    print(f'QR files saved in {args.output.resolve()}')


if __name__ == '__main__':
    main()
