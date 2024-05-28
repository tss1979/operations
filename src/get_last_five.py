def get_last_five(data=None):
    if data is None:
        return []
    if len(data) > 5:
        return data[len(data) - 5:]
    elif len(data) != 0:
        print('В отправленном файле меньше 5 записей')
        return data
    else:
        print('Данные отсутствуют')
        return []