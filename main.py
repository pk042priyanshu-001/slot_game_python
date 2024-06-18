import random

# Constants for the game
MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Symbols and their respective counts in the slot machine
symbols = {
    "Apple": 2,
    "Banana": 4,
    "Oranges": 6,
    "Mangoes": 8
}

def deposit():
    # Function to get the deposit amount from the player
    while True:
        amount = input("Enter some money: $")
        # Check if the amount is a digit
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero.")
        else:
            print("Please enter a valid number. (e.g.:$100)")
    return amount

def get_number_of_lines():
    # Function to get the number of lines the player wants to bet on
    while True:
        lines = input(f'Enter the number of lines to bet on between 1 to {MAX_LINE}: ')
        # Check if the lines input is a digit
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print(f'Enter an integer between 1 to {MAX_LINE}')
        else:
            print('Enter a number.')
    return lines

def get_bet():
    # Function to get the bet amount from the player
    while True:
        amount = input("What amount would you like to bet?: $")
        # Check if the amount is a digit
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Max. bet is ${MAX_BET} and Min. bet is ${MIN_BET}.")
        else:
            print(f"Please enter a number between ${MIN_BET} to ${MAX_BET}")

def spin_slot_machine(rows, cols, symbols):
    # Function to spin the slot machine and generate the outcome
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    
    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            column.append(symbol)
        columns.append(column)

    return columns

def print_outcome(columns):
    # Function to print the outcome of the slot machine spin
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")

def check_winning(columns, lines, bet, values):
    # Function to check for winning lines and calculate winnings
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line)
    return winnings, winning_lines

def game(balance):
    # Function to handle a single round of the game
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f'You only have ${balance}. A bet of ${total_bet} is not possible. Gareeb!!😅')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. And your total bet is ${total_bet}')
    
    slot = spin_slot_machine(ROWS, COLS, symbols)

    print_outcome(slot)

    winnings, winning_lines = check_winning(slot, lines, bet, symbols)

    print(f'You have won ${winnings}!!! 😮😮😮')
    print(f'You won on lines: {winning_lines}')

    return winnings - total_bet

def main():
    # Main function to start the game
    balance = deposit()

    while True:
        print(f'You have ${balance} as your balance.')
        spin = input('Press enter to continue the game and (q to quit the game): ')
        if spin == 'q':
            break

        balance += game(balance)

        if balance == 0:
            print('Chal phut yaha se gareeb!! 🤭🤭')
            break

    print(f'You have won ${balance}')

main()
