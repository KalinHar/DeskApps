from tkinter import *
from tkinter.ttk import *


def new_game():  # Reset main variables and start new game.
    global counter, pl1m, pl2m, button
    counter = 0
    pl1m = ''
    pl2m = ''
    button = {x: x for x in range(1, 10)}
    start_game()


def clear_view():  # Clear window.
    for slave in window.grid_slaves():
        slave.destroy()


def end_of_game(result):  # Rendering final view, with winning combination and winner if exist.
    if result:
        for r in range(3):
            for c in range(3):
                if r * 3 + c + 1 in result:  # Check the board button is in winning combination.
                    if button[r * 3 + c + 1] == 'x':
                        if pl1m == 'x':
                            winner = "Player 1"
                        else:
                            winner = "Player 2"
                        Label(window, image=photoXW).grid(row=r, column=c)  # Paste the winning mark on winning comb.
                    else:
                        if pl1m == 'o':
                            winner = "Player 1"
                        else:
                            winner = "Player 2"
                        Label(window, image=photoOW).grid(row=r, column=c)  # Paste the winning mark on winning comb.
        Label(window, text="The Winner is: " + winner, font=('Verdana', 12)).grid(row=3, columnspan=3)
        Button(window, text="Next", width=20, command=new_game).grid(row=4, columnspan=3)
    else:
        Label(window, text="No Winner!", font=('Verdana', 12)).grid(row=3, columnspan=3)
        Button(window, text="Next", width=20, command=new_game).grid(row=4, columnspan=3)


def check_for_winner():  # Check for winning combination and send it to final view.
    if button[1] == button[2] == button[3]:
        end_of_game([1, 2, 3])
    elif button[4] == button[5] == button[6]:
        end_of_game([4, 5, 6])
    elif button[7] == button[8] == button[9]:
        end_of_game([7, 8, 9])
    elif button[1] == button[4] == button[7]:
        end_of_game([1, 4, 7])
    elif button[2] == button[5] == button[8]:
        end_of_game([2, 5, 8])
    elif button[3] == button[6] == button[9]:
        end_of_game([3, 6, 9])
    elif button[1] == button[5] == button[9]:
        end_of_game([1, 5, 9])
    elif button[7] == button[5] == button[3]:
        end_of_game([7, 5, 3])
    elif counter == 9:
        main_desk()
        end_of_game([])
    else:
        main_desk()


def change_button_view(n):  # Changing button selected from player.
    global button
    if counter % 2 == 0:
        button[n] = pl2m
    else:
        button[n] = pl1m
    if counter > 4:
        check_for_winner()
    else:
        main_desk()


def button_view(n):  # Generate button view.
    if button[n] == "x":
        return Button(window, image=photoX)
    elif button[n] == "o":
        return Button(window, image=photoO)
    else:
        return Button(window, image=photoN, command=lambda: change_button_view(n))


def main_desk():  # Rendering main board.
    clear_view()
    global counter
    counter += 1
    b1 = button_view(1)
    b1.grid(row=0, column=0)
    b2 = button_view(2)
    b2.grid(row=0, column=1)
    b3 = button_view(3)
    b3.grid(row=0, column=2)
    b4 = button_view(4)
    b4.grid(row=1, column=0)
    b5 = button_view(5)
    b5.grid(row=1, column=1)
    b6 = button_view(6)
    b6.grid(row=1, column=2)
    b7 = button_view(7)
    b7.grid(row=2, column=0)
    b8 = button_view(8)
    b8.grid(row=2, column=1)
    b9 = button_view(9)
    b9.grid(row=2, column=2)
    if counter % 2 == 0:
        Label(window, text="Player 2", font=('Verdana', 12)).grid(row=3, columnspan=3)
    else:
        Label(window, text="Player 1", font=('Verdana', 12)).grid(row=3, columnspan=3)
    Label(window, text="it's your turn!", font=('Verdana', 12)).grid(row=4, columnspan=3, pady=2)


def players_marks(m):  # Generate players marks.
    global pl1m, pl2m
    if m == "x":
        pl1m = 'x'
        pl2m = 'o'
    else:
        pl1m = 'o'
        pl2m = 'x'
    main_desk()


def start_game():  # Rendering start window.
    clear_view()
    Label(window, text="Welcome to:", font=('Verdana', 16)).grid(row=0, column=0, columnspan=3, pady=5)
    Label(window, text="Tic-Tac-Toe", font=('Verdana', 20)).grid(row=1, column=0, columnspan=3, pady=2)
    Label(window, text="Game for 2 players.", font=('Verdana', 16)).grid(row=2, column=0, columnspan=3, pady=5)
    Label(window, text="Player 1 choose", font=('Verdana', 16)).grid(row=3, column=0, columnspan=3)
    Label(window, text="your mark:", font=('Verdana', 16)).grid(row=4, column=0, columnspan=3, pady=5)
    Label(window, text="or", font=('Verdana', 16)).grid(row=5, column=1, padx=26)
    Button(window, image=photoX, command=lambda: players_marks("x")).grid(row=5, column=0, pady=4)
    Button(window, image=photoO, command=lambda: players_marks("o")).grid(row=5, column=2)


window = Tk()
window.iconbitmap('ttt.ico')
window.title("TicTacToe")
window.resizable(width=False, height=False)

photoO = PhotoImage(file="Omark.png")
photoOW = PhotoImage(file="OWmark.png")
photoX = PhotoImage(file="Xmark.png")
photoXW = PhotoImage(file="XWmark.png")
photoN = PhotoImage(file="Nmark.png")

counter = 0
pl1m = ''  # Player 1 mark
pl2m = ''  # Player 2 mark
button = {x: x for x in range(1, 10)}  # Generate 9 buttons with different values.

start_game()
window.mainloop()
