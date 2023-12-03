import tkinter as tk
from tkinter import ttk
from window.__window import Window
from side_func import read_config
from query.connect_to_db import query


def create_new_bet(user):
    root = Window(title="Создание новой ставки",
                  size=[300,200],
                  pos=[int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-150,
                  int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-100],
                  resize=[0,0],
                  rows=5,
                  user_id=user)
    
    
    ttk.Label(root, text="Выберите гонку:").grid(row=1, column=0, padx=10, pady=5)
    ttk.Label(root, text="Выберите участника:").grid(row=2, column=0, padx=10, pady=5)
    ttk.Label(root, text="Размер ставки:").grid(row=3, column=0, padx=10, pady=5)
    ttk.Label(root, text="Возможный выигрыш:").grid(row=4, column=0, padx=10, pady=5)
    root.cooficient = ttk.Label(root, text="")
    root.cooficient.grid(row=4, column=1, padx=10, pady=5)
    
    root.max_chance= 0
    root.coof = 0
    
    races_data=query('''select * 
                        from races
                        where date >= date("now")
                        ORDER BY date''')

    
    def select_race(event):
        root.max_chance=0
        root.participants=query(f'''select jockeys.name, horses.name 
                               from RaceParticipants
                               JOIN jockeys ON RaceParticipants.jockey_id = jockeys.jockey_id
                               JOIN horses ON RaceParticipants.horse_id = horses.horse_id
                               where race_id={root.race_id_combobox.get().split(' ', maxsplit=1)[0]}''')
        
        for getter in root.participants:
            root.max_chance += query(f'''SELECT COUNT(*) FROM RaceParticipants
                                JOIN jockeys ON RaceParticipants.jockey_id = jockeys.jockey_id
                                JOIN horses ON RaceParticipants.horse_id = horses.horse_id
                                WHERE RaceParticipants.winner = 1 AND (jockeys.name = '{getter[0]}' OR horses.name = '{getter[1]}')''')[0][0]

        root.participant_combobox.set('')
        root.participant_combobox['values'] = [f"{par[0]} - {par[1]}" for par in root.participants]

    root.race_id_combobox = ttk.Combobox(root, values=races_data, state="readonly")
    root.race_id_combobox.grid(row=1, column=1, padx=0, pady=5)
    root.race_id_combobox.bind("<<ComboboxSelected>>",select_race)
    
    def select_participant(event):
        getter = root.participant_combobox.get().split(' - ', maxsplit=1)
        root.chance = query(f'''SELECT COUNT(*) FROM RaceParticipants
                        JOIN jockeys ON RaceParticipants.jockey_id = jockeys.jockey_id
                        JOIN horses ON RaceParticipants.horse_id = horses.horse_id
                        where RaceParticipants.winner == 1 and jockeys.name = '{getter[0]}' or RaceParticipants.winner == 1 and horses.name = '{getter[1]}';''')[0][0]
    
        root.coof = round(root.chance/root.max_chance, 2) + 1
        
    root.participant_combobox = ttk.Combobox(root, values=[], state="readonly")
    root.participant_combobox.grid(row=2, column=1, padx=0, pady=5)
    root.participant_combobox.bind("<<ComboboxSelected>>",select_participant)
    
    def on_validate(P, V, W):
        if P.isdigit() and int(P)<=root.wallet:
            root.cooficient.config(text=int(int(P)*root.coof))
            return True
        else:
            if P == '':
                root.cooficient.config(text='')
                return True
            else:
                root.bell()
                return False
    
    root.bet_size_entry = ttk.Entry(root, validate="key", validatecommand=(root.register(on_validate), '%P', '%V', '%W'))
    root.bet_size_entry.grid(row=3, column=1, padx=0, pady=5)
    
    def confirm_bet():
        race_id = root.race_id_combobox.get().split(' ', maxsplit=1)[0]
        participant = query(f'''SELECT RaceParticipants.jockey_id, RaceParticipants.horse_id FROM RaceParticipants
                                JOIN jockeys ON RaceParticipants.jockey_id = jockeys.jockey_id
                                JOIN horses ON RaceParticipants.horse_id = horses.horse_id
                                where  jockeys.name = '{root.participant_combobox.get().split(' - ')[0]}' 
                                and horses.name = '{root.participant_combobox.get().split(' - ')[1]}'
                                and race_id={race_id};''')
        jockey = participant[0][0]
        horse = participant[0][1]
        bet_size = root.bet_size_entry.get()
        
        query(f'''insert into Bets (race_id, jockey_id, horse_id, user_id, bet_size) 
              values ({race_id}, '{jockey}', '{horse}', {user}, {int(int(bet_size)*root.coof)});''')
        query(f'''UPDATE users SET wallet = {int(root.wallet-int(bet_size))} WHERE user_id = {user};''')
        root.destroy()

    ttk.Button(root, text="Подтвердить ставку", command=confirm_bet).grid(row=5, column=0, columnspan=2, pady=5)


    