# Project 6 : Countdown Timer,
# Created By Huzaifa Ghouri (419013)

import time
def countdown_timer(seconds):

    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(time_format, end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00 \nTime's Up")

try:
    total_seconds = int(input("Enter the countdown time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Invalid input. Please enter an integer.")