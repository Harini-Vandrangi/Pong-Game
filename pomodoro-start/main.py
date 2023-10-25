from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
TIMER = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(TIMER)
    tick.config(text="")
    timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    if reps > 8:
        return
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Break", fg=PINK)
    elif reps % 2 != 0:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)
        tick.config(text=f"")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    mins = count//60
    secs = count % 60
    if secs <= 9:
        secs = f"0{secs}"
    canvas.itemconfig(time, text=f"{mins}:{secs}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count-1)
    else:
        start_timer()
        ticks = ""
        for _ in range(reps//2):
            ticks += "✔"
        tick.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pi = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pi)
time = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer label
timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

# tick label
tick = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row=3)
# start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# reset button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
