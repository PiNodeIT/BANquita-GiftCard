# Python Script for generate BANquita-themed BANANO GiftCard
# Version 0.1
# Author Monk3yBanano | BanaoPiNode

# Import QR Code ad Pillow library
import qrcode
from PIL import Image
import os

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 1,
)

# The data that you want to store
data = input("Insert Seed:\n")
deposit = input("Insert Deposit Address (must start in ban_ ):\n")
name = input("Save as (no extension) :\n")

# Add data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image()
qr_img = img.resize((80,80))

# Temp Save QRcode
qr_img.save((name)+".png")

# Merge QRCode on BG Image
bg = Image.open('./src/bg.png')
qr_code = Image.open((name)+".png")
cp_bg = bg.copy()
cp_bg.paste(qr_code, (344, 5))

# Save GiftCard on "GiftCard" folder
cp_bg.save("./GiftCard/"+(name)+"_GiftCard.png", quality=95)

# Remove Temp QRCode file
os.remove((name)+".png")

# Create qr code instance
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 1,
)

# Add data deposit address
qr.add_data(deposit)
qr.make(fit=True)

# Create an image from the QR Code instance
dep = qr.make_image()
dep_img = dep.resize((300,300))

#Save Deposit QRcode
dep_img.save("./GiftCard/"+(name)+"_DEPOSIT.png", quality=95)
