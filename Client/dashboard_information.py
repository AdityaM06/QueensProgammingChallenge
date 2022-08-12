from tkinter import *
from tkinter import filedialog
import window
import dashboard_vaccine
from PIL import Image, ImageTk
import functions
import protocol
from networking import run_background

# For displaying images
label_image1 = None
label_image2 = None


# Change healthcard image
def uploadNewImage(image_num=-1):
    # Popup for user to select image
    filename = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("JPEG", ".jpeg")])
    if not filename: return
    if image_num == -1: return

    # Open image and resize
    image = Image.open(filename)
    image = image.resize((470, 350))
    image = image.convert('RGB')

    # Show change locally
    _image = ImageTk.PhotoImage(image)
    if image_num == 0:
        # Image #1
        window.canvas.create_image(111, 310, anchor="nw", image=_image)

    elif image_num == 1:
        # Image #2
        window.canvas.create_image(698, 310, anchor="nw", image=_image)

    # Write new data to server
    image = image.resize((470//2, 350//2))
    window.DATA[protocol.DATA_INDEXES[protocol.HEALTHCARD]] [image_num] = functions.Image_to_base64(image)
    run_background ( window.NET.updatePersonalData, window.DATA, protocol.HEALTHCARD )
    





# Function which displays the dashboard window
def dashboard():
    # Setting window title
    window.window.title('Information')

    # Creating a canvas within the window to place items onto
    window.canvas = Canvas(
        window.window,
        bg = "#FFFFFF",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    window.canvas.place(x = 0, y = 0)

    # Adding "myHealth Dashboard" text to top left
    window.canvas.create_text(
        106.0,
        52.99999999999999,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 52 * -1)
    )

    # Health card text label
    window.canvas.create_text(
        1280//2,
        247.37673950195312,
        anchor="center",
        text="Health Card",
        fill="#FF8888",
        font=("Inter Regular", 32 * -1)
    )

    # Creating health card slot for image
    window.canvas.create_rectangle(
        106.0,
        305.0,
        587.0,
        667.0,
        fill="#FFFFFF",
        outline="#FF8888")
    

    # Creating additional box for second image
    window.canvas.create_rectangle(
        693.0,
        305.0,
        1174.0,
        667.0,
        fill="#FFFFFF",
        outline="#FF8888")


    # Creating information tab button on top
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
        x=906.2482299804688,
        y=125.3313980102539,
        width=266.31109619140625,
        height=59.18022918701172
    )

    # Creating vaccine tab button on top
    global vaccine_button_image
    vaccine_button_image = PhotoImage(
        file='assets/vaccine_button.png')
    vaccine_button = Button(
        image=vaccine_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=dashboard_vaccine.vaccine_tab,
        relief="flat"
    )
    vaccine_button.place(
        x=639.9371948242188,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating appointments tab button on top
    global appointments_button_image
    appointments_button_image = PhotoImage(
        file='assets/appointments_button.png')
    appointments_button = Button(
        image=appointments_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    appointments_button.place(
        x=373.62615966796875,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating records tab button on top
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
        x=107.31511688232422,
        y=125.3313980102539,
        width=266.31103515625,
        height=59.18022918701172
    )

    # Creating upload button to upload healthcard #1
    global upload_button_image
    upload_button_image = PhotoImage(
        file='assets/upload_button.png')
    upload_button1 = Button(
        image=upload_button_image,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: uploadNewImage(image_num=0),
        relief="flat"
    )
    upload_button1.place(
        x=317.567444,
        y=220,
        width=57.8651123046875,
        height=57.8651123046875
    )
    window.canvas.create_text(
        346.5,
        280.0,
        anchor="n",
        text="Upload",
        fill="#FF8888",
        font=("Inter Regular", 13 * -1)
    )

    # Creating upload button to upload healthcard #2
    upload_button2 = Button(
        image=upload_button_image,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: uploadNewImage(image_num=1),
        relief="flat"
    )
    upload_button2.place(
        x=904.567444,
        y=220,
        width=57.8651123046875,
        height=57.8651123046875
    )
    window.canvas.create_text(
        933.5,
        280.0,
        anchor="n",
        text="Upload",
        fill="#FF8888",
        font=("Inter Regular", 13 * -1)
    )

    global label_image1, label_image2
    label_image1 = ImageTk.PhotoImage( functions.base64_to_Image ( window.DATA[protocol.DATA_INDEXES[protocol.HEALTHCARD]] [0] ).resize((470, 350)) )
    label_image2 = ImageTk.PhotoImage( functions.base64_to_Image ( window.DATA[protocol.DATA_INDEXES[protocol.HEALTHCARD]] [1] ).resize((470, 350)) )

    # Image #1
    window.canvas.create_image(
        111,
        310,
        anchor="nw",
        image=label_image1
    )

    # Image #2
    window.canvas.create_image(
        698,
        310,
        anchor="nw",
        image=label_image2
    )
