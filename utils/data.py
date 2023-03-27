import json

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

############################################
# Testing
############################################
#print(read_data())
