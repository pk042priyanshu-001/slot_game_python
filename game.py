import tkinter as tk
from tkinter import messagebox, simpledialog
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

class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")
        self.balance = 0

        # Create and place widgets
        self.balance_label = tk.Label(root, text="Balance: $0")
        self.balance_label.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.lines_label = tk.Label(root, text="Number of lines (1-3):")
        self.lines_label.pack()
        self.lines_entry = tk.Entry(root)
        self.lines_entry.pack()

        self.bet_label = tk.Label(root, text="Bet amount ($1-$100):")
        self.bet_label.pack()
        self.bet_entry = tk.Entry(root)
        self.bet_entry.pack()

        self.spin_button = tk.Button(root, text="Spin", command=self.play_game)
        self.spin_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        # Prompt for initial deposit when the application starts
        self.deposit()

    def deposit(self):
        # Function to get the deposit amount from the player
        amount = self.prompt("Enter some money: $")
        if amount is not None:
            self.balance += amount
            self.update_balance()

    def prompt(self, prompt_text):
        # Function to prompt the user for input
        while True:
            amount_str = simpledialog.askstring("Input", prompt_text)
            if amount_str is None:  # User cancelled
                return None
            if amount_str.isdigit():
                amount = int(amount_str)
                if amount > 0:
                    return amount
                else:
                    messagebox.showerror("Error", "Amount should be greater than zero.")
            else:
                messagebox.showerror("Error", "Please enter a valid number. (e.g.:$100)")

    def update_balance(self):
        # Function to update the balance display
        self.balance_label.config(text=f"Balance: ${self.balance}")

    def get_number_of_lines(self):
        # Function to get the number of lines the player wants to bet on
        lines_str = self.lines_entry.get()
        if lines_str.isdigit():
            lines = int(lines_str)
            if 1 <= lines <= MAX_LINE:
                return lines
        messagebox.showerror("Error", f"Enter an integer between 1 and {MAX_LINE}")
        return None

    def get_bet(self):
        # Function to get the bet amount from the player
        amount_str = self.bet_entry.get()
        if amount_str.isdigit():
            amount = int(amount_str)
            if MIN_BET <= amount <= MAX_BET:
                return amount
        messagebox.showerror("Error", f"Please enter a number between ${MIN_BET} and ${MAX_BET}")
        return None

    def play_game(self):
        # Function to handle a single round of the game
        lines = self.get_number_of_lines()
        if lines is None:
            return

        bet = self.get_bet()
        if bet is None:
            return

        total_bet = lines * bet
        if total_bet > self.balance:
            messagebox.showerror("Error", f'You only have ${self.balance}. A bet of ${total_bet} is not possible.')
            return

        self.balance -= total_bet
        self.update_balance()

        slot = self.spin_slot_machine(ROWS, COLS, symbols)
        self.print_outcome(slot)

        winnings, winning_lines = self.check_winning(slot, lines, bet, symbols)

        self.balance += winnings
        self.update_balance()

        messagebox.showinfo("Results", f'You have won ${winnings}!!!\nYou won on lines: {winning_lines}')

        if self.balance == 0:
            messagebox.showinfo("Game Over", "You have run out of money! Game over!")
            self.root.quit()

    def spin_slot_machine(self, rows, cols, symbols):
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

    def print_outcome(self, columns):
        # Function to print the outcome of the slot machine spin
        outcome_text = ""
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    outcome_text += column[row] + " | "
                else:
                    outcome_text += column[row] + "\n"
        self.result_label.config(text=outcome_text)

    def check_winning(self, columns, lines, bet, values):
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

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
