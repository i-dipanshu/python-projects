# pip install qrcode

import qrcode as qr
image = qr.make("https://github.com/i-dipanshu/python-projects")
image.save("mygithub.png")

