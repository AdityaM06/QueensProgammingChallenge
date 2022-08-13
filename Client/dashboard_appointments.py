from tkinter import *
from datetime import datetime
import window
import functions
import protocol
from networking import run_background

appointments_list = []
appointment_x = None
appointment_y = None
y_increment = None
add_appointment_window = None


# Function which adda an appointment to the appointments list
def add_appointment(name: str, date: str):
    # Adding appointment to the list
    appointments_list.append({'name': name, 'date': date})

    # Sorting list by date recently
    appointments_list.sort(key=lambda x: datetime.strptime(x['date'], "%Y/%m/%d %H:%M"))
    appointments_list.reverse()


# Function which verifies the user inputs for the date and time
def date_verify():
    # Resetting error messages
    error_text.config(text='')
    date_time_str = date_time.get()
    title_str = title.get()

    # Verify proper date
    match (functions.check_date(date_time_str)):
        case protocol.INVALID_INPUT:
            # Invalid
            error_text.config(text='Incorrect format or incorrect date, please enter a valid date')
            return
        case protocol.VALID_INPUT:
            pass

    add_appointment(title_str, date_time_str)
    add_appointment_window.destroy()
    dashboard_appointments()


# Function to make a new window to add an appointment
def add_appointment_window():
    global add_appointment_window

    add_appointment_window = Toplevel(window.window)
    add_appointment_window.title('Add Appointment')
    add_appointment_window.geometry("500x600")
    add_appointment_window.configure(bg="white")

    global date_time, title
    date_time = StringVar()
    title = StringVar()

    # Mock Window
    canvas = Canvas(
        add_appointment_window,
        bg="#FFFFFF",
        height=600,
        width=500,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    # Add appointment text
    canvas.create_text(
        40.0,
        50.0,
        anchor="nw",
        text="Add Appointment",
        fill="#FF8888",
        font=("Inter Medium", 50 * -1)
    )

    # Adding format text
    canvas.create_text(
        50.0,
        239.0,
        anchor="nw",
        text="Please format yyyy/mm/dd HH:MM (24h time)",
        fill="#FF8888",
        font=("Inter Medium", 15)
    )

    # Adding the add button
    global add_button_image
    add_button_image = PhotoImage(
        file='assets/add_button.png')
    add_button = Button(
        add_appointment_window,
        image=add_button_image,
        borderwidth=0,
        highlightthickness=0,
        command=date_verify,
        relief="flat"
    )
    add_button.place(
        x=50.0,
        y=500.0,
        width=400.0,
        height=50.0
    )

    # Adding the date and time entry field
    global date_time_entry_image
    date_time_entry_image = PhotoImage(
        file='assets/date_time_entry.png')
    canvas.create_image(
        (50, 163),
        anchor="nw",
        image=date_time_entry_image
    )
    date_time_entry = Entry(
        add_appointment_window,
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=date_time
    )
    date_time_entry.place(
        x=60.0,
        y=190.0,
        width=380.0,
        height=30.0
    )

    # Adding the title entry field
    global title_entry_field_image
    title_entry_field_image = PhotoImage(
        file='assets/title_entry.png')
    canvas.create_image(
        (50, 332),
        anchor="nw",
        image=title_entry_field_image
    )
    title_entry = Entry(
        add_appointment_window,
        bd=0,
        bg="#FFFFFF",
        fg='black',
        font=('Inter', '20'),
        highlightthickness=0,
        textvariable=title
    )
    title_entry.place(
        x=60.0,
        y=359.0,
        width=380.0,
        height=30.0
    )

    global error_text
    error_text = Label(add_appointment_window, text='', fg='red', bg='white')
    error_text.place(x=50, y=141)


# Main screen for appointments
def dashboard_appointments():
    # Clearing the window
    window.canvas.delete(all)

    # Setting window title
    window.window.title('Appointments')

    # Creating a canvas within the window to place items onto
    window.canvas = Canvas(
        window.window,
        bg="#FFFFFF",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    window.canvas.place(x=0, y=0)

    # Adding the tabs
    functions.draw_tabs()

    # Adding "myHealth Dashboard" text to top left
    window.canvas.create_text(
        106.0,
        52.99999999999999,
        anchor="nw",
        text="myHealth Dashboard",
        fill="#FF8888",
        font=("Inter Medium", 52 * -1)
    )

    # Adding the suggestions table
    global suggestions_schedule_image
    suggestions_schedule_image = PhotoImage(
        file='assets/suggestions_rectangle.png')
    window.canvas.create_image(797, 215, anchor="nw", image=suggestions_schedule_image)

    # Creating rectangle for upcoming appointments
    window.canvas.create_rectangle(
        106.0,
        215.0,
        719.0,
        690.0,
        fill="#FFFFFF",
        outline="#FF8888")
    # Adding appointments
    window.canvas.create_text(
        126.0,
        235,
        anchor="nw",
        text="Upcoming:",
        fill="#FF8888",
        font=("Inter Medium", 26)
    )

    global appointment_x, appointment_y, y_increment
    appointment_x = 176
    appointment_y = 283
    y_increment = 25

    for item in appointments_list:
        date = datetime.strptime(item['date'], "%Y/%m/%d %H:%M").date()
        window.canvas.create_text(
            appointment_x,
            appointment_y,
            anchor="nw",
            text=item['name'] + ' at ' + date.strftime('%a, %b %-m %Y %-I:%M%p'),
            fill="#FF8888",
            font=("Inter Medium", 20)
        )
        appointment_y += y_increment

    # Adding the add appointment button
    global add_appointment_image
    add_appointment_image = PhotoImage(
        file='assets/plus_button.png')
    plus_button = Button(
        image=add_appointment_image,
        borderwidth=0,
        highlightthickness=0,
        command=add_appointment_window,
        relief="flat"
    )
    plus_button.place(
        x=126,
        y=620,
        width=50,
        height=50
    )
