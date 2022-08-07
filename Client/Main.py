import config, window
import login
from tkinter import *

window.window = Tk()

# Configure dimensions
WIDTH, HEIGHT = config.WIDTH, config.HEIGHT
window.window.geometry(f"{WIDTH}x{HEIGHT}")
window.window.configure(bg = "white")

# Mock Window
window.canvas = Canvas(
    window.window,
    bg="#FFFFFF",
    height=config.HEIGHT,
    width=confiAddeg.WIDTH,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Starting Screen
login.login()

# Start program
window.window.resizable(False, False)
window.window.mainloop()
