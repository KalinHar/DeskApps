from tkinter import *
import json
from tkinter.ttk import Combobox
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import messagebox


def cars_update():  # Update cars data.
    try:
        with open("autodata.txt", "r+") as file:
            models = json.loads(file.read())
        cars = [x["model"] for x in models]
    except:
        cars = []
    return cars


def clear_view():  # Clear window.
    for widget in window.winfo_children():
        widget.destroy()


def save_data(model, insurance, inspection, vinete, replace, note):  # Save new data.
    try:
        with open("autodata.txt", "r+") as file:
            models = json.loads(file.read())
    except:
        models = []
    if model in car:
        messagebox.showinfo("Can't Added!", 'Model exist in AutoData!')
        return save_data_view()
    if model:
        save_model = {"model": model, "insurance": insurance, "inspection": inspection,
                      "vinete": vinete, "replace": replace, "note": note}
        models.append(save_model)
        car.append(model)
        messagebox.showinfo('Model added: ', 'Successfully!')
        save_data_view()
    else:
        messagebox.showinfo('Entry: ', 'Please entry Model!')
        save_data_view()
    with open("autodata.txt", "w") as file:
        json.dump(models, file)


def edit_data(model, insurance, inspection, vinete, replace, note):  # Edit selected car data.
    answer = messagebox.askquestion("Save New Data!", "Are you sure?")
    if answer == "no":
        return
    with open("autodata.txt", "r+") as file:
        models = json.loads(file.read())
        for index in range(len(models)):
            if models[index]["model"] == model:
                break
        del models[index]
        save_model = {"model": model, "insurance": insurance, "inspection": inspection, "vinete": vinete,
                      "replace": replace, "note": note}
        models.append(save_model)
        file.truncate(0)
        file.seek(0)
        json.dump(models, file)
        messagebox.showinfo(model, 'Was Updated!')
        main_view()


def delete_data(model):  # Delete selected car data.
    if model not in car:
        messagebox.showinfo('Model: ', 'Please, select Model!')
        return
    answer = messagebox.askquestion("Confirm delete", "Are you sure?")
    if answer == "no":
        return
    with open("autodata.txt", "r+") as file:
        models = json.loads(file.read())
        for index in range(len(models)):
            if models[index]["model"] == model:
                break
        car.remove(model)
        del models[index]
        file.truncate(0)
        file.seek(0)
        json.dump(models, file)
        messagebox.showinfo(model, 'Was Deleted!')
        main_view()


def car_view(model):  # Render selected car data window.
    if model not in car:
        messagebox.showinfo('Model: ', 'Please, select Model!')
        return
    with open("autodata.txt", "r") as file:
        models = json.loads(file.read())
        for index in range(len(models)):
            if models[index]["model"] == model:
                break
        mod, insu, insp, vine, repl, note = [v for v in models[index].values()]
    clear_view()
    Label(window, text="model,№: " + mod, font=("arial bold", 14)).pack(pady=10, padx=10)
    Label(window, text="Insurance Valid to: " + insu, font=("arial bold", 12)).pack(pady=10, padx=10)
    Label(window, text="Technical Inspection on: " + insp, font=("arial bold", 12)).pack(pady=10, padx=10)
    Label(window, text="Vinete Valid to: " + vine, font=("arial bold", 12)).pack(pady=10, padx=10)
    Label(window, text="Oil Replacement: " + repl, font=("arial bold", 12)).pack(pady=10, padx=10)
    text_area = st.ScrolledText(window, width=30, height=1)
    text_area.pack(pady=10, padx=10)
    text_area.insert(tk.INSERT, note)
    text_area.configure(state='disabled')
    Button(window, text="Back", command=main_view, font=("arial bold", 10), width=8, height=0)\
        .pack(pady=10, padx=10)


def edit_data_view(model):  # Render Editing data window.
    if model not in car:
        messagebox.showinfo('Model: ', 'Please, select Model!')
        return
    with open("autodata.txt", "r") as file:
        models = json.loads(file.read())
        for index in range(len(models)):
            if models[index]["model"] == model:
                break
        mod, insu, insp, vine, repl, note = [v for v in models[index].values()]
    clear_view()
    Label(window, text="Model,№: " + mod, font=("arial bold", 12))\
        .grid(row=0, columnspan=2, pady=10)
    Label(window, text="Insurance Valid to:", font=("arial bold", 10)).grid(row=1, column=0, pady=10, sticky="e")
    insurance = Entry(window, width=28, font=("arial bold", 10), bg="pink")
    insurance.grid(row=1, column=1)
    insurance.insert(0, insu)
    Label(window, text="Technical Inspection on:", font=("arial bold", 10))\
        .grid(row=2, column=0, padx=5, pady=10, sticky="e")
    inspection = Entry(window, width=28, font=("arial bold", 10), bg="pink")
    inspection.grid(row=2, column=1)
    inspection.insert(0, insp)
    Label(window, text="Vinete Valid to:", font=("arial bold", 10)).grid(row=3, column=0, pady=10, sticky="e")
    vinete = Entry(window, width=28, font=("arial bold", 10), bg="pink")
    vinete.grid(row=3, column=1)
    vinete.insert(0, vine)
    Label(window, text="Oil Repl(date),to(km):", font=("arial bold", 10)).grid(row=4, column=0, pady=10, sticky="e")
    replacement = Entry(window, width=28, font=("arial bold", 10), bg="pink")
    replacement.grid(row=4, column=1)
    replacement.insert(0, repl)
    Label(window, text="Note:", font=("arial bold", 10)).grid(row=5, column=0, pady=10, sticky="e")
    notes = Entry(window, width=28, font=("arial bold", 10), bg="pink")
    notes.grid(row=5, column=1)
    notes.insert(0, note)
    Button(window, text="Cancel", command=main_view, font=("arial bold", 9), width=8, height=0)\
        .grid(row=6, column=0, pady=10)
    Button(window, text="Edit",
           command=lambda: edit_data(mod, insurance.get(), inspection.get(), vinete.get(), replacement.get(),
                                     notes.get()), font=("arial bold", 9), width=8, height=0) \
        .grid(row=6, column=1)


def save_data_view():  # Render saving data window.
    clear_view()
    Label(window, text="Model,№:", font=("arial bold", 12))\
        .grid(row=0, column=0, pady=10, padx=5, sticky="e")
    model = Entry(window, width=30, font=("arial bold", 9))
    model.grid(row=0, column=1)
    model.insert(0, "Model,№")
    Label(window, text="Insurance Valid to:", font=("arial bold", 9))\
        .grid(row=1, column=0, pady=10, padx=5, sticky="e")
    insurance = Entry(window, width=30, font=("arial bold", 9))
    insurance.grid(row=1, column=1)
    insurance.insert(0, "Exp.Date")
    Label(window, text="Technical Inspection on:", font=("arial bold", 9))\
        .grid(row=2, column=0, padx=5, pady=10, sticky="e")
    inspection = Entry(window, width=30, font=("arial bold", 9))
    inspection.grid(row=2, column=1)
    inspection.insert(0, "Exp.Date")
    Label(window, text="Vinete Valid to:", font=("arial bold", 9))\
        .grid(row=3, column=0, padx=5, pady=10, sticky="e")
    vinete = Entry(window, width=30, font=("arial bold", 9))
    vinete.grid(row=3, column=1)
    vinete.insert(0, "Exp.Date")
    Label(window, text="Oil Repl(date),to(km):", font=("arial bold", 9))\
        .grid(row=4, column=0, padx=5, pady=10, sticky="e")
    replacement = Entry(window, width=30, font=("arial bold", 9))
    replacement.grid(row=4, column=1)
    replacement.insert(0, 0)
    Label(window, text="Note:", font=("arial bold", 9))\
        .grid(row=5, column=0, pady=10, padx=5, sticky="e")
    notes = Entry(window, width=30, font=("arial bold", 9))
    notes.grid(row=5, column=1)
    notes.insert(0, "OK")
    Button(window, text="Back", command=main_view, font=("arial bold", 12), width=10, height=0)\
        .grid(row=6, column=0)
    Button(window, text="Save",
           command=lambda: save_data(model.get(),insurance.get(), inspection.get(), vinete.get(),
                                     replacement.get(), notes.get()), font=("arial bold", 12), width=10, height=0)\
        .grid(row=6, column=1, pady=10)


def main_view():  # Render main menu window.
    clear_view()
    Button(window, text="Add New", command=save_data_view, font=("arial bold", 12), width=10, height=0)\
        .pack(pady=20)
    Label(window, text="Please, select vehicle:", font=("arial bold", 10)).pack()
    selected_model = StringVar(window)
    dropdown = Combobox(window, textvariable=selected_model, width=20, font=("arial bold", 12))
    dropdown['values'] = car
    dropdown.pack(padx=10, pady=20)
    Button(window, text="View", command=lambda: car_view(selected_model.get()),
           font=("arial bold", 12), width=10, height=0).pack()
    Button(window, text="Edit", command=lambda: edit_data_view(selected_model.get()),
           font=("arial bold", 12), width=10, height=0).pack(pady=20)
    Button(window, text="Delete",command=lambda: delete_data(selected_model.get()),
           font=("arial bold", 12), width=10, height=0).pack()


window = Tk()
window.geometry("380x350")
window.resizable(width=False, height=False)
window.title("Auto Data")
window.iconbitmap('car.ico')
car = cars_update()
main_view()
window.mainloop()
