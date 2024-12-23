### This module provides a way to generate an OTP using the authenticator app 
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import logging
import pyotp
#import qrcode
from PIL import Image
import utili.secretCode as secretCode



### This function generates an otp for an existing user 
def TOTP():   
    # Create a TOTP instance with the secret key
    totp = pyotp.TOTP(secretCode.secret_key.replace(" ",""))
    otp = totp.now()
    logging.info(f"Generated OTP: {otp}")
    return otp




# ## This function creates a QR code, for authentication, for a new user
# def tfa_Setup():
#     logging.info("Scan Qr")
#     # Generate the provisioning URI
#     provisioning_uri = pyotp.totp.TOTP(secretCode.secret_key).provisioning_uri(
#         name="abdullah.waraich@uptodata.com", issuer_name="Study Gene 2FA for c003.dev.uptodata.studygen.cloud")

#     # Create a QR code from the provisioning URI
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(provisioning_uri)
#     qr.make(fit=True)
    
#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save("qr_code.png")  # Save the image to a file
#     img.show()  # Display the image (opens the default image viewer)
#     input("Press Enter to continue after scanning the QR code...")   # Wait for the user to confirm that they've scanned the QR code
#     logging.info(" Qr Scanned")
