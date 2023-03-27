import json
from transaction import Transaction

def read_data():
    """
    Returns list of transactions retrieved from json file
    """
    text = ""
    # Open file retrieve each line
    with open("../data/operations.json", "r", encoding="utf-8") as file:
        for line in file:
            text += line.rstrip()
    # Return list of transactions
    return json.loads(text)


def get_five():
    """
    Returns a list of five executed transactions as Transaction class objects
    """
    transactions = []
    # Read form json file and store executed transactions
    for transaction in read_data():
        # Check if transaction has status "EXECUTED"
        if transaction["state"] == "EXECUTED":
            temp = Transaction(
                date_ = transaction["date"],
                description = transaction["description"],
                destination = transaction["to"],
                amount = transaction["operationAmount"]["amount"],
                currency = transaction["operationAmount"]["currency"]["name"],
            )
            # Check if there is source for transaction
            if "from" in transaction.keys():
                temp.set_source(transaction["from"])
            transactions.append(temp)
        # Check if list has 5 transactions already
        if len(transactions) == 5:
            break

    return transactions
############################################
# Testing
############################################
# print(read_data())
# for i in get_five():
#     print(i.show_details())
