from utils.data import get_five


# Start program
def main():
    # Get five executed transactions from JSON file
    transactions = get_five()
    # Display last five executed transactions
    for transaction in transactions:
        print(transaction.show_details())


# Call the main function
if __name__ == '__main__':
    main()