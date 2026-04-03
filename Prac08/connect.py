import psycopg2  # Библиотека для работы с базой данных PostgreSQL
from config import load_config # Импорт твоей функции из предыдущего файла(сonfig.py)

def connect(config):
    """ Устанавливает соединение с сервером базы данных PostgreSQL """
    try:
        # Оператор 'with' гарантирует, что соединение закроется автоматически,
        # даже если произойдет ошибка. 
        # '**config' — это "распаковка" словаря. Программа превращает {'user': 'admin'} 
        # в аргумент user='admin' для функции connect.
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.') # Сообщение об успехе
            return conn # Возвращаем объект соединения для дальнейшей работы (чтения/записи данных)

    except (psycopg2.DatabaseError, Exception) as error:
        # Если пароль неверный, база отключена или нет интернета — сработает этот блок
        print(error) 

if __name__ == '__main__':
    # 1. Сначала загружаем настройки (словарь с данными из .ini)
    config = load_config() 
    # 2. Передаем эти настройки функции соединения
    connect(config)