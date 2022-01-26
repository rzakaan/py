import qrcode
data = input("> ")
img = qrcode.make(data)
img.save("qrcode.png")