import qrcode
img = qrcode.make("https://www.qrcodi.com/7iks/pages/menu2.html")
type(img)  # qrcode.image.pil.PilImage
img.save("_qrcode.png")