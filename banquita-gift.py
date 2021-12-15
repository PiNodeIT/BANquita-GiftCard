# Python Script for generate BANquita-themed BANANO GiftCard
# Version 0.2
# Author Monk3yBanano | BanaoPiNode

# Import QR Code ad Pillow library
import qrcode
from PIL import Image
import os
import base64
from pathlib import Path
from argparse import ArgumentParser
import nanolib
from cursed_image_string import b64img


def save_qrcode(data: str, size: "tuple[int, int]", name: str, is_deposit: bool = False) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image()
    qr_img = img.resize(size)

    if is_deposit:
        qr_img.save("./GiftCard/" + (name) + "_DEPOSIT.png", quality=95)
    else:
        qr_img.save((name) + ".png")


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--seed",
        dest="seed",
        nargs="?",
        const=None,
        help="(optional) Seed for the gift account",
    )
    parser.add_argument(
        "-n",
        "--name",
        dest="name",
        nargs="?",
        default="BANquita",
        help="(optional) output filename",
    )
    args = parser.parse_args()
    seed, name = args.seed, args.name

    if not seed:
        seed = nanolib.generate_seed()
    else:
        nanolib.validate_seed(seed)

    save_qrcode(seed, (80, 80), name)

    # generate bg image
    imgdata = base64.b64decode(b64img)
    bg_temp_file = "bg.png"
    with open(bg_temp_file, "wb") as f:
        f.write(imgdata)

    # Merge QRCode on BG Image
    bg = Image.open("bg.png")
    qr_code = Image.open((name) + ".png")
    cp_bg = bg.copy()
    cp_bg.paste(qr_code, (344, 5))

    # Create GiftCard folder if not exist
    Path("./GiftCard").mkdir(parents=True, exist_ok=True)

    # Save GiftCard on "GiftCard" folder
    cp_bg.save("./GiftCard/" + (name) + "_GiftCard.png", quality=95)

    # Remove Temp QRCode file
    os.remove((name) + ".png")

    # Remove Temp BG file
    os.remove("bg.png")

    deposit = nanolib.generate_account_id(seed, 0).replace("xrb_", "ban_")
    save_qrcode(deposit, (300, 300), name, is_deposit=True)


if __name__ == "__main__":
    main()
