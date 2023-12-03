from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from query.connect_to_db import query
import os


class Window(Tk):
    def __init__(self,
                 title = 'new_window',
                 size = [300, 200],
                 pos = [500, 100],
                 resize = [1,1],
                 minsize = [200, 100],
                 rows = 1,
                 user_id = 0):
        """Класс для работы с окном

        Args:
            title (str, optional): Имя окна. Defaults to 'new_window'.
            
            size (list, optional): Размер окна. Defaults to [300, 200].
            
            pos (list, optional): Позиция окна. Defaults to [500, 100].
            
            resize (list, optional): Можно ли изменять окно. Defaults to [1,1].
            
            minsize (list, optional): Минимальный размер окна. Defaults to [200, 100].
            
            rows (int, optional): Количество строк обьектов. Defaults to 1.
            
            user_id (int, optional): ID пользователя. Defaults to 0.
        """
        self.user_id=user_id
        super().__init__()
        self.title(title)
        self.resizable(resize[0], resize[1])
        self.iconbitmap(default="./picture/icon.ico")
        self.minsize(minsize[0],minsize[1])
        self.geometry(f"{size[0]}x{size[1]}+{pos[0]}+{pos[1]}")

        if self.user_id:
            # определение шапки
            self.upper = ttk.Label(self, text=f'Привіт, {query(f'''SELECT name FROM users WHERE user_id={self.user_id}''')[0][0]}')
            self.upper.grid(row=0, column=0, sticky="w", pady=0)
            
            self.wallet = query(f'''SELECT wallet FROM users WHERE user_id= {self.user_id}''')[0][0]
            self.upper_rig = ttk.Label(self, text=f'{self.wallet} ₴', foreground='blue', width=10)
            self.upper_rig.grid(row=0, column=1, sticky="e", pady=0)
            self.upper_rig.bind("<Button-1>", self.show_entry_dialog)
            
            
            self.button_rig = ttk.Button(self, text='↻', width=2)
            self.button_rig.grid(row=0, column=1, sticky="e", pady=0)
            self.button_rig.bind("<Button-1>", self.update)
            
            # определение подвала
            self.lower = ttk.Label(self, text='something')
            self.lower.grid(row=rows+1, column=0, sticky="ew")
            self.check_db_status()

    def show_entry_dialog(self, event):
        result = simpledialog.askstring(" ", "На сколько пополнить:")
        if result is not None:  
            self.wallet += int(result)
            print(self.wallet)
            query(f"UPDATE users SET wallet = {self.wallet} WHERE user_id = {self.user_id}")
            self.upper_rig.config(text=f'{self.wallet} ₴')

    def update(self, event):
        self.wallet=query(f'''SELECT wallet FROM users WHERE user_id={self.user_id}''')[0][0]
        self.upper_rig.config(text=f'{self.wallet} ₴')
        self.check_db_status()
        
    def check_db_status(self):
        if os.path.exists('db/curs.db'):
            try:
                query("SELECT 1") 
                self.update_db_status('OK')
            except Exception as e:
                self.update_db_status('Error')
        else:
            self.update_db_status('Not found')

    def update_db_status(self, status='OK'):
        self.lower.config(text=f'DB status: {status}')
    
    def __del__(self):
        print("Экземпляр удален")