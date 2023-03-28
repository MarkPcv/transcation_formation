from utils import transaction

# Create global variables of Transaction class
trans1 = transaction.Transaction(
                    "2019-08-26T10:50:58.294041",
                    "Перевод организации",
                    "Счет 64686473678894779589",
                    "31957.58",
                    "руб.",
                    source="Maestro 1596837868705199"
                    )

trans2 = transaction.Transaction(
                    "2018-06-30T02:08:58.425572",
                    "Перевод организации",
                    "Счет 64686473678894779589",
                    "9824.07",
                    "USD",
                    source="Счет 75106830613657916952",
                    )

trans3 = transaction.Transaction(
                    "2018-03-23T10:45:06.972075",
                    "Открытие вклада",
                    "Счет 41421565395219882431",
                    "48223.05",
                    "руб."
                    )

# Test Transaction class methods
# Test get_source function
def test_get_source():
    assert trans2.get_source() == "Счет **6952"
    assert trans3.get_source() == "Н/П"

# Test get_destination function
def test_get_destination():
    assert trans1.get_destination() == "Счет **9589"

# Test get_date function
def test_get_date():
    assert trans3.get_date() == "23.03.2018"

# Test show_details function
def test_show_details():
    assert trans2.show_details() == ("30.06.2018 Перевод организации\n"
                                    "Счет **6952 -> Счет **9589\n"
                                    "9824.07 USD\n")

    assert trans3.show_details() == ("23.03.2018 Открытие вклада\n"
                                     "Н/П -> Счет **2431\n"
                                     "48223.05 руб.\n")

# Test print of the class Transaction
def test_print():
    assert trans1.__repr__() == (
        "Дата транзакции: 2019-08-26T10:50:58.294041\n"
        "Описание транзакции: Перевод организации\n"
        "От: Maestro 1596 83** **** 5199\n"
        "Куда: Счет **9589\n"
        "Сумма: 31957.58\n"
        "Валюта: руб.\n"
    )

# Test function hide_information
def test_hide_card():
    card_number = "Maestro 1596837868705199"
    assert transaction.hide_information(card_number) == \
           "Maestro 1596 83** **** 5199"

def test_hide_account():
    account_number = "Счет 64686473678894779589"
    assert transaction.hide_information(account_number) == \
           "Счет **9589"

