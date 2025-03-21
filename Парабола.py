from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

def do_plot(step, graf, canvas):
    graf.clear()
    x = np.linspace(-15, 15, 100)
    y = x ** step
    graf.plot(x, y)
    canvas.draw()
    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)
    result_text = "График функции:", "x^",step
    result_lb.configure(text=result_text)


def do_plot_q(a, b, c, graf, canvas):
    graf.clear()
    x = np.arange(-40, 40, 1)
    y = a * x ** 2 + b * x + c
    graf.plot(x, y)
    canvas.draw()
    result_lb = Label(frame)
    result_lb.grid(row=4, column=1, columnspan=3)
    result_text = "График функции:", "x^",a,"+",b,"x","+",c
    result_lb.configure(text=result_text)


def clear_frame():
    for widgets in frame.winfo_children():
        widgets.destroy()


def prabola_frame():
    clear_frame()
    figure = plt.Figure(figsize=(5, 5), facecolor='gray')
    canvas = FigureCanvasTkAgg(figure, frame)
    canvas.get_tk_widget().grid(row=2, column=1, columnspan=3)
    graf = figure.add_subplot(111)

    step_lb = Label(
        frame,
        text="Степень x"
    )
    step_lb.grid(row=1, column=1)
    step_tf = Entry(
        frame,
    )
    step_tf.grid(row=1, column=2)
    cal_btn = Button(
        frame,
        text='Построить',
        command=lambda: do_plot(float(step_tf.get()), graf, canvas)

    )
    cal_btn.grid(row=1, column=3)




def qadratic_frame():
    clear_frame()
    figure = plt.Figure(figsize=(5, 5), facecolor='gray')
    canvas = FigureCanvasTkAgg(figure, frame)
    canvas.get_tk_widget().grid(row=5, column=1, columnspan=3)
    graf = figure.add_subplot(111)
    a_lb = Label(
        frame,
        text="a"
    )
    a_lb.grid(row=1, column=1)
    a_tf = Entry(
        frame,
    )
    a_tf.grid(row=1, column=2)
    b_lb = Label(
        frame,
        text="b"
    )
    b_lb.grid(row=2, column=1)
    b_tf = Entry(
        frame,
    )
    b_tf.grid(row=2, column=2)
    c_lb = Label(
        frame,
        text="c"
    )
    c_lb.grid(row=3, column=1)
    c_tf = Entry(
        frame,
    )
    c_tf.grid(row=3, column=2)
    cal_btn = Button(
        frame,
        text='Построить',
        command=lambda: do_plot_q(float(a_tf.get()), float(b_tf.get()), float(c_tf.get()), graf, canvas)
    )
    cal_btn.grid(row=4, column=1, columnspan=2)


window = Tk()
window.title("Построение параболы")
window.geometry('800x600+10+10')

mainmenu = Menu(window)
window.config(menu=mainmenu)

grafmenu = Menu(mainmenu, tearoff=0)
grafmenu.add_command(label="Парабола", command=prabola_frame)
grafmenu.add_command(label="Квадратичная функция", command=qadratic_frame)

mainmenu.add_cascade(label="График",
                     menu=grafmenu)
frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(
    expand=True)
window.mainloop()