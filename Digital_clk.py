import tkinter as tk
import time

def update_time():
    current = time.strftime("%H:%M:%S")
    label.config(text=current)
    label.after(1000, update_time)

win = tk.Tk()
win.title("Digital Clock")

label = tk.Label(win, font=("Arial", 48), fg="black")
label.pack(pady=40)

update_time()
win.mainloop()
