
import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(tagOrId=timer_text, text="00:00")
    timer_label.config(text="Timer.", fg=GREEN, font=(FONT_NAME, 20, "bold"))
    checks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0 or reps == 0 and reps < 8:
        count_down(work_sec)
        timer_label.config(text="Work.", fg=GREEN, font=(FONT_NAME, 20, "bold"))
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Rest.", fg=RED, font=(FONT_NAME, 20, "bold"))
    elif reps % 2 == 0 and reps < 7:
        count_down(short_break_sec)
        timer_label.config(text="Rest.", fg=PINK, font=(FONT_NAME, 20, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(tagOrId=timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        for _ in range(math.floor(reps / 2)):
            marks = "✅"
            checks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Anyieth's Timer.")
window.config(pady=50, padx=100, bg=YELLOW)
# creating a canvas

canvas = Canvas(height=200, width=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(108, 85, image=tomato_image)
timer_text = canvas.create_text(108, 110, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
checks = Label(fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)


checks.grid(column=1, row=4)
timer_label.grid(column=1, row=0)
start_button.grid(column=0, row=3)
reset_button.grid(column=3, row=3)
canvas.grid(column=1, row=1)

window.mainloop()
