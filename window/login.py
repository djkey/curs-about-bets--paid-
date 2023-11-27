from tkinter import ttk
from query.connect_to_db import query
from window.__window import Window
from window.registration import register
from window.main_window import create_main_window
from side_func import read_config


def login():
    root = Window(title='login',
                  size= [220, 160],
                  pos= [int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-110,
                        int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-80],
                  resize=[0, 0],
                  rows= 4)

    
    root.info = ttk.Label(root)
    root.info.grid(row= 0, column=0, columnspan=2)
    root.username_label = ttk.Label(root, text='Login').grid(row=1, column=0, padx=10, pady=10, sticky='W')
    root.username_entry = ttk.Entry(root)
    root.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky='W')
    root.password_label = ttk.Label(root, text='Password').grid(row=2, column=0, padx=10, pady=10)
    root.password_entry = ttk.Entry(root, show='*')
    root.password_entry.grid(row=2, column=1, padx=10, pady=10)
    

    def on_login():
        username = root.username_entry.get()
        password = root.password_entry.get()

        result = query(f"SELECT user_id FROM users WHERE name='{username}' AND password='{password}'")
        if result:
            root.destroy()  
            create_main_window()
            pass
        else:
            root.info.config(text='Ошибка!')
        
    def on_register():
        register()
        # переход к регистрации
    
    
    root.login_button = ttk.Button(root, text="Войти", command=on_login).grid(row=3, columnspan=2)

    root.label_register = ttk.Label(root, text="Регистрация", foreground="blue", cursor="hand2")
    root.label_register.grid(row=4, column=1, padx=10, pady=10, sticky="se")
    root.label_register.bind("<Button-1>", lambda event: on_register())



    root.mainloop()
