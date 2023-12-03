from tkinter import ttk
from window.__window import Window
from side_func import read_config
from query.connect_to_db import query
from datetime import datetime

def create_history_bets(user):
    def win_los(winner):
        current_date = datetime.now()
        bets =query(f"SELECT * FROM Bets WHERE user_id = {user}")

        participants = []
        for bet in bets:
            race_id, jockey_id, horse_id, bets_size,_ = bet[1], bet[2], bet[3], bet[5],bet[4]
            date=query(f'''SELECT date FROM races where race_id='{race_id}';''')[0][0]
            jockey_name=query(f'''SELECT name FROM jockeys WHERE jockey_id={jockey_id}''')[0][0]
            horse_name=query(f'''SELECT name FROM horses WHERE horse_id={horse_id}''')[0][0]
            
            participants.append((race_id, jockey_id, horse_id, jockey_name, horse_name, bets_size, date))
            
        results=[]
        for participant in participants:
            
            race_id, jockey_id, horse_id, date_string= participant[0], participant[1], participant[2], participant[6]
            
            result = query(f"SELECT winner FROM RaceParticipants WHERE race_id = {race_id} AND jockey_id = {jockey_id} AND horse_id = {horse_id}")
            date_object = datetime.strptime(date_string, "%Y-%m-%d")
            if result and result[0][0] == winner and date_object < current_date:
                results.append((participant[0],participant[3],participant[4],participant[5],participant[6]))
        return results
    
    
    root = Window(title="Создание новой ставки",
                  size=[520,340],
                  pos=[int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-260,
                  int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-170],
                  resize=[0,0],
                  rows=4,
                  user_id=user)
    
    root.win = ttk.Label(root, text='Победившие ставки', anchor='center')
    root.win.grid(row=1, column=0, columnspan=2, sticky="ew")
    
    root.table = ttk.Treeview(root, columns=("race_id", "jockey", "horse", "bet_size", "date"), show="headings")
    root.table.heading("race_id", text="ID гонки")
    root.table.heading("jockey", text="Жокей")
    root.table.heading("horse", text="Лошадь")
    root.table.heading("bet_size", text="Размер ставки")
    root.table.heading("date", text="Дата заезда")
    
    data = win_los(1)

    for row in data:
        root.table.insert("", "end", values=row)

    root.table.column("race_id", anchor="center", width=55, stretch="no")
    root.table.column("jockey", anchor="w", width=150, stretch="no")
    root.table.column("horse", anchor="w", width=100, stretch="no")
    root.table.column("bet_size", anchor="e", width=90, stretch="no")
    root.table.column("date", anchor="center", width=100, stretch="no")

    root.table.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=(5, 0))
    
    root.scrollbar = ttk.Scrollbar(root, orient="vertical", command=root.table.yview)
    root.scrollbar.grid(row=2, column=2, rowspan=2, sticky="ns")
    root.table.configure(yscrollcommand=root.scrollbar.set)
    
    root.table.config(height=5)

# ---------------------------------

    root.lose = ttk.Label(root, text='Проигравшие ставки', anchor='center')
    root.lose.grid(row=3, column=0, columnspan=2, sticky="ew")

    root.table2 = ttk.Treeview(root, columns=("race_id", "jockey", "horse", "bet_size", "date"), show="headings")
    root.table2.heading("race_id", text="ID гонки")
    root.table2.heading("jockey", text="Жокей")
    root.table2.heading("horse", text="Лошадь")
    root.table2.heading("bet_size", text="Размер ставки")
    root.table2.heading("date", text="Дата заезда")
    
    data2 = win_los(0)

    for row in data2:
        root.table2.insert("", "end", values=row)

    root.table2.column("race_id", anchor="center", width=55, stretch="no")
    root.table2.column("jockey", anchor="w", width=150, stretch="no")
    root.table2.column("horse", anchor="w", width=100, stretch="no")
    root.table2.column("bet_size", anchor="e", width=90, stretch="no")
    root.table2.column("date", anchor="center", width=100, stretch="no")

    root.table2.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=(5, 0))
    
    root.scrollbar2 = ttk.Scrollbar(root, orient="vertical", command=root.table2.yview)
    root.scrollbar2.grid(row=4, column=2, rowspan=2, sticky="ns")
    root.table2.configure(yscrollcommand=root.scrollbar2.set)
    
    root.table2.config(height=5)