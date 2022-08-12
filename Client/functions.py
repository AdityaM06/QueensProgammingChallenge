import re, protocol, base64
from io import BytesIO
from PIL import Image


""" https://www.c-sharpcorner.com/article/how-to-validate-an-email-address-in-python/ """
def check_email(email):
    if len(email) > 25: return protocol.TOO_LONG
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    return protocol.VALID_INPUT if re.search(regex, email) else protocol.INVALID_INPUT

""" https://stackoverflow.com/questions/89909/how-do-i-verify-that-a-string-only-contains-letters-numbers-underscores-and-da """
def check_password(password):
    if len(password) > 20: return protocol.TOO_LONG
    regex = "^[A-Za-z0-9!@#$%&]+$"
    return protocol.VALID_INPUT if re.search(regex, password) else protocol.INVALID_INPUT

""" Returns PIL Image from base64 string """
def base64_to_Image(data : str):
    im_bytes = base64.b64decode(data.encode())   # im_bytes is a binary image
    im_file = BytesIO(im_bytes)                  # convert image to file-like object
    return Image.open(im_file)                   # img is now PIL Image object


""" Return base64 string from PIL image"""
def Image_to_base64(img):
    img = img.convert('RGB')
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()
    im_b64 = base64.b64encode(im_bytes)
    return im_b64.decode()