from tkinter import *
import window
import dashboard_vaccine


# Function which displays the dashboard window
def dashboard():
    # Setting window title
    window.window.title('Information')

    # Creating a canvas within the window to place items onto
    window.canvas = Canvas(
        window.window,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    window.canvas.place(x = 0, y = 0)

    # Adding "myHealth Dashboard" text to top left
    window.canvas.create_text(
        106.0,
        52.99999999999999,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 52 * -1)
    )

    # Creating health card slot
    window.canvas.create_rectangle(
        106.0,
        304.84478759765625,
        664.9244384765625,
        666.5017700195312,
        fill="#FFFFFF",
        outline="#FF8888")

    window.canvas.create_text(
        292.74652099609375,
        242.37673950195312,
        anchor="nw",
        text="Health Card",
        fill="#FF8888",
        font=("Inter Regular", 32 * -1)
    )

    # Creating additional text box
    window.canvas.create_rectangle(
        770.0,
        305.0,
        1173.0,
        667.0,
        fill="#FFFFFF",
        outline="#FF8888")

    window.canvas.create_text(
        850.0,
        242.0,
        anchor="nw",
        text="Emergency Info",
        fill="#FF8888",
        font=("Inter Regular", 32 * -1)
    )

    # Creating information tab button on top
    global information_button_image
    information_button_image = PhotoImage(
        file='assets/information_button.png')
    information_button = Button(
        image=information_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    information_button.place(
        x=906.2482299804688,
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
    global records_button_image
    records_button_image = PhotoImage(
        file='assets/records_button.png')
    records_button = Button(
        image=records_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    records_button.place(
        x=107.31511688232422,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating upload button to upload healthcard
    global upload_button_image
    upload_button_image = PhotoImage(
        file='assets/upload_button.png')
    upload_button = Button(
        image=upload_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    upload_button.place(
        x=29.0,
        y=616.0,
        width=57.8651123046875,
        height=57.8651123046875
    )
    window.canvas.create_text(
        34.8651123046875,
        674.3070068359375,
        anchor="nw",
        text="Upload",
        fill="#FF8888",
        font=("Inter Regular", 13 * -1)
    )
