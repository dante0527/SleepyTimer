"""
Sleepy - sleep timer for my titi
Author: Dante Lee
"""

import tkinter as tk
import tkinter.ttk as ttk
import os

# Window
root = tk.Tk()
root.resizable(0,0)
root.geometry("400x300+300+300")
root.configure(bg="pink")
root.title("Sleepy Timer")

def sleep(option, delay):
    option="-s"
    os.system(f"sudo shutdown {option} +{int(delay)}")


# Timer option
label_delay = tk.Label(
    text="Set delay",
    fg="black",
    bg="pink")
label_delay.pack()

minutes = ["15", "30", "45", "60"]

default_delay = tk.StringVar()
default_delay.set(minutes[-1])
delay = ttk.OptionMenu(root, default_delay, *minutes)
delay.pack()

# Start timer button
label_run = tk.Label(
    text="Start timer",
    fg="black",
    bg="pink"
)
label_run.pack()

button_run = tk.Button(root, text="Go", command=sleep, highlightbackground="pink")
button_run.pack()

if __name__ == "__main__":
    root.mainloop()