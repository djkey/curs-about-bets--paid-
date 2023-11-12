from tkinter import *
from tkinter import ttk



def create_main_window():
    root = Tk()
    root.title("Курсова ведення обліку ставок на іподромі")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{int(screen_width/2)}x{int(screen_height/2)}+{int(screen_width/4)}+{int(screen_height/4)}")

    left_frame = ttk.Frame(root, padding=10)
    left_frame.grid(row=0, column=0, sticky="nsw")

    button1 = ttk.Button(left_frame, text="Кнопка 1", command=lambda: button_clicked(1))
    button2 = ttk.Button(left_frame, text="Кнопка 2", command=lambda: button_clicked(2))
    button3 = ttk.Button(left_frame, text="Кнопка 3", command=lambda: button_clicked(3))

    button1.grid(row=0, column=0, sticky="ew", pady=5)
    button2.grid(row=1, column=0, sticky="ew", pady=5)
    button3.grid(row=2, column=0, sticky="ew", pady=5)

    right_frame = ttk.Frame(root, padding=10)
    right_frame.grid(row=0, column=1, sticky="nsew")

    # пример таблицы
    table = ttk.Treeview(right_frame, columns=("Name", "Age", "Country"), show="headings")
    table.heading("Name", text="Имя")
    table.heading("Age", text="Возраст")
    table.heading("Country", text="Страна")

    data = [("John", 25, "USA"), ("Anna", 30, "Canada"), ("Tom", 22, "UK")]
    for row in data:
        table.insert("", "end", values=row)

    for column in ("Name", "Age", "Country"):
        table.column(column, anchor="center", width=100, stretch=tk.NO)

    table.grid(row=0, column=0, sticky="nsew")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()

def button_clicked(button_number):
    print(f"Кнопка {button_number} нажата")

 