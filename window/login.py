import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from window.registration import register

def login(db_cursor):
    root = tk.Tk()
    root.title("Вход")
    Wheight = 220
    Wwidth =160
    root.geometry(f"{Wheight}x{Wwidth}+{int((screen_width-Wwidth)/2)}+{int(screen_height/2)}")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}+{int(screen_width/4)}+{int(screen_height/4)}")
    root.resizable(width=False, height=False)

    def on_login():
        username = entry_username.get()
        password = entry_password.get()

        db_cursor.execute(f"SELECT * FROM users WHERE username={username} AND password={password}")
        result = db_cursor.fetchone()

        if result:
            messagebox.showinfo("Вход", "Вход выполнен успешно!")
        else:
            messagebox.showerror("Ошибка", "Неправильный логин или пароль")

    label_username = ttk.Label(root, text="Логин:")
    label_password = ttk.Label(root, text="Пароль:")
    entry_username = ttk.Entry(root)
    entry_password = ttk.Entry(root, show="*")
    label_register = tk.Label(root, text="Регистрация", fg="blue", cursor="hand2")
    
    label_username.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    label_password.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entry_username.grid(row=0, column=1, padx=10, pady=10)
    entry_password.grid(row=1, column=1, padx=10, pady=10)
    label_register.grid(row=3, column=1, padx=0, pady=10, sticky="se")
    label_register.bind("<Button-1>", lambda event: register(db_cursor))
    button_login = tk.Button(root, text="Вход", command=on_login)
    button_login.grid(row=2, column=0, columnspan=2, pady=10)


    root.mainloop()
