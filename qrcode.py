import os
import qrcode
import sys
sys.path.insert(1, '../python-qrcode')


url = sys.argv[1]

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
print("Created qrcode to url: " + url)

img = qr.make_image(fill_color="black", back_color="white")
img = img.save("_qrcode.png")