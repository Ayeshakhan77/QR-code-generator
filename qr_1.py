import qrcode as qr

img= qr.make("https://www.google.co.uk/")
img.save("image.png")