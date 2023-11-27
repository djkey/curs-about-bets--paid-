# from tkinter import *
from tkinter import ttk
from window.__window import Window
from side_func import read_config



def create_main_window():
    root = Window(
        title='Курсова ведення обліку ставок на іподромі',
        size=[int(int(read_config(filename='config.ini', section='Screen size')['width'])/2),
              int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)],
        pos=[int(int(read_config(filename='config.ini', section='Screen size')['width'])/4),
              int(int(read_config(filename='config.ini', section='Screen size')['height'])/4)],
        rows=3,
        user_id=1
    )

    root.left_frame = ttk.Frame(root, padding=10)
    root.left_frame.grid(row=0, column=0, sticky="nsw")

    root.button1 = ttk.Button(root, text="Кнопка 1", command=lambda: button_clicked(1))
    root.button2 = ttk.Button(root, text="Кнопка 2", command=lambda: button_clicked(2))
    root.button3 = ttk.Button(root, text="Кнопка 3", command=lambda: button_clicked(3))

    root.button1.grid(row=1, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)
    root.button2.grid(row=2, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)
    root.button3.grid(row=3, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)

    root.right_frame = ttk.Frame(root, padding=10)
    root.right_frame.grid(row=0, column=1, sticky="nse")

    # пример таблицы
    table = ttk.Treeview(root, columns=("Name", "Age", "Country"), show="headings")
    table.heading("Name", text="Имя")
    table.heading("Age", text="Возраст")
    table.heading("Country", text="Страна")

    data = [("John", 25, "USA"), ("Anna", 30, "Canada"), ("Tom", 22, "UK")]
    for row in data:
        table.insert("", "end", values=row)

    for column in ("Name", "Age", "Country"):
        table.column(column, anchor="center", width=100, stretch="no")

    table.grid(row=1, column=1, rowspan=3, sticky="nsew")

    # root.columnconfigure(0, weight=1)
    # root.columnconfigure(1, weight=1)
    # root.rowconfigure(1, weight=1)
    root.mainloop()

def button_clicked(button_number):
    print(f"Кнопка {button_number} нажата")


 