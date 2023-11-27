from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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
        super().__init__()
        self.title(title)
        self.resizable(resize[0], resize[1])
        self.iconbitmap(default="./picture/icon.ico")
        self.minsize(minsize[0],minsize[1])
        self.geometry(f"{size[0]}x{size[1]}+{pos[0]}+{pos[1]}")


        if user_id:
            # определение шапки
            self.upper = ttk.Label(self, text=f'{user_id} user', width=1)
            self.upper.grid(row=0, column=0, sticky="ew", pady=0)
            
            # определение подвала
            self.lower = ttk.Label(self, text='something')
            self.lower.grid(row=rows+1, column=0, sticky="ew")


    def __del__(self):
        print("Экземпляр удален")