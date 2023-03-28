from utils import data

# Test read_data function
def test_read_data():
    assert data.read_data()[0] == {
            'date': '2019-08-26T10:50:58.294041',
            'description': 'Перевод организации',
            'from': 'Maestro 1596837868705199',
            'id': 441945886,
            'operationAmount': {
                                'amount': '31957.58',
                                'currency': {
                                    'code': 'RUB',
                                    'name': 'руб.'}
                                },
            'state': 'EXECUTED',
            'to': 'Счет 64686473678894779589'
    }

# Test get_five function
def test_get_five():
    assert data.get_five()[0].__repr__() == (
        'Дата транзакции: 2019-08-26T10:50:58.294041\n'
        'Описание транзакции: Перевод организации\n'
        'От: Maestro 1596 83** **** 5199\n'
        'Куда: Счет **9589\nСумма: 31957.58\n'
        'Валюта: руб.\n'
    )