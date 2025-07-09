import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20, border = 10,)
qr.add_data("https://www.google.co.uk/")   #Enter your link here
qr.make(fit=True )
img=qr.make_image(fill_color="pink", back_color="Black")
img.save("image.png")