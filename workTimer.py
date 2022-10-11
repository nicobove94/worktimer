import tkinter as tk
from tkinter import *
import time
import datetime

# Function that creates a window when the timer is complete
def window(n):
    m = tk.Tk()
    m.geometry("750x270")
    
    if int(n) == 0:
        text = Label(m, text = "Working period has completed, begin break.", font=('Helvetica 20 bold')).pack()
    elif int(n) == 1:
        text = Label(m, text = "Break period has completed, resume work.", font=('Helvetica 20 bold')).pack()

    m.mainloop()

# Create class that acts as a countdown
def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
 
    #print("Bzzzt! The countdown is at zero seconds!")
    
# Inputs for hours, minutes, seconds on timer
print("FOR THE WORK PERIOD:")
h = input("Enter the time in hours: ")
m = input("Enter the time in minutes: ")
s = input("Enter the time in seconds: ")
print("FOR THE BREAK PERIOD")
h1 = input("Enter the time in hours: ")
m1 = input("Enter the time in minutes: ")
s1 = input("Enter the time in seconds: ")

try:
    while(True):
        countdown(int(h), int(m), int(s))
        window(0)

        countdown(int(h1), int(m1), int(s1))
        window(1)
except(KeyboardInterrupt):
    print("Working period completed, have a nice day.")
