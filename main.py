from tkinter import *
from tkinter import ttk
import pymysql
from configparser import ConfigParser
from window.login import login
from window.main_window import create_main_window
 
def read_config(filename='config.ini', section='Database'):
    """Функция предназначена для получения данных с кофигурационного файла

    Args:
        filename (str): Расположение *.ini. Defaults to 'config.ini'.

        section (str): Название секции в *.ini. Defaults to 'Database'.

    Returns:
        dict: словарь с данными
    """
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    for name, value in parser.items(section):
        config[name] = value
    return config

def connect_to_database(config):
    """Функция нужна для подключения к MySQL

    Args:
        config (dict): словарь с параметрами для подключени к БД

    Returns:
        хз: Указатель на БД
        
        NONE: ошибка подключения
    """
    try:
        connection = pymysql.connect(**config)
        if connection.open:
            print("Connection: OK")
        return connection
    except pymysql.Error as err:
        print(f"ERROR: connection\n{err}")
        return None

def main():
    db_config = read_config()

    if db_config:
        
        connection = connect_to_database(db_config)
        db_cursor = connection.cursor()
        db_cursor.execute('SELECT VERSION()')
        rows = db_cursor.fetchall()
        
        for row in rows:
            print(row)
            
        if login(db_cursor):

            # после авторизации
            create_main_window()
            
            
            
        # конец программы 
        if connection:
            connection.close()
            print("connection: Close")
    else:
        print("ERROR: no configure")
    


if __name__ == "__main__":
    main()
