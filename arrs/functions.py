import datetime
import json


def get_data(path: str) -> list[dict]:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


# class Functions:
def get_executed_operations(operations: list[dict]) -> list[dict]:
    executed_operations = list()
    for operation in operations:
        if operation.get('state') == "EXECUTED":
            executed_operations.append(operation)
    return executed_operations


def get_key(operation):
    return operation['date']


def get_recent_five_operations(executed_operations: list[dict]) -> list[dict]:
    return list(sorted(executed_operations, key=get_key, reverse=True))[:5]


def convert_time(date: str) -> str:
    date_time = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.datetime.strftime(date_time, '%d.%m.%Y')


def convert_payment_dir(direction: str) -> str:
    if direction.startswith('Счет'):
        return f'Счет {direction[5:9]} {direction[9:11]}** ***{direction[-4:]}'
    card_dir = direction.split(' ')[-1]
    name_of_card = direction.split(" ")[:-1]
    return f'{" ".join(name_of_card)} {card_dir[:4]} {card_dir[4:6]}** ***{card_dir[-4:]}'


def validate_operation(operation: dict) -> str:
    date = convert_time(operation['date'])
    from_ = convert_payment_dir(operation['from']) if operation.get('from') else 'неизвестный'
    to_ = f"**{operation['to'].split(' ')[-1][-4:]}"

    return f"{date} {operation['description']}\n{from_} -> " \
           f"{to_}\n{operation['operationAmount']['amount']} " \
           f"{operation['operationAmount']['currency']['name']}\n"
