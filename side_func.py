from configparser import ConfigParser


def read_config(filename, section):
    """Функция предназначена для получения данных с кофигурационного файла

    Args:
        filename (str): Расположение *.ini.

        section (str): Название секции в *.ini. 
        
    Returns:
        dict: словарь с данными
    """
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    for name, value in parser.items(section):
        config[name] = value
    return config