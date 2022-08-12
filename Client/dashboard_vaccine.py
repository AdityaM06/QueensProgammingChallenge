from tkinter import *
import window
import dashboard_healthcard


# Function which displays the vaccine tab
def vaccine_tab():
    # Setting window title
    window.window.title('Vaccines')

    # Creating a canvas within the window to place items onto
    window.canvas = Canvas(
        window.window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    window.canvas.place(x=0, y=0)

    # Adding "myHealth Dashboard" text to top left
    window.canvas.create_text(
        106.0,
        52.99999999999999,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 52 * -1)
    )

    # Creating information tab button on top
    global healthcard_button_image
    healthcard_button_image = PhotoImage(
        file='assets/healthcard_button.png')
    healthcard_button = Button(
        image=healthcard_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=dashboard_healthcard.dashboard,
        relief="flat"
    )
    healthcard_button.place(
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
        command=None,
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
        x=107.31511688232422,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating the table
    global vaccine_table_image
    vaccine_table_image = PhotoImage(
        file='assets/vaccine_table.png')
    window.canvas.create_image(106,200,anchor="nw",image=vaccine_table_image)

    # Adding legend
    window.canvas.create_text(
        1280//2,
        695,
        anchor="center",
        text="A dot symbolizes upcoming, a checkmark symbolizes completed",
        fill="#FF8888",
        font=("Inter", 15)
    )

