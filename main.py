"""
Sleepy - sleep timer for my titi
Author: Dante Lee
"""

from tkinter import *
import os

# Window
window = Tk()
window.resizable(0,0)
window.geometry("300x200+300+300")
window.title("Sleepy Timer")
window.configure(background="pink")
window.grid_columnconfigure((0, 1), weight=1, uniform="equal")

def sleep():
    os.system(f"sudo shutdown {timer_type.get()} +{int(timer_delay.get())}")


# Timer length option
label_delay = Label(
    window,
    text="Set delay",
    fg="black",
    bg="pink")
label_delay.grid(column=0, row=0, pady=(10, 5))

minutes = [15, 30, 45, 60]
timer_delay = IntVar()
timer_delay.set(minutes[1])
menu_delay = OptionMenu(window, timer_delay, minutes[0], *minutes[1:])
menu_delay.config(fg="black", bg="pink", activeforeground="black")
menu_delay.grid(column=0, row=1)

# Timer type option
label_timer_type = Label(
    window,
    text="When timer ends...",
    fg="black",
    bg="pink")
label_timer_type.grid(column=1, row=0, columnspan=2, pady=(10, 5))

timer_type = StringVar()
R_Sleep = Radiobutton(window, text="Sleep", var=timer_type, value="-s")
R_Shutdown = Radiobutton(window, text="Shutdown", var=timer_type, value="-h")
R_Restart = Radiobutton(window, text="Restart", var=timer_type, value="-r")
timer_type.set("-s")

R_Sleep.config(fg="black", bg="pink")
R_Shutdown.config(fg="black", bg="pink")
R_Restart.config(fg="black", bg="pink")

R_Sleep.grid(column=1, row=1, sticky=NW, columnspan=2, padx=(30, 0))
R_Shutdown.grid(column=1, row=2, sticky=NW, columnspan=2, padx=(30, 0))
R_Restart.grid(column=1, row=3, sticky=NW, columnspan=2, padx=(30, 0))

# Start timer button
label_run = Label(
    text="Start timer",
    foreground="black",
    background="pink"
)
label_run.grid(column=0, row=4, columnspan=2, pady=(10, 5))

button_run = Button(window, text="Go", command=sleep, highlightbackground="pink")
button_run.grid(column=0, row=5, columnspan=2)


if __name__ == "__main__":
    window.mainloop()
