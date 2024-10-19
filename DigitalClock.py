from tkinter import *  # Importing tkinter for GUI components
import time  # Importing time to get system time

# Creating the main window
window = Tk()
window.title("Digital Clock")  # Setting the window title
window.geometry("600x400")  # Setting the size of the window
window.config(bg="black")  # Setting a dark background color for the window

def myTime():
    # Fetching the current hour, minute, second, AM/PM, day, and timezone
    hour = time.strftime("%I")  # Hour in 12-hour format
    minute = time.strftime("%M")  # Minute
    second = time.strftime("%S")  # Second
    am_pm = time.strftime("%p")  # AM or PM
    day = time.strftime("%A")  # Full weekday name (e.g., Monday)
    zone = time.strftime("%Z")  # Timezone name (e.g., UTC, IST)

    # Creating formatted strings for time and day
    mytext = hour + ":" + minute + ":" + second + " " + am_pm  # Time with AM/PM
    mytext2 = day + ", " + zone  # Day and Timezone

    # Updating the labels with the new time and day information
    mylabel.config(text=mytext)
    mylabel2.config(text=mytext2)

    # Call this function every 1000 milliseconds (1 second) to update the time
    mylabel.after(1000, myTime)

# Creating the main label to display the time with a digital font
mylabel = Label(window, text="", font=("Digital-7", 72), fg="cyan", bg='black')  # Using a digital style font
mylabel.pack(pady=20)  # Pack with padding for better layout

# Creating the secondary label to display the day and timezone
mylabel2 = Label(window, text="", font=("Arial", 24), fg="light gray", bg='black')  # Softer color for the day and timezone
mylabel2.pack(pady=10)  # Pack with padding for spacing

# Initial call to start the time update function
myTime()

# Running the tkinter main loop to keep the window active
window.mainloop()
