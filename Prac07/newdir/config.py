from configparser import ConfigParser #connecting library to work with files 

def load_config(filename='database.ini', section='postgresql'): #creating function that take two parametrs, postgresql(section to receive data )
    parser = ConfigParser() # объект parser, который умеет "читать" структуру ini-файлов.
    parser.read(filename) 

    # get section, default to postgresql
    config = {}
    if parser.has_section(section): #проверяет, существует ли в файле нужный заголовок (postgresql)
        params = parser.items(section) #превращает все строки в этой секции в список кортежей вида ('key', 'value')
        for param in params: #Цикл for переносит эти данные в словарь config, чтобы к ним было удобно обращаться по ключу.
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config #Функция возвращает заполненный словарь с настройками.

if __name__ == '__main__': #Блок if __name__ == '__main__': запускает код, 
#только если вы запускаете этот файл напрямую. Он вызывает функцию и печатает результат в консоль.
    config = load_config()
    print(config)







