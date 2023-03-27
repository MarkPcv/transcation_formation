from datetime import date


def hide_information(init_data):
    """
    Hides the information of transaction details
    """
    # Divide the source information
    data = init_data.split(' ')
    # Check if it is card or account number:
    if data[0] in "Счет":
        # Format account number
        data[1] = f"**{data[1][-4:]}"
    else:
        # Format card number
        data[1] = f"{data[1][0:4]} {data[1][4:6]}** **** {data[1][12:]}"

    return ' '.join(data)


class Transaction:
    """Transaction of a user"""
    def __init__(self, date_: str, description: str, source: str,
                 destination: str, amount: str, currency: str):
        """Class initialization"""
        self.date = date_
        self.description = description
        self.__source = source
        self.__destination = destination
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        """Represents class contents"""
        return(
            f"Дата транзакции: {self.date}\n"
            f"Описание транзакции: {self.description}\n"
            f"От: {self.get_source()}\n"
            f"Куда: {self.get_destination()}\n"
            f"Сумма: {self.amount}\n"
            f"Валюта: {self.currency}\n"
        )

    def get_source(self):
        """
        Returns hidden source of transaction
        """
        return hide_information(self.__source)

    def get_destination(self):
        """
        Returns hidden destination of transaction
        """
        return hide_information(self.__destination)

    def get_date(self):
        """
        Returns date in format dd.mm.yyyy
        """
        # Extract date from the string
        date_ = date.fromisoformat(self.date[0:10])
        return date_.strftime("%d.%m.%Y")

    def show_details(self):
        """
        Displays transaction details
        """
        return(
            f"{self.get_date()} {self.description}\n"
            f"{self.get_source()} -> {self.get_destination()}\n"
            f"{self.amount} {self.currency}\n"
        )


############################################
# Testing
############################################
trans = Transaction("2019-08-26T10:50:58.294041",
                    "Перевод организации",
                    "Maestro 1596837868705199",
                    "Счет 64686473678894779589",
                    "31957.58",
                    "руб.")

#print(trans.get_source())
#print(trans.get_destination())
#print(trans)
#print(trans.get_date())
#print(trans.show_details())