"""
data = str(input("Введите транзакцию"))  #   -500 (бензин 92)


def deconstructor_data(data):
    def which_type(data):
        if data[0] == '-':
            transaction_type = 'transaction out'
        elif data[0] == '+':
            transaction_type = 'transaction in'
        else:
            transaction_type = 'not valid'
        return transaction_type
    return which_type(data)

print(deconstructor_data(data))
"""
# Place to peewee models
