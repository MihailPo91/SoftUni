import pyqrcode
import png
from pyqrcode import QRCode

link = "https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11623319714326143&slink=lpcb8n"
url = pyqrcode.create(link)
url.png("qr_code.png", scale=8)
