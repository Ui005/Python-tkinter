import tkinter as tk
from tkinter import messagebox, simpledialog

class Pet:
    def __init__(self, name, price, nickname):
        self.name = name
        self.price = price
        self.nickname = nickname

    def __str__(self):
        return f"{self.nickname} ({self.name}) - {self.price} рублей"

class Cat(Pet):
    def __init__(self, nickname, price):
        super().__init__('Кошка', price, nickname)

class Dog(Pet):
    def __init__(self, nickname, price):
        super().__init__('Собака', price, nickname)

class Parrot(Pet):
    def __init__(self, nickname, price):
        super().__init__('Попугай', price, nickname)

class Fish(Pet):
    def __init__(self, nickname, price):
        super().__init__('Рыбка', price, nickname)

class PetShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Зоомагазин")

        self.pets = []

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        petmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Питомцы", menu=petmenu)
        petmenu.add_command(label="Добавить питомца", command=self.add_pet)
        petmenu.add_command(label="Показать список питомцев", command=self.show_pets)

        self.frame = tk.Frame(root)
        self.frame.pack()


    def add_pet(self):
        nickname = simpledialog.askstring("Кличка", "Введите кличку питомца:")
        if not nickname:  # Handle case where user cancels or enters nothing
            return
        pet_type = simpledialog.askstring("Тип питомца", "Введите тип питомца (Кошка, Собака, Попугай, Рыбка):")
        if not pet_type:
            return
        price = simpledialog.askfloat("Цена", "Введите цену питомца:")
        if price is None: # Handle case where user cancels or enters nothing
            return

        if pet_type == "Кошка":
            pet = Cat(nickname, price)
        elif pet_type == "Собака":
            pet = Dog(nickname, price)
        elif pet_type == "Попугай":
            pet = Parrot(nickname, price)
        elif pet_type == "Рыбка":
            pet = Fish(nickname, price)
        else:
            messagebox.showerror("Ошибка", "Неизвестный тип питомца!")
            return

        self.pets.append(pet)
        messagebox.showinfo("Успех", f"{pet.nickname} успешно добавлен!")

    def show_pets(self):
        pet_list = "\n".join(str(pet) for pet in self.pets)
        if pet_list:
            messagebox.showinfo("Список питомцев", pet_list)
        else:
            messagebox.showinfo("Список питомцев", "Список пуст.")




window = tk.Tk()
window.geometry('600x500+10+10')
app = PetShopApp(window)
window.mainloop()