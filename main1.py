import qrcode
from PIL import Image
qr=qrcode.QRcode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://anthascil.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="red")
img.save("zux_web.png")