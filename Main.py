import config
import Login
import Register
from tkinter import *

config.window = Tk()

config.window.geometry("500x600")
config.window.configure(bg = "white")


config.canvas = Canvas(
    config.window,
    bg = "white",
    height = 600,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

Login.login()

config.window.resizable(True, True)
config.window.mainloop()
