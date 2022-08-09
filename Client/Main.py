import config, window
import login, register, fail_window
from tkinter import *
from networking import Network, MockNetwork, run_background

# Creating the window
window.window = Tk()
window.window.title('Sign In')

# Configure window dimensions
WIDTH, HEIGHT = config.WIDTH, config.HEIGHT
window.window.geometry(f"{WIDTH}x{HEIGHT}")
window.window.configure(bg = "white")

# Mock Window
window.canvas = Canvas(
    window.window,
    bg="#FFFFFF",
    height=config.HEIGHT,
    width=config.WIDTH,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

# Thread for networking
config.NET = Network() #MockNetwork( True | False )
run_background ( config.NET.connect_to, *('localhost', 9848) )

# Wait for a response
while (config.NET.status == 0): pass

# Process response
if (config.NET.status == 1):

    # Failed, show fail screen
    fail_window.fail_window()

elif (config.NET.status == 2):

    # Starting Screen
    login.login()


# Start program
window.window.resizable(False, False)
window.window.mainloop()
