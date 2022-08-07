from tkinter import *
import os
import window, config, register
import traceback

def login_verify():
    username = window.username_verify.get()
    password = window.password_verify.get()

    print(f"[LOGIN] User: {username}    Pass: {password}")
    
    """
    Label(window.window, text='Success!', fg='green', bg='white').place(x=60, y=570)
    Label(window.window, text='Incorrect password!', fg='red', bg='white').place(x=60, y=383)
    Label(window.window, text='Username not found!', fg='red', bg='white').place(x=60, y=235)
    """


def login():
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
        text="SIGN IN",
        fill="#FF8787",
        font=("Inter Medium", 50 * -1)
    )

    global sign_in_button_img
    sign_in_button_img = PhotoImage(
        file='assets/sign_in_button.png')
    sign_in_btn = Button(
        image=sign_in_button_img,
        borderwidth=0,
        highlightthickness=0,
        command=login_verify,
        relief="flat"
    )
    sign_in_btn.place(
        x=50.0,
        y=450.0,
        width=400.0,
        height=50.0
    )

    global or_register_button_img
    or_register_button_img = PhotoImage(
        file='assets/or_register_button.png')
    or_register_btn = Button(
        image=or_register_button_img,
        borderwidth=0,
        highlightthickness=0,
        command=register.register,
        relief="flat"
    )
    or_register_btn.place(
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
