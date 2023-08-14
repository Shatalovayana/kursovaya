import json
from datetime import datetime


def load_operations(filename):
    """Функция загружает операции из файла .json"""
    with open(filename, 'r', encoding="utf-8") as file:
        operations = json.load(file)
        return operations


def executed_operations(lst):
    """Выбирает словарь со статусом executed и добавляет его в новый список"""
    executed_list = []
    for k in lst:
        if k.get('state') == 'EXECUTED':
            executed_list.append(k)
        else:
            continue
    return sorted(executed_list, key=lambda x: x['date'], reverse=True)


def date_operations(dictionary):
    """Функция оформляет даты в требующемся формате"""
    new_date, time = dictionary['date'].split('T')
    date_obj = datetime.strptime(new_date, '%Y-%m-%d')
    # преобразуется обратно в строку с помощью метода strftime()
    return date_obj.strftime('%d.%m.%Y')


def get_card_number_from(dictionary):
    """Функция зашифровывает номер карты отправителя"""
    if 'from' not in dictionary:
        secret_number = "No information"
    else:
        if 'Счет' in dictionary['from']:
            numbers = '**' + dictionary['from'][-4:]
            secret_number = dictionary['from'][:-20] + numbers
        else:
            card_number = dictionary['from'][-16:]
            coding_card = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
            secret_number = dictionary['from'][:-16] + coding_card
    return secret_number


def get_card_number_to(dictionary):
    """Функция зашифровывает номер карты получателя"""
    if 'to' not in dictionary:
        secret_number = "No information"
    else:
        if 'Счет' in dictionary['to']:
            numbers = '**' + dictionary['to'][-4:]
            secret_number = dictionary['to'][:-20] + numbers
        else:
            card_number = dictionary['to'][-16:]
            coding_card = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
            secret_number = dictionary['to'][:-16] + coding_card
    return secret_number


def get_amount(amount_info):
    """Функция возвращает сумму и валюту конкретной операции"""
    amount = amount_info['amount']
    currency = amount_info['currency']['name']
    return f'{amount} {currency}'


def print_bank_info(operation_info):
    """Функция печатает необходимую информацию, согласно заданию"""
    print(f'{date_operations(operation_info)} {operation_info["description"]}\n'
          f'{get_card_number_from(operation_info)} -> {get_card_number_to(operation_info)}\n'
          f'{get_amount(operation_info["operationAmount"])}\n')


#for i in executed_operations(load_operations("operations.json")):
    #print(get_card_number_to(i))


#print(executed_operations(load_operations('operations.json')))
#print(load_operations('operations.json'))
#print(date_operations())
