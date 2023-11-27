# register.py
from tkinter import *
import tkinter as tk
from tkinter import ttk
from query.connect_to_db import query
from side_func import read_config



def dismiss(window):
    window.grab_release() 
    window.destroy()

def register():
    register_window = Toplevel()
    register_window.resizable(0,0)
    register_window.title("Регистрация")
    register_window.geometry(f'270x200+{int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-135}+{int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-100}')
    register_window.protocol("WM_DELETE_WINDOW", lambda: dismiss(register_window))

    def is_valid_age(*args):
        age = entry_age.get()
        if not age.isdigit():
            message.config(text="Некорректный возраст", foreground="red")
        else:
            message.config(text="")

    def is_valid_phone(*args):
        phone = entry_phone.get()
        if not (phone.isdigit() and len(phone) == 10):
            message.config(text="Некорректный телефон", foreground="red")
        else:
            message.config(text="")
    
    def on_register():
        name = entry_name.get()
        password = entry_pass.get()
        gender = var_gender
        age = entry_age.get()
        email = entry_email.get()
        phone = entry_phone.get()
        is_root = var_root.get()
        
        if len(name) > 0 and len(password)>0 and 10 <= int(age) < 100 and "@" in email and email.endswith(".com") and phone.isdigit() and len(phone) == 10:
            query(f"INSERT INTO users (name, password, gender, age, email, phone_number, root) VALUES ('{name}', '{password}', '{gender}', {age}, '{email}', '{phone}', {is_root})")
            dismiss(register_window)
        else:
            message.config(text="Некорректные данные")
            

    label_name = ttk.Label(register_window, text="Логин:")
    label_pass = ttk.Label(register_window, text="Пароль:")
    label_gender = ttk.Label(register_window, text="Пол:")
    label_age = ttk.Label(register_window, text="Возраст(10-100):")
    label_email = ttk.Label(register_window, text="Email:")
    label_phone = ttk.Label(register_window, text="Номер телефона:")
    
    message = ttk.Label(register_window)

    entry_name = ttk.Entry(register_window)
    entry_pass = ttk.Entry(register_window)
    var_gender = 'm'
    entry_age = ttk.Entry(register_window)
    entry_email = ttk.Entry(register_window)
    entry_phone = ttk.Entry(register_window)
    register_window.grab_set()

    var_root = tk.StringVar(value='0')
    check_root = ttk.Checkbutton(register_window, text="root", variable=var_root)

    button_register = ttk.Button(register_window, text="Зарегистрироваться", command=on_register)

    label_name.grid(row=1, column=0, padx=10, pady=1, sticky='ew')
    entry_name.grid(row=1, column=1, padx=10, pady=1, sticky='ew')
    
    label_pass.grid(row=2, column=0, padx=10, pady=1, sticky='ew')
    entry_pass.grid(row=2, column=1, padx=10, pady=1, sticky='ew')

    label_gender.grid(row=3, column=0, padx=10, pady=1, sticky='w')

    male_radio = ttk.Radiobutton(register_window, text='М', variable=var_gender, value='m')
    male_radio.grid(row=3, column=1, padx=10, pady=1, sticky='w')

    female_radio = ttk.Radiobutton(register_window, text='Ж', variable=var_gender, value='f')
    female_radio.grid(row=3, column=1, padx=10, pady=1)

    label_age.grid(row=4, column=0, padx=10, pady=1, sticky='w')
    entry_age.grid(row=4, column=1, padx=10, pady=1,)
    entry_age.bind("<KeyRelease>", is_valid_age)

    label_email.grid(row=5, column=0, padx=10, pady=1, sticky='w')
    entry_email.grid(row=5, column=1, padx=10, pady=1)

    label_phone.grid(row=6, column=0, padx=10, pady=1, sticky='w')
    entry_phone.grid(row=6, column=1, padx=10, pady=1)
    entry_phone.bind("<KeyRelease>", is_valid_phone)

    
    button_register.grid(row=7, column=0, columnspan=2, pady=10)
    check_root.grid(row=7, column=1, sticky='e')

    message.grid(row=0,column=0, columnspan=2)


    register_window.mainloop()
