from tkinter import *
from tkinter.ttk import *
import random


def clear_view():  # Clear window.
    for slave in window.grid_slaves():
        slave.destroy()


def who_win(you, pc):  # Compares who win and return winner.
    global your_wins
    global pc_wins
    if you == pc:
        return "Equal!"
    elif (you == "Rock" and pc == "Scissors") or\
            (you == "Scissors" and pc == "Paper") or\
            (you == "Paper" and pc == "Rock"):
        your_wins += 1
        return "You\nWin!"
    else:
        pc_wins += 1
        return "PC\nWin!"


def reset():  # Reset wins statistics.
    global your_wins
    global pc_wins
    your_wins = 0
    pc_wins = 0
    main_view()


def action_view(your_choice):  # Rendering after battle window.
    clear_view()
    pc_choice = random.choice(list(actions.keys()))
    message = who_win(your_choice, pc_choice)
    Label(window, text='Rock Scissors Paper', font=('Verdana', 15)).grid(row=0, columnspan=3)
    Label(window, image=actions[your_choice]).grid(row=1, column=0, pady=3, padx=3)
    Label(window, image=actions[pc_choice]).grid(row=1, column=2, pady=3, padx=3)
    Button(window, text=" New \nturn!", command=main_view).grid(row=2, column=1)
    Label(window, text=message, font=('Verdana', 12)).grid(row=1, column=1, pady=3, padx=3)


def main_view():  # Rendering main window
    clear_view()
    Label(window, text='Rock Scissors Paper', font=('Verdana', 15)).grid(row=0, columnspan=3)
    Button(window, text="click", image=photo1, command=lambda: action_view("Rock")).grid(row=1, column=0)
    Button(window, text="click", image=photo2, command=lambda: action_view("Scissors")).grid(row=1, column=1)
    Button(window, text="click", image=photo3, command=lambda: action_view("Paper")).grid(row=1, column=2)
    Label(window, text="Your wins:", font=('Verdana', 9)).grid(row=2, column=0)
    Label(window, text="PC wins:", font=('Verdana', 9)).grid(row=2, column=2)
    Label(window, text=your_wins, font=('Verdana', 12)).grid(row=3, column=0)
    Label(window, text=pc_wins, font=('Verdana', 12)).grid(row=3, column=2)
    Button(window, text="Reset\nresults!", command=reset).grid(row=2, rowspan=2, column=1)


window = Tk()
window.iconbitmap('rsp1.ico')
window.title("RoSciPa")
window.resizable(width=False, height=False)
photo1 = PhotoImage(file="Rock.png")
photo2 = PhotoImage(file="Scissors.png")
photo3 = PhotoImage(file="Paper.png")
actions = {'Rock': photo1, 'Scissors': photo2, 'Paper': photo3}
your_wins = 0
pc_wins = 0
main_view()
window.mainloop()
