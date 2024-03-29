import os
import json


def load_operations(filename):
    """
    Загружает информацию из файла
    """
    with open(file=os.path.abspath(filename), mode='r', encoding='utf-8') as file:
        return json.load(file)


def sort_operations(operations):
    """
    Принимает список словарей
    и сортирует операции по дате
    """
    new_operations = []
    for operation in operations:
        if len(operation) != 0:
            if operation.get('date') is not None:
                new_operations.append(operation)
    new_operations = sorted(new_operations, key=lambda new_operations: new_operations['date'], reverse=True)
    return new_operations


def filter_operations(operations):
    """
    Фильтрует операции по state: EXECUTED
    """
    new_operations = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            new_operations.append(operation)
    return new_operations


def cut_operations(operations):
    """
    Обрезает первые 5 операций
    """
    new_operations = operations[0:5]
    return new_operations


def formatter_date(date):
    """
    Перевод даты в нужный формат: из 2019-10-14 в 14.10.2018
    """
    old_format_date = date[:10]
    split_date = old_format_date.split("-")
    new_format_date = ".".join(split_date[::-1])
    return new_format_date


def mask_account(account):
    """
    Получение значения описания операции.
    Например, "Перевод организации"
    """
    if account is not None:
        my_op_is_from_to = account.split(" ")
        letters = my_op_is_from_to[0]

        if my_op_is_from_to[1].isdigit():
            digits = my_op_is_from_to[1]
        else:
            letters = letters + " " + my_op_is_from_to[1]
            digits = my_op_is_from_to[2]

        if len(digits) == 16:
            digits = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
        elif len(digits) == 20:
            digits = f"**{digits[-4:]}"
        return letters + " ", digits + " "

    else:
        return '', ''


def print_result():
    """
    Печать итогового результата работы программы
    """
    operations = load_operations('operations.json')
    operations = filter_operations(operations)
    operations = sort_operations(operations)
    operations = cut_operations(operations)
    for operation in operations:
        try:
            print(f"\n{formatter_date(operation['date'])} {operation['description']}\n"
                  f"{mask_account(operation.get('from'))[0]}{mask_account(operation.get('from'))[1]}-> "
                  f"{mask_account(operation.get('to'))[0]}{mask_account(operation.get('to'))[1]}\n"
                  f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
        except KeyError:
            operation['date'] = None
            operation['from'] = None
            operation['to'] = None
            operation['operationAmount']['amount'] = None
            operation['operationAmount']['currency']['name'] = None
    return 0
