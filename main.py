import configparser
from tkinter import *
from window.login import login
from window.main_window import create_main_window

def get_screen_size():
    """Определение размера экрана

    Returns:    
    int, int: Ширина, высота
    """
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height

def update_config_file(width, height, file = 'config.ini', section = 'Screen size'):
    """Запись параметров в *.ini файл

    Args:
        width (int): Ширина.
        
        height (int): Высота.
        
        file (str): В какой файл идет запись. Defaults to 'config.ini'.
        
        section (str): В какую секцию идет запись. Defaults to 'Screen size'.
    """
    config = configparser.ConfigParser()
    config.read(file)

    try:
        config.add_section(section)
    except (configparser.DuplicateSectionError):
        print(f"Error: section '{section}' already exist.")
        
    config.set(section, 'Width', str(width))
    config.set(section, 'Height', str(height))

    with open(file, 'w') as configfile:
        config.write(configfile)
        print(f"{file} file has been updated.")


if __name__ == "__main__":
    width, height = get_screen_size()
    update_config_file(width, height)
    
    login()
