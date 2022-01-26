import io, argparse, qrcode
parser = argparse.ArgumentParser(description='Generate QR code from text.')
parser.add_argument('--text', help='Data to be written into qrcode')
parser.add_argument('--tty', action='store_true', help='Draw image into tty')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

data = ""
if args.text == None:
    data = input("> ")
else:
    data = args.text

if args.tty:
    qr = qrcode.QRCode()
    qr.add_data(data)
    f = io.StringIO()
    qr.print_ascii(out=f)
    f.seek(0)
    print(f.read())
else:
    img = qrcode.make(data)
    img.save("qrcode.png")