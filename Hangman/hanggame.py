import random
from tkinter import *
from tkinter import messagebox

words = ['ЛИСИЦА', 'КОТКА', 'ВЪЛК', 'НОСОРОГ', 'МАГАРЕ', 'БИВОЛ', 'ЛЕБЕД', 'ПАУН', 'КОЗА', 'МУФЛОН', 'ЗУБЪР',
         'ПАТКА', 'ЛЕОПАРД', 'РИС', 'ЛЪВ', 'ТИГЪР', 'МИШКА', 'ГЪЛЪБ', 'ВРАНА', 'ХИЕНА', 'АЛБАТРОС', 'ТЮЛЕН',
         'ЗАЕК', 'ПУЙКА', 'КОН', 'ЧАКАЛ', 'НОРКА', 'СИНИГЕР', 'АКУЛА', 'ДЕЛФИН', 'ГАРГА', 'ВИДРА', 'ЖИРАФ',
         'ОКТОПОД', 'ГЛАРУС', 'ЗЕБРА', 'КАМИЛА', 'ЩРАУС', 'ПАНТЕРА', 'МЕЧКА', 'ПРАСЕ', 'КОКОШКА', 'МАЙМУНА',
         'КРАВА', 'ОВЦА', 'ЩЪРКЕЛ', 'ЧАПЛА', 'ХИПОПОТАМ', 'ПЕТЕЛ', 'КУЧЕ', 'ЕЛЕН', 'СЪРНА', 'ФАЗАН', 'ГУЩЕР',
         'САФРИД', 'ЦАЦА', 'ТОЛСТОЛОБ', 'ПЕПЕРУДА', 'ПЛЪХ', 'ОХЛЮВ', 'КОСАТКА', 'БУХАЛ', 'АНАКОНДА', 'ЖАБА',
         'ПАПАГАЛ', 'ПИНГВИН', 'МОРЖ', 'КОСТЕНУРКА', 'ПЕЛИКАН', 'ОРЕЛ', 'ЯСТРЕБ', 'ФЛАМИНГО', 'ВАРАН', 'РАК',
         'ИГУАНА', 'КРОРКОДИЛ', 'СКОРПИОН', 'ДЪЖДОВНИК', 'ГЕКОН', 'САЛАМАНДЪР', 'ОРАНГУТАН', 'ШИМПАНЗЕ',
         'КЕНГУРУ', 'КОАЛА', 'ПАНДА', 'ОПОСУМ', 'СЛОН', 'КОСАТКА', 'КАШАЛОТ', 'ГЛУХАР']


def game_window():  # Main window of the game.
    global count_of_wrong_letters, word, words, shown_word

    def reset():  # Resets the global variables and starts new game.
        global count_of_wrong_letters, word, words, shown_word
        for slave in window.grid_slaves():
            slave.destroy()
        count_of_wrong_letters = 0
        words.remove(word)
        word = random.choice(words)
        shown_word = ["_"] * len(word)
        game_window()

    def check_letter(le):  # Checks the letters in word and checks for win or lose.
        global count_of_wrong_letters
        if le in word:
            for i in range(len(word)):
                if le == word[i]:
                    shown_word[i] = le
            Label(window, text=' '.join(shown_word), font=("Verdana Bold", 18)).grid(row=1, column=2, columnspan=10)
        else:
            count_of_wrong_letters += 1
            Label(window, image=photos[count_of_wrong_letters]).grid(row=0, rowspan=5, column=0)
        if word == ''.join(shown_word):
            messagebox.showinfo("", "ВИЕ ПОБЕДИХТЕ!")
            reset()
        if count_of_wrong_letters == 6:
            messagebox.showinfo("", "ВИЕ ЗАГУБИХТЕ!")
            reset()

    def disable_button(i):  # Gets the letter and switched pressed button to DISABLED.
        if i == 1:
            letter = b1["text"]
            b1["state"] = "disabled"
            b1["bg"] = "pink"
        elif i == 2:
            letter = b2["text"]
            b2["state"] = "disabled"
            b2["bg"] = "pink"
        elif i == 3:
            letter = b3["text"]
            b3["state"] = "disabled"
            b3["bg"] = "pink"
        elif i == 4:
            letter = b4["text"]
            b4["state"] = "disabled"
            b4["bg"] = "pink"
        elif i == 5:
            letter = b5["text"]
            b5["state"] = "disabled"
            b5["bg"] = "pink"
        elif i == 6:
            letter = b6["text"]
            b6["state"] = "disabled"
            b6["bg"] = "pink"
        elif i == 7:
            letter = b7["text"]
            b7["state"] = "disabled"
            b7["bg"] = "pink"
        elif i == 8:
            letter = b8["text"]
            b8["state"] = "disabled"
            b8["bg"] = "pink"
        elif i == 9:
            letter = b9["text"]
            b9["state"] = "disabled"
            b9["bg"] = "pink"
        elif i == 10:
            letter = b10["text"]
            b10["state"] = "disabled"
            b10["bg"] = "pink"
        elif i == 11:
            letter = b11["text"]
            b11["state"] = "disabled"
            b11["bg"] = "pink"
        elif i == 12:
            letter = b12["text"]
            b12["state"] = "disabled"
            b12["bg"] = "pink"
        elif i == 13:
            letter = b13["text"]
            b13["state"] = "disabled"
            b13["bg"] = "pink"
        elif i == 14:
            letter = b14["text"]
            b14["state"] = "disabled"
            b14["bg"] = "pink"
        elif i == 15:
            letter = b15["text"]
            b15["state"] = "disabled"
            b15["bg"] = "pink"
        elif i == 16:
            letter = b16["text"]
            b16["state"] = "disabled"
            b16["bg"] = "pink"
        elif i == 17:
            letter = b17["text"]
            b17["state"] = "disabled"
            b17["bg"] = "pink"
        elif i == 18:
            letter = b18["text"]
            b18["state"] = "disabled"
            b18["bg"] = "pink"
        elif i == 19:
            letter = b19["text"]
            b19["state"] = "disabled"
            b19["bg"] = "pink"
        elif i == 20:
            letter = b20["text"]
            b20["state"] = "disabled"
            b20["bg"] = "pink"
        elif i == 21:
            letter = b21["text"]
            b21["state"] = "disabled"
            b21["bg"] = "pink"
        elif i == 22:
            letter = b22["text"]
            b22["state"] = "disabled"
            b22["bg"] = "pink"
        elif i == 23:
            letter = b23["text"]
            b23["state"] = "disabled"
            b23["bg"] = "pink"
        elif i == 24:
            letter = b24["text"]
            b24["state"] = "disabled"
            b24["bg"] = "pink"
        elif i == 25:
            letter = b25["text"]
            b25["state"] = "disabled"
            b25["bg"] = "pink"
        elif i == 26:
            letter = b26["text"]
            b26["state"] = "disabled"
            b26["bg"] = "pink"
        elif i == 27:
            letter = b27["text"]
            b27["state"] = "disabled"
            b27["bg"] = "pink"
        elif i == 28:
            letter = b28["text"]
            b28["state"] = "disabled"
            b28["bg"] = "pink"
        elif i == 29:
            letter = b29["text"]
            b29["state"] = "disabled"
            b29["bg"] = "pink"
        elif i == 30:
            letter = b30["text"]
            b30["state"] = "disabled"
            b30["bg"] = "pink"
        check_letter(letter)

    # Generate buttons view and commands.
    title = Label(window, text="кат.ЖИВОТНИ", font=("Verdana", 12))
    img_hang = Label(window, image=photos[count_of_wrong_letters])
    word_view = Label(window, text=' '.join(shown_word), font=("Verdana Bold", 18))
    b1 = Button(window, text="А", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(1))
    b2 = Button(window, text="Б", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(2))
    b3 = Button(window, text="В", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(3))
    b4 = Button(window, text="Г", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(4))
    b5 = Button(window, text="Д", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(5))
    b6 = Button(window, text="Е", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(6))
    b7 = Button(window, text="Ж", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(7))
    b8 = Button(window, text="З", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(8))
    b9 = Button(window, text="И", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(9))
    b10 = Button(window, text="Й", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(10))
    b11 = Button(window, text="К", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(11))
    b12 = Button(window, text="Л", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(12))
    b13 = Button(window, text="М", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(13))
    b14 = Button(window, text="Н", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(14))
    b15 = Button(window, text="О", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(15))
    b16 = Button(window, text="П", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(16))
    b17 = Button(window, text="Р", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(17))
    b18 = Button(window, text="С", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(18))
    b19 = Button(window, text="Т", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(19))
    b20 = Button(window, text="У", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(20))
    b21 = Button(window, text="Ф", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(21))
    b22 = Button(window, text="Х", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(22))
    b23 = Button(window, text="Ц", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(23))
    b24 = Button(window, text="Ч", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(24))
    b25 = Button(window, text="Ш", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(25))
    b26 = Button(window, text="Щ", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(26))
    b27 = Button(window, text="Ъ", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(27))
    b28 = Button(window, text="Ь", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(28))
    b29 = Button(window, text="Ю", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(29))
    b30 = Button(window, text="Я", font=("Verdana Bold", 12), width=3, command=lambda: disable_button(30))
    img_hang.grid(row=0, rowspan=5, column=0, padx=5, pady=5)
    title.grid(row=0, column=2, columnspan=10, padx=3, pady=3)
    word_view.grid(row=1, column=2, columnspan=10)
    b1.grid(row=2, column=2, padx=5)
    b2.grid(row=2, column=3, padx=5)
    b3.grid(row=2, column=4, padx=5)
    b4.grid(row=2, column=5, padx=5)
    b5.grid(row=2, column=6, padx=5)
    b6.grid(row=2, column=7, padx=5)
    b7.grid(row=2, column=8, padx=5)
    b8.grid(row=2, column=9, padx=5)
    b9.grid(row=2, column=10, padx=5)
    b10.grid(row=2, column=11, padx=5)
    b11.grid(row=3, column=2)
    b12.grid(row=3, column=3)
    b13.grid(row=3, column=4)
    b14.grid(row=3, column=5)
    b15.grid(row=3, column=6)
    b16.grid(row=3, column=7)
    b17.grid(row=3, column=8)
    b18.grid(row=3, column=9)
    b19.grid(row=3, column=10)
    b20.grid(row=3, column=11)
    b21.grid(row=4, column=2)
    b22.grid(row=4, column=3)
    b23.grid(row=4, column=4)
    b24.grid(row=4, column=5)
    b25.grid(row=4, column=6)
    b26.grid(row=4, column=7)
    b27.grid(row=4, column=8)
    b28.grid(row=4, column=9)
    b29.grid(row=4, column=10)
    b30.grid(row=4, column=11)


window = Tk()
window.iconbitmap('hang.ico')
window.title("БЕСЕНКА")
window.resizable(width=False, height=False)
photo0 = PhotoImage(file="hang0.png")
photo1 = PhotoImage(file="hang1.png")
photo2 = PhotoImage(file="hang2.png")
photo3 = PhotoImage(file="hang3.png")
photo4 = PhotoImage(file="hang4.png")
photo5 = PhotoImage(file="hang5.png")
photo6 = PhotoImage(file="hang6.png")
photos = (photo0, photo1, photo2, photo3, photo4, photo5, photo6,)
count_of_wrong_letters = 0
word = random.choice(words)
shown_word = ["_"] * len(word)
game_window()
window.mainloop()
