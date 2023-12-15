import tkinter
import time

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"


def start_clicked():
    pass

def stop_clicked():
    pass

def main():
    stop = False

    window = tkinter.Tk()

    #
    title_label = tkinter.Label(text="Pomodoro", font=(FONT_NAME, 24)).grid(column=1, row=0)
    timer_label = tkinter.Label(text=count, font=FONT_NAME).grid(column=1, row=1)
    start_button = tkinter.Button(text="Start", command=start_clicked).grid(column=0, row=2)
    stop_button = tkinter.Button(text="Stop", command=stop_clicked).grid(column=2, row=2)
    #
    window.title("POMODORO APP")
    window.minsize(width=400,height=400)
    #

    window.mainloop()


main()



