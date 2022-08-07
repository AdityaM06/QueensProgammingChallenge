from tkinter import *
import window


def dashboard():
    window.window.destroy()

    window.window = Tk()

    window.window.geometry("1280x720")
    window.window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window.window,
        bg = "#FFFFFF",
        height = 1080,
        width = 1920,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        150.0,
        30.0,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 80 * -1)
    )

    canvas.create_rectangle(
        150.0,
        413.0,
        1000.0,
        963.0,
        fill="#FFFFFF",
        outline="#FF8888")

    canvas.create_text(
        434.0,
        318.0,
        anchor="nw",
        text="Health Card",
        fill="#FF8888",
        font=("Inter Regular", 50 * -1)
    )

    canvas.create_rectangle(
        1187.0,
        413.0,
        1713.0,
        963.0,
        fill="#FFFFFF",
        outline="#FF8888")

    canvas.create_text(
        1256.0,
        318.0,
        anchor="nw",
        text="Emergency Info",
        fill="#FF8888",
        font=("Inter Regular", 50 * -1)
    )

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
        x=1367.0,
        y=140.0,
        width=405.0,
        height=90.0
    )


    global vaccine_button_image
    vaccine_button_image = PhotoImage(
        file='assets/vaccine_button.png')
    vaccine_button = Button(
        image=vaccine_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    vaccine_button.place(
        x=962.0,
        y=140.0,
        width=405.0,
        height=90.0
    )


    global appointments_button_image
    appointments_button_image = PhotoImage(
        file='assets/appointment_button.png')
    appointments_button = Button(
        image=appointments_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    appointments_button.place(
        x=557.0,
        y=140.0,
        width=405.0,
        height=90.0
    )

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
        x=152.0,
        y=140.0,
        width=405.0,
        height=90.0
    )

    canvas.create_text(
        1782.0,
        1036.0,
        anchor="nw",
        text="Upload",
        fill="#FF8888",
        font=("Inter Regular", 20 * -1)
    )

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
        x=1782.0,
        y=942.0,
        width=88.0,
        height=88.0
    )
    window.window.resizable(True, True)
    window.window.mainloop()
