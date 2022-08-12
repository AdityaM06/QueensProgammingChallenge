import re, protocol, base64
from tkinter import *
from io import BytesIO
from PIL import Image
import dashboard_vaccine, dashboard_healthcard


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

def draw_tabs():
    # Creating information tab button on top
    global healthcar_button_image
    healthcar_button_image = PhotoImage(
        file='assets/healthcard_button.png')
    healthcard_button = Button(
        image=healthcar_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=None,
        relief="flat"
    )
    healthcard_button.place(
        x=107.31511688232422,
        y=125.3313980102539,
        width=266.31109619140625,
        height=59.18022918701172
    )

    # Creating vaccine tab button on top
    global vaccine_button_image
    vaccine_button_image = PhotoImage(
        file='assets/vaccine_button.png')
    vaccine_button = Button(
        image=vaccine_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=dashboard_vaccine.vaccine_tab,
        relief="flat"
    )
    vaccine_button.place(
        x=639.9371948242188,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating appointments tab button on top
    global appointments_button_image
    appointments_button_image = PhotoImage(
        file='assets/appointments_button.png')
    appointments_button = Button(
        image=appointments_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    appointments_button.place(
        x=373.62615966796875,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating records tab button on top
    global information_button_image
    information_button_image = PhotoImage(
        file='assets/information_button.png')
    information_button = Button(
        image=information_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    information_button.place(
        x=906.2482299804688,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )
