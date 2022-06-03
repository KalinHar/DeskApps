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

    def disable_button(i):  # Gets the letter, switched pressed button to DISABLED and change color.
        letter = buttons[i-1]["text"]
        buttons[i-1]["state"] = "disabled"
        buttons[i-1]["bg"] = "pink"

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
    buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30]
    img_hang.grid(row=0, rowspan=5, column=0, padx=5, pady=5)
    title.grid(row=0, column=2, columnspan=10, padx=3, pady=3)
    word_view.grid(row=1, column=2, columnspan=10)
    # Generate buttons grid of 3 rows and 10 columns
    n = 0
    for r in range(2,5):
        for c in range(2,12):
            buttons[n].grid(row=r, column=c, padx=5)
            n += 1

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
