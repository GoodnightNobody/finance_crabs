

def bool_valid(value:str):
        yes = ['y', 'Y', 'yes', 'Yes', 'Да', 'да']
        no = ['n', 'N', 'no', 'No', 'нет', 'Нет']
        if value in yes:
            return True
        elif value in no:
            return False


def size_valid(value:str):
    size = ['s', 'm', 'l']
    if value.lower() in size:
        return value.lower()
    else:
        return None


def kilo_valid(value):
    try:
        value = float(value)
    except ValueError as e:
        return e
    finally:
        return value
