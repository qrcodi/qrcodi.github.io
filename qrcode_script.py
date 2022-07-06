import qrcode
from PIL import Image
import PIL

img = qrcode.make("https://www.qrcodi.com/7iks/pages/menu2.html")
type(img)  # qrcode.image.pil.PilImage
img.save("_qrcode.png")