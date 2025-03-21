import tkinter as tk
from tkinter import *



def sum_number(num1, num2, result_lb):
    sumary = int(num1) + int(num2)
    result_text = "Сумма", num1, "и", num2, "Равна", sumary
    result_lb.configure(text=result_text)

def dif_number(num1, num2, result_lb):
    diff = int(num1) - int(num2)
    result_text = "Разность", num1, "и", num2, "Равна", diff
    result_lb.configure(text=result_text)

def multi_number(num1, num2, result_lb):
    mult = int(num1) * int(num2)
    result_text = "Произведение", num1, "и", num2, "Равна", mult
    result_lb.configure(text=result_text)

def del_number(num1, num2, result_lb):
    dell = int(num1) / int(num2)
    result_text = "Частное", num1, "и", num2, "Равна", dell
    result_lb.configure(text=result_text)
def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()

def create_sum_elements():
    clear_frame()
    number_one_lb = Label(frame, text="Число 1")  # создаем подпись к первому textbox
    number_one_lb.grid(row=1, column=1)  # указываем расположение элемента
    number_one_tb = Entry(frame)  # создаем первый textbox
    number_one_tb.grid(row=1, column=2)  # аналогично размещаем
    number_two_lb = Label(frame, text="Число 2")  # создаем подпись к второму textbox
    number_two_lb.grid(row=2, column=1)  # указываем расположение элемента
    number_two_tb = Entry(frame)  # создаем второй textbox
    number_two_tb.grid(row=2, column=2)  # аналогично размещаем

    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)

    btn = Button(
        frame,
        text='Посчитать',  # Надпись на кнопке.
        command=lambda: sum_number(number_one_tb.get(), number_two_tb.get(), result_lb)
    )
    btn.grid(row=3, column=1, columnspan=3)

def create_dif_elements():
    clear_frame()
    number_one_lb = Label(frame, text="Число 1")  # создаем подпись к первому textbox
    number_one_lb.grid(row=1, column=1)  # указываем расположение элемента
    number_one_tb = Entry(frame)  # создаем первый textbox
    number_one_tb.grid(row=1, column=2)  # аналогично размещаем
    number_two_lb = Label(frame, text="Число 2")  # создаем подпись к второму textbox
    number_two_lb.grid(row=2, column=1)  # указываем расположение элемента
    number_two_tb = Entry(frame)  # создаем второй textbox
    number_two_tb.grid(row=2, column=2)  # аналогично размещаем

    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)

    btn = Button(
        frame,
        text='Посчитать',  # Надпись на кнопке.
        command=lambda: dif_number(number_one_tb.get(), number_two_tb.get(), result_lb)
    )
    btn.grid(row=3, column=1, columnspan=3)

def create_del_elements():
    clear_frame()
    number_one_lb = Label(frame, text="Число 1")  # создаем подпись к первому textbox
    number_one_lb.grid(row=1, column=1)  # указываем расположение элемента
    number_one_tb = Entry(frame)  # создаем первый textbox
    number_one_tb.grid(row=1, column=2)  # аналогично размещаем
    number_two_lb = Label(frame, text="Число 2")  # создаем подпись к второму textbox
    number_two_lb.grid(row=2, column=1)  # указываем расположение элемента
    number_two_tb = Entry(frame)  # создаем второй textbox
    number_two_tb.grid(row=2, column=2)  # аналогично размещаем

    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)

    btn = Button(
        frame,
        text='Посчитать',  # Надпись на кнопке.
        command=lambda: del_number(number_one_tb.get(), number_two_tb.get(), result_lb)
    )
    btn.grid(row=3, column=1, columnspan=3)

def create_multi_elements():
    clear_frame()
    number_one_lb = Label(frame, text="Число 1")  # создаем подпись к первому textbox
    number_one_lb.grid(row=1, column=1)  # указываем расположение элемента
    number_one_tb = Entry(frame)  # создаем первый textbox
    number_one_tb.grid(row=1, column=2)  # аналогично размещаем
    number_two_lb = Label(frame, text="Число 2")  # создаем подпись к второму textbox
    number_two_lb.grid(row=2, column=1)  # указываем расположение элемента
    number_two_tb = Entry(frame)  # создаем второй textbox
    number_two_tb.grid(row=2, column=2)  # аналогично размещаем

    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)

    btn = Button(
        frame,
        text='Посчитать',  # Надпись на кнопке.
        command=lambda: multi_number(number_one_tb.get(), number_two_tb.get(), result_lb)
    )
    btn.grid(row=3, column=1, columnspan=3)


window = Tk()  # Создаём окно приложения.
window.title("Калькулятор")  # Добавляем название приложения.
window.geometry('600x500+10+10')  # Указываем размеры окна

mainmenu = Menu(window)
window.config(menu=mainmenu)

grafmenu = Menu(mainmenu, tearoff=0)
grafmenu.add_command(label="Сложение", command=create_sum_elements)
grafmenu.add_command(label="Вычитание", command=create_dif_elements)
grafmenu.add_command(label="Умножение", command=create_multi_elements)
grafmenu.add_command(label="Деление", command=create_del_elements)

mainmenu.add_cascade(label="Математические опрерации",
                     menu=grafmenu)

frame = Frame(
    window,  # Обязательный параметр, который указывает окно для размещения Frame.
    padx=10,  # Задаём отступ по горизонтали.
    pady=10  # Задаём отступ по вертикали.
)

frame.pack(expand=True)

window.mainloop()