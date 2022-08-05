from tkinter import *
from PIL import ImageTk, Image
import os
import config
import Login


# Function to register a user to a file
def register_user():
    username_info = config.username.get()
    password_info = config.password.get()

    # Saving username and password to file
    f = open('users/' + str(username_info), 'w')
    f.write(username_info + '\n')
    f.write(password_info)
    f.close()

    # Clearing the entry field
    config.username_entry.delete(0, END)
    config.password_entry.delete(0, END)

    # Confimring registration
    Label(config.window, text='Sucuessfuly registered', bg='white', fg='green', font=('Calibri', 12)).pack()


# Function for registration screen
def register():
    config.username = StringVar()
    config.password = StringVar()

    config.canvas.destroy()
    config.canvas = Canvas(
        config.window,
        bg="#FFFFFF",
        height=600,
        width=500,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    config.canvas.place(x=0, y=0)

    config.canvas.create_text(
        50.0,
        50.0,
        anchor="nw",
        text="REGISTER",
        fill="#FF8787",
        font=("Inter Medium", 50 * -1)
    )
    global button_image_1
    button_image_1 = PhotoImage(
        file='assets/register_button.png')
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=register_user,
        relief="flat"
    )
    button_1.place(
        x=50.0,
        y=450.0,
        width=400.0,
        height=50.0
    )
    global button_image_2
    button_image_2 = PhotoImage(
        file='assets/Or_Sign_In_Button.png')
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Login.login,
        relief="flat"
    )
    button_2.place(
        x=197.0,
        y=520.0,
        width=107.0,
        height=24.0
    )
    global entry_image_1
    entry_image_1 = PhotoImage(
        file='assets/entry_1.png')
    entry_bg_1 = config.canvas.create_image(
        250.0,
        343.0,
        image=entry_image_1
    )
    config.password_entry = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=config.password
    )
    config.password_entry.place(
        x=60.0,
        y=333.0,
        width=300.0,
        height=30.0
    )
    global entry_image_2
    entry_image_2 = PhotoImage(
        file='assets/entry_2.png')
    entry_bg_2 = config.canvas.create_image(
        250.0,
        198.0,
        image=entry_image_2
    )
    config.username_entry = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=config.username
    )
    config.username_entry.place(
        x=60.0,
        y=185.0,
        width=300.0,
        height=30.0
    )
