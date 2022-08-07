from tkinter import *
import config, window, login
import traceback

# Function to register a user to a file
def register_user():
    username = window.username_verify.get()
    password = window.password_verify.get()

    print(f"[REGISTER] User: {username}    Pass: {password}")

    """
    Label(window.window, text='Sucuessfuly registered', bg='white', fg='green', font=('Calibri', 12)).pack()
    """


# Function for registration screen
def register():
    window.username_verify = StringVar()
    window.password_verify = StringVar()

    window.canvas.destroy()
    window.canvas = Canvas(
        window.window,
        bg="#FFFFFF",
        height=config.HEIGHT,
        width=config.WIDTH,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    window.canvas.place(x=0, y=0)

    window.canvas.create_text(
        50.0,
        50.0,
        anchor="nw",
        text="REGISTER",
        fill="#FF8787",
        font=("Inter Medium", 50 * -1)
    )
    global register_button_img
    register_button_img = PhotoImage(
        file='assets/register_button.png')
    register_btn = Button(
        image=register_button_img,
        borderwidth=0,
        highlightthickness=0,
        command=register_user,
        relief="flat"
    )
    register_btn.place(
        x=50.0,
        y=450.0,
        width=400.0,
        height=50.0
    )

    global or_sign_in_button_img
    or_sign_in_button_img = PhotoImage(
        file='assets/or_sign_in_button.png')
    or_sign_in_btn = Button(
        image=or_sign_in_button_img,
        borderwidth=0,
        highlightthickness=0,
        command=login.login,
        relief="flat"
    )
    or_sign_in_btn.place(
        x=197.0,
        y=520.0,
        width=107.0,
        height=24.0
    )

    global pass_entry_image
    pass_entry_image = PhotoImage(
        file='assets/pass_entry.png')
    window.canvas.create_image(
        250.0,
        343.0,
        image=pass_entry_image
    )
    window.password_entry = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=window.password_verify
    )
    window.password_entry.place(
        x=60.0,
        y=333.0,
        width=300.0,
        height=30.0
    )
    global user_entry_image
    user_entry_image = PhotoImage(
        file='assets/user_entry.png')
    window.canvas.create_image(
        250.0,
        198.0,
        image=user_entry_image
    )
    window.username_entry = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=window.username_verify
    )
    window.username_entry.place(
        x=60.0,
        y=185.0,
        width=300.0,
        height=30.0
    )
