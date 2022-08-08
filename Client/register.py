from tkinter import *
import config, window, login
import protocol

# Function to register a user to a file
def register_user():
    # Get user input
    username = window.username_verify.get()
    password = window.password_verify.get()

    # Comma and empty string check
    if "," in username or "," in password:
        Label(window.window, text='No commas allowed!', fg='red', bg='white', font="MS_Sans_Serif 14").place(x=config.WIDTH // 2, y=570, width=500, anchor="center")
    elif username == "" or password == "":
        Label(window.window, text='Email and password required!', fg='red', bg='white', font="MS_Sans_Serif 14").place(x=config.WIDTH // 2, y=570, width=500, anchor="center")
    else:
        # Send request to Server
        print(f"[REGISTER] User: {username}    Pass: {password}")
        response = config.NET.register(username, password)

        # Process response
        if response == protocol.REGISTER_SUCCESS:
            # Display error to user
            Label(window.window, text='Successfully Registered! Please Sign in', fg='green', bg='white', font="MS_Sans_Serif 20").place(x=config.WIDTH//2, y=570, anchor="center")
        elif response == protocol.REGISTER_FAIL:
            Label(window.window, text='Failed to Register, account already exists?', fg='red', bg='white', font="MS_Sans_Serif 16").place(x=config.WIDTH//2, y=570, anchor="center")
            pass

def toggle_password_visible():
    if window.password_entry.cget('show') == '•':
        window.password_entry.config(show='')
    else:
        window.password_entry.config(show='•')

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

    global eye_button_image
    eye_button_image = PhotoImage(
        file='assets/eye.png')
    password_toggle_button = Button(
        image=eye_button_image,
        borderwidth=0,
        background="white",
        highlightthickness=0,
        command=toggle_password_visible,
        relief="flat"
    )
    password_toggle_button.place(
        x=390.0,
        y=325.0,
        width=50,
        height=50
    )
