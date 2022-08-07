from tkinter import *
import os
import config
import Register


def toggle_password_visible():
    if config.entry_1.cget('show') == '•':
        config.entry_1.config(show='')
    else:
        config.entry_1.config(show='•')


def login_verify():
    username1 = config.username_verify.get()
    password1 = config.password_verify.get()

    config.entry_1.delete(0, END)
    config.entry_2.delete(0, END)

    list_of_files = os.listdir('users/')

    if username1 in list_of_files:
        f = open('users/' + str(username1), 'r')
        verify = f.read().splitlines()

        if password1 in verify:
            Label(config.window, text='Success!', fg='green', bg='white').place(x=60, y=570)
        else:
            Label(config.window, text='Incorrect password!', fg='red', bg='white').place(x=60, y=383)
    else:
        Label(config.window, text='Username not found!', fg='red', bg='white').place(x=60, y=235)


def login():
    config.username_verify = StringVar()
    config.password_verify = StringVar()

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
        text="SIGN IN",
        fill="#FF8787",
        font=("Inter Medium", 50 * -1)
    )

    global button_image_1
    button_image_1 = PhotoImage(
        file='assets/button_1.png')
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=login_verify,
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
        file='assets/button_2.png')
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=Register.register,
        relief="flat"
    )
    button_2.place(
        x=197.0,
        y=520.0,
        width=107.0,
        height=24.0
    )

    global button_image_3
    button_image_3 = PhotoImage(
        file='assets/eye.png')
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=toggle_password_visible,
        relief="flat"
    )
    button_3.place(
        x=390.0,
        y=325.0,
        width=50,
        height=50
    )

    global entry_image_1
    entry_image_1 = PhotoImage(
        file='assets/entry_1.png')
    entry_bg_1 = config.canvas.create_image(
        250.0,
        343.0,
        image=entry_image_1
    )
    config.entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=config.password_verify
    )
    config.entry_1.place(
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
    config.entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=config.username_verify
    )
    config.entry_2.place(
        x=60.0,
        y=185.0,
        width=300.0,
        height=30.0
    )
