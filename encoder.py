import pyqrcode
import png

#  from pyqrcode import QRCode


#  Text which is to be converted to QR code

print("Enter text to convert")
s = input(": ")
# Name of  QR code png file
print("Enter image name to save")
n = input(": ")
# Adding extension os pnf/png
print("Enter Size of image to scale, Default is 10px : ")
size = input(": ")
d = n + ".png"
# create qr code
url = pyqrcode.create(s)
# Saving code as a png file
# feature to pick specific size

url.png(d, scale =size)
