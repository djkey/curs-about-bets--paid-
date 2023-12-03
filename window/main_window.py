# from tkinter import *
from tkinter import ttk
from window.__window import Window
from side_func import read_config
from query.connect_to_db import query
from window.new_bet import create_new_bet
from window.history_bets import create_history_bets
from window.info import create_info

class mainWindow(Window):
    def update(self, event):
        super(mainWindow, self).update(event)
        for row in self.table.get_children():
            self.table.delete(row)

        data = query(f'''SELECT bets.race_id, jockeys.name as Jockey, horses.name as Horse, bet_size, races.date
                        FROM bets
                        JOIN jockeys ON bets.jockey_id = jockeys.jockey_id
                        JOIN horses ON bets.horse_id = horses.horse_id
                        JOIN races ON bets.race_id = races.race_id 
                        WHERE user_id={self.user_id} AND races.date >= date("now")''')
        for row in data:
            self.table.insert("", "end", values=row)
            
def create_main_window(user):
    
    root = mainWindow(
        title='Курсова ведення обліку ставок на іподромі',
        size=[700,325],
        pos=[int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-290,
              int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-160],
        rows=3,
        user_id=user
    )

    root.button1 = ttk.Button(root, text="Нова ставка", command=lambda: button_clicked(1))
    root.button2 = ttk.Button(root, text="Історія ставок", command=lambda: button_clicked(2))
    root.button3 = ttk.Button(root, text="База знань", command=lambda: button_clicked(3))

    root.button1.grid(row=1, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)
    root.button2.grid(row=2, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)
    root.button3.grid(row=3, column=0, sticky="ew", padx=15, pady=15, ipadx=30, ipady=20)


            
    def button_clicked(button_number):

        match button_number:
            case 1:
                create_new_bet(user)
            case 2:
                create_history_bets(user)
                root.update(None)
            case 3:
                create_info(user)

    root.table = ttk.Treeview(root, columns=("race_id", "jockey", "horse", "bet_size", "date"), show="headings")
    root.table.heading("race_id", text="ID гонки")
    root.table.heading("jockey", text="Жокей")
    root.table.heading("horse", text="Коні")
    root.table.heading("bet_size", text="Розмір ставки")
    root.table.heading("date", text="Дата заїздів")
    
    data = query(f'''SELECT bets.race_id, jockeys.name as Jockey, horses.name as Horse, bet_size, races.date
                     FROM bets
                     JOIN jockeys ON bets.jockey_id = jockeys.jockey_id
                     JOIN horses ON bets.horse_id = horses.horse_id
                     JOIN races ON bets.race_id = races.race_id 
                     WHERE user_id={user} AND races.date >= date("now")''')

    for row in data:
        root.table.insert("", "end", values=row)

    root.table.column("race_id", anchor="center", width=55, stretch="no")
    root.table.column("jockey", anchor="w", width=150, stretch="no")
    root.table.column("horse", anchor="w", width=100, stretch="no")
    root.table.column("bet_size", anchor="e", width=90, stretch="no")
    root.table.column("date", anchor="center", width=100, stretch="no")

    root.table.grid(row=1, column=1, rowspan=3, sticky="nsew")

    # scrollbar = ttk.Scrollbar(orient="vertical", command=root.table.yview)
    # scrollbar.pack(side='right', fill='y')
    
    root.scrollbar = ttk.Scrollbar(root, orient="vertical", command=root.table.yview)
    root.scrollbar.grid(row=1, column=2, rowspan=3, sticky="ns")
    root.table.configure(yscrollcommand=root.scrollbar.set)

    root.mainloop()



 