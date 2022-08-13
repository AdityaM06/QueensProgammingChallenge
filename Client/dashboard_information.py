from tkinter import *
import window
import functions
import protocol
from networking import run_background

# Variables
last_name = 'Last name: '
first_name = 'First name: '
middle_name = 'Middle mame: '
date_of_birth = 'Date of birth: '
age = 'Age: '
address = 'Address: '
phone_number = 'Phone number: '
height = 'Height: '
weight = 'Weight: '
BMI = 'BMI: '
current_prescriptions = []
current_prescriptions_str = 'Current prescriptions: '
current_medical_conditions = []
current_medical_conditions_str = 'Current medical conditions: '
family_medical_history = []
family_medical_history_str = 'Family medical history: '

# Function which displays the information dashboard window
def dashboard_information():
    # Setting the window
    functions.create_canvas()

    # Adding the tabs
    functions.draw_tabs()

    # Image for edit icon
    global edit_button_image
    edit_button_image = PhotoImage(file='assets/edit_icon.png')

    # Adding "myHealth Dashboard" text to top left
    window.canvas.create_text(
        106.0,
        52.99999999999999,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 52 * -1)
    )

    # Adding the main rectangle
    window.canvas.create_rectangle(
        107.0,
        200.0,
        1173.0,
        700.0,
        fill="#FFFFFF",
        outline="#FF8888")

    # Adding the last name text
    window.canvas.create_text(
        157.0,
        214,
        anchor="nw",
        text=last_name,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the first name text
    window.canvas.create_text(
        157.0,
        251,
        anchor="nw",
        text=first_name,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the middle name text
    window.canvas.create_text(
        157.0,
        288,
        anchor="nw",
        text=middle_name,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the date of birth text
    window.canvas.create_text(
        157.0,
        324,
        anchor="nw",
        text=date_of_birth,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the age text
    window.canvas.create_text(
        157.0,
        361,
        anchor="nw",
        text=middle_name,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the address text
    window.canvas.create_text(
        157.0,
        398,
        anchor="nw",
        text=address,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the phone number text
    window.canvas.create_text(
        157.0,
        435,
        anchor="nw",
        text=phone_number,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the height text
    window.canvas.create_text(
        157.0,
        472,
        anchor="nw",
        text=height,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the weight text
    window.canvas.create_text(
        157.0,
        508,
        anchor="nw",
        text=weight,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the BMI text
    window.canvas.create_text(
        157.0,
        545,
        anchor="nw",
        text=BMI,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the current prescriptions text
    window.canvas.create_text(
        157.0,
        582,
        anchor="nw",
        text=current_prescriptions_str,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the current medical conditions text
    window.canvas.create_text(
        157.0,
        619,
        anchor="nw",
        text=current_medical_conditions_str,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

    # Adding the family medical history text
    window.canvas.create_text(
        157.0,
        656,
        anchor="nw",
        text=family_medical_history_str,
        fill="#FF8888",
        font=("Inter Medium", 20)
    )

