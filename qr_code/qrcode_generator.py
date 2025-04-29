import qrcode
import re


def generateQR():
    info = input("Please enter information to generate qr code: ")
    img = qrcode.make(info)
    save_info = re.sub(r"[^\w\s]", "_", info)
    print(save_info)
    img.save(f"qr_code_data/{save_info}.png")
    # img.show()


if __name__ == "__main__":
    while True:
        task = int(input("Want to make QR code? (1-YES / 0-NO)"))
        if task == 1:
            generateQR()
            print("Your QR code is saved")
        else:
            break

    print("Thank you!")
