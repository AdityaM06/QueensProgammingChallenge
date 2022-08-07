import config, window
from tkinter import *

def fail_window():
    window.canvas = Canvas(
        window.window,
        bg="#FFFFFF",
        height=config.HEIGHT,
        width=config.WIDTH,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    Label(window.window, text='Failed to\nConnect!', fg='#ff8787', bg='white', font="MS_Sans_Serif 40").place(x=config.WIDTH//2, y=config.HEIGHT//2, anchor="center")
