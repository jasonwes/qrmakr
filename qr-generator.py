import qrcode
from PIL import Image

# Set embeded image file path and open the image
embeded_image_path="/Users/jasonwessel/Documents/images/LinkedIn_icon_circle.svg.png"
embeded_image = Image.open(embeded_image_path)
# Resize embeded image
wpercent = (100/float(embeded_image.size[0]))
hsize = int((float(embeded_image.size[1])*float(wpercent)))
logo = embeded_image.resize((100, hsize), Image.ANTIALIAS)

# Create QRcode object with modifiable settings
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# Create variables to store the information
data = "https://www.linkedin.com/in/jason-wessel-275703137/"
# Encode the data or link and generated a qr code image
QRcode.add_data(data)
QRcode.make()

# Modify color of QR code
QRimg = QRcode.make_image(fill_color='Blue', back_color="white").convert('RGB')

# Paste embeded image into generated qr
pos = ((QRimg.size[0] - logo.size[0]) // 2, 
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# Save the QR Code
QRimg.save("test3.jpg")
print("Successfully generated QR code")