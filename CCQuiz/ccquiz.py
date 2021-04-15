import continent
from tkinter import *
from tkinter import messagebox
import random


def clear_view():  # Clear window.
    for slave in tk.grid_slaves():
        slave.destroy()


def reset():  # Reset global value to start new game.
    global dict_of_game, true_answers, countries, capitals, country, capital
    dict_of_game = {}
    true_answers = 0
    countries = []
    capitals = ["Расака", "Манато", "Няма такава Държава", "Има такъв народ", "Тантар"]
    country = ""
    capital = ""
    start_window()


def end_of_game():  # End of game and view the result.
    clear_view()
    Label(tk, text="Вие познахте :", font=("Courier", 14)).grid(row=0, padx=5, pady=5)
    Label(tk, text=str(true_answers) + " столици от: " + str(len(dict_of_game)) + "  държави,", font=("Courier", 14))\
        .grid(row=1, padx=5, pady=5)
    Label(tk, text="в този тест!", font=("Courier", 14)).grid(row=2, padx=5, pady=5)
    Button(tk, text="Нов тест", font=("Courier", 14), command=reset).grid(row=3, padx=5, pady=5)


def check_answer(answer):  # Check for true answer.
    global true_answers, capital
    if answer == capital:
        true_answers += 1
    start_game()


def start_game():  # Start game and view main window.
    global country, capital, capitals
    if countries:
        country = random.choice(countries)  # Get random country from dictionary.
        countries.remove(country)
        capital = dict_of_game[country]
        capitals.remove(capital)
        answer1 = random.choice(capitals)  # Get other 3 random capitals for answer buttons.
        capitals.remove(answer1)
        answer2 = random.choice(capitals)
        capitals.remove(answer2)
        answer3 = random.choice(capitals)
        answers = [answer3, answer2, answer1, capital]
        capitals.extend(answers[1:])  # Roll back capitals to the list.
        clear_view()
        Label(tk, text="Държава:", font=("Courier", 14)).grid(row=0, columnspan=2, padx=20, pady=10)
        Label(tk, text=country, font=("Courier", 24)).grid(row=1, columnspan=2, padx=20, pady=10)
        Label(tk, text="Изберете Столица:", font=("Courier", 14)).grid(row=3, columnspan=2, padx=20, pady=10)
        ans1 = random.choice(answers)
        answers.remove(ans1)
        Button(tk, text=ans1, bg="White", font=("Courier", 16), width=25, command=lambda: check_answer(ans1))\
            .grid(row=4, column=0, padx=3, pady=3)
        ans2 = random.choice(answers)
        answers.remove(ans2)
        Button(tk, text=ans2, bg="White", font=("Courier", 16), width=25, command=lambda: check_answer(ans2))\
            .grid(row=4, column=1, padx=3, pady=3)
        ans3 = random.choice(answers)
        answers.remove(ans3)
        Button(tk, text=ans3, bg="White", font=("Courier", 16), width=25, command=lambda: check_answer(ans3))\
            .grid(row=5, column=0, padx=3, pady=3)
        ans4 = random.choice(answers)
        answers.remove(ans4)
        Button(tk, text=ans4, bg="White", font=("Courier", 16), width=25, command=lambda: check_answer(ans4))\
            .grid(row=5, column=1, padx=3, pady=3)
    else:
        end_of_game()


def start_window():  # Start window to select a region of the game.

    def add_continent():
        global countries, capitals, dict_of_game

        selection = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
        while "No" in selection:
            selection.remove("No")
        if not selection:
            messagebox.showinfo("Грешка:", "Изберете РЕГИОН!")
            return start_window

        for r in selection:
            if r == region[0]:
                dict_of_game.update(continent.europe)
            elif r == region[1]:
                dict_of_game.update(continent.asia)
            elif r == region[2]:
                dict_of_game.update(continent.africa)
            elif r == region[3]:
                dict_of_game.update(continent.america)
            elif r == region[4]:
                dict_of_game.update(continent.oceania)

        capitals.extend(list(dict_of_game.values()))
        countries = list(dict_of_game.keys())
        start_game()

    clear_view()
    region = ["ЕВРОПА", "АЗИЯ", "АФРИКА", "АМЕРИКА", "ОКЕАНИЯ"]
    dict_of_game = {}

    Label(tk, text="ТЕСТ:", font=("Courier", 14)).grid(row=0, columnspan=2, padx=20, pady=10)
    Label(tk, text="ПОЗНАЙ СТОЛИЦАТА НА ДЪРЖАВАТА", font=("Courier", 20)).grid(row=1, columnspan=2, padx=20, pady=10)
    Label(tk, text="Изберете регион за теста:", font=("Courier", 14)).grid(row=2, columnspan=2, padx=20, pady=10)
    for n in range(5):
        Label(tk, text=region[n], font=("Courier", 14)).grid(row=3+n, column=1, padx=20, pady=10, sticky="w")
    var1 = StringVar()
    check_box = Checkbutton(tk, variable=var1, onvalue=region[0], offvalue="No")
    check_box.deselect()
    check_box.grid(row=3, column=0, padx=20, pady=10, sticky="e")
    var2 = StringVar()
    check_box = Checkbutton(tk, variable=var2, onvalue=region[1], offvalue="No")
    check_box.deselect()
    check_box.grid(row=4, column=0, padx=20, pady=10, sticky="e")
    var3 = StringVar()
    check_box = Checkbutton(tk, variable=var3, onvalue=region[2], offvalue="No")
    check_box.deselect()
    check_box.grid(row=5, column=0, padx=20, pady=10, sticky="e")
    var4 = StringVar()
    check_box = Checkbutton(tk, variable=var4, onvalue=region[3], offvalue="No")
    check_box.deselect()
    check_box.grid(row=6, column=0, padx=20, pady=10, sticky="e")
    var5 = StringVar()
    check_box = Checkbutton(tk, variable=var5, onvalue=region[4], offvalue="No")
    check_box.deselect()
    check_box.grid(row=7, column=0, padx=20, pady=10, sticky="e")
    Button(tk, text="Начало на Теста", width=15, font=("Courier", 14), command=add_continent).grid(row=8, columnspan=2, pady=5)


dict_of_game = {}
true_answers = 0
countries = []
capitals = ["Русе", "Пловдив", "Барселона", "Ница", "Паница", "Мекица", "Има такава Държава",
            "Има такъв Народ", "Бай Иван"]  # More capitals, for more fun!
country = ""
capital = ""
tk = Tk()
tk.title("CCQuiz")
start_window()
tk.mainloop()
