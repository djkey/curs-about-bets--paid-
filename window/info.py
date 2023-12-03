from tkinter import ttk
from tkinter import Frame
from query.connect_to_db import query
from window.__window import Window
from side_func import read_config





def create_info(user):
            
            
    info = Window(title='База знань',
                  size= [600, 300],
                  pos= [int(int(read_config(filename='config.ini', section='Screen size')['width'])/2)-300,
                        int(int(read_config(filename='config.ini', section='Screen size')['height'])/2)-150],
                  resize=[0, 0],
                  rows= 4,
                  user_id=user)
    
    def show_table(event,var):
        if var==1:
            info.table1.grid(row=1, column=1, rowspan=3)
            info.table2.grid_forget()
            info.table3.grid_forget()
        if var==2:
            info.table1.grid_forget()
            info.table2.grid(row=1, column=1, rowspan=3)
            info.table3.grid_forget()
        if var==3:
            info.table1.grid_forget()
            info.table2.grid_forget()
            info.table3.grid(row=1, column=1, rowspan=3)
        info.scrollbar1.grid(row=1, column=2, rowspan=3, sticky="ns")
        info.scrollbar2.grid(row=4, column=1, columnspan=3, sticky="ew")
            
    
    info.label1 = ttk.Label(info, text="Жокеї", cursor="hand2", foreground='blue')
    info.label1.grid(row=1, column=0, pady=30)
    info.label1.bind("<Button-1>", lambda event: show_table(event, 1))
        
    info.label2 = ttk.Label(info, text="Коні", cursor="hand2", foreground='blue')
    info.label2.grid(row=2, column=0, pady=30)
    info.label2.bind("<Button-1>", lambda event: show_table(event, 2))
    
    info.label3 = ttk.Label(info, text="Гонки", cursor="hand2", foreground='blue')
    info.label3.grid(row=3, column=0, pady=30)
    info.label3.bind("<Button-1>", lambda event: show_table(event, 3))



    info.table1 = ttk.Treeview(info, columns=("jockey_id", "name", "gender", "age", "description"))
    info.table1["show"] = "headings"
    info.table1.heading("jockey_id", text="#")
    info.table1.heading("name", text="І'мя")
    info.table1.heading("gender", text="Стать")
    info.table1.heading("age", text="Вік")
    info.table1.heading("description", text="Опис")
    
    data = query(f'''SELECT *
                     FROM jockeys''')

    for row in data:
        info.table1.insert("", "end", values=row)

    info.table1.column("jockey_id", anchor="center", width=30)
    info.table1.column("name", anchor="w", width=150, stretch="no")
    info.table1.column("gender", anchor="w", width=50, stretch="no")
    info.table1.column("age", anchor="w", width=60, stretch="no")
    info.table1.column("description", anchor="w", width=210, stretch="no")
    
    # --------------------------------------------------
    
    info.table2 = ttk.Treeview(info, columns=("horse_id", "name", "gender", "age", "description"))
    info.table2["show"] = "headings"
    info.table2.heading("horse_id", text="#")
    info.table2.heading("name", text="Кличка")
    info.table2.heading("gender", text="Стать")
    info.table2.heading("age", text="Вік")
    info.table2.heading("description", text="Опис")
    
    data = query(f'''SELECT horse_id, name, gender, age, description
                     FROM horses''')

    for row in data:
        info.table2.insert("", "end", values=row)

    info.table2.column("horse_id", anchor="center", width=30)
    info.table2.column("name", anchor="w", width=150, stretch="no")
    info.table2.column("gender", anchor="w", width=50, stretch="no")
    info.table2.column("age", anchor="w", width=60, stretch="no")
    info.table2.column("description", anchor="w", width=210, stretch="no")
    
    # --------------------------------------------------
    
    info.table3 = ttk.Treeview(info, columns=("race_id", "date"))
    info.table3["show"] = "headings"
    info.table3.heading("race_id", text="#")
    info.table3.heading("date", text="Дата",anchor='w')

    data = query(f'''SELECT *
                     FROM races''')

    for row in data:
        info.table3.insert("", "end", values=row)

    info.table3.column("race_id", anchor="center", width=30, stretch="no")
    info.table3.column("date", anchor="w", width=470, stretch="no")
    
    # --------------------------------------------------
    
    info.scrollbar1 = ttk.Scrollbar(info, orient="vertical")
    info.scrollbar2 = ttk.Scrollbar(info, orient="horizontal")
    info.table1.configure(yscrollcommand=info.scrollbar1.set, xscrollcommand=info.scrollbar2.set)
    info.table2.configure(yscrollcommand=info.scrollbar1.set, xscrollcommand=info.scrollbar2.set)
    info.table3.configure(yscrollcommand=info.scrollbar1.set)
    

    
