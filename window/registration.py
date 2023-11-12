# register.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def register(db_cursor):
    register_window = tk.Tk()
    register_window.title("Регистрация")

    def on_register():
        name = entry_name.get()
        gender = var_gender.get()
        age = entry_age.get()
        email = entry_email.get()
        phone = entry_phone.get()
        is_root = var_root.get()

        db_cursor.execute(f"INSERT INTO users (name, gender, age, email, phone, root) VALUES ({name}, {gender}, {age}, {email}, {phone}, {is_root})")
        db_cursor.connection.commit()

        messagebox.showinfo("Регистрация", "Регистрация выполнена успешно!")

    # Создаем и размещаем виджеты с использованием ttk
    label_name = ttk.Label(register_window, text="Имя:")
    label_gender = ttk.Label(register_window, text="Пол:")
    label_age = ttk.Label(register_window, text="Возраст:")
    label_email = ttk.Label(register_window, text="Email:")
    label_phone = ttk.Label(register_window, text="Номер телефона:")

    entry_name = ttk.Entry(register_window)
    entry_age = ttk.Entry(register_window)
    entry_email = ttk.Entry(register_window)
    entry_phone = ttk.Entry(register_window)

    var_gender = tk.StringVar()
    var_gender.set("Мужской")  # Устанавливаем значение по умолчанию

    option_menu_gender = ttk.Combobox(register_window, textvariable=var_gender, values=["Мужской", "Женский"])
    
    var_root = tk.BooleanVar()
    check_root = ttk.Checkbutton(register_window, text="root", variable=var_root)

    button_register = ttk.Button(register_window, text="Зарегистрироваться", command=on_register)

    # Размещаем виджеты с использованием сетки
    label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    label_gender.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    option_menu_gender.grid(row=1, column=1, padx=10, pady=10)

    label_age.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    entry_age.grid(row=2, column=1, padx=10, pady=10)

    label_email.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
    entry_email.grid(row=3, column=1, padx=10, pady=10)

    label_phone.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
    entry_phone.grid(row=4, column=1, padx=10, pady=10)

    check_root.grid(row=0, column=2, padx=10, pady=10, sticky=tk.NE)
    
    button_register.grid(row=5, column=0, columnspan=2, pady=10)

    # Запускаем цикл событий Tkinter
    register_window.mainloop()
