# Slot Machine Game

## Overview

This is a simple Slot Machine game implemented using Python and Tkinter for the graphical user interface (GUI). The game allows players to deposit money, place bets on multiple lines, and spin the slot machine to potentially win money based on matching symbols.

## Features

- Deposit money into the game
- Place bets on up to 3 lines
- Spin the slot machine and see the outcome
- Win money based on matching symbols
- Graphical user interface for easy interaction

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Ensure you have Python 3 installed on your system.
2. Tkinter is included with Python, so no additional installation is needed for it.

## Usage

1. Clone the repository or download the `slot_machine.py` script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the `slot_machine.py` file.
4. Run the script using the following command:
   ```sh
   python slot_machine.py
5. The Slot Machine game window will appear.

**How to Play**
## 1. Deposit Money:

* When the game starts, you will be prompted to enter an initial amount of money to deposit into the game.
* You can also click the "Deposit" button to add more money at any time.

## 2. Place Bets:

* Enter the number of lines (1 to 3) you want to bet on in the "Number of lines" entry field.
* Enter the amount you want to bet per line in the "Bet amount" entry field.

## 3. Spin the Slot Machine:

* Click the "Spin" button to play the game.
* The slot machine will spin and display the outcome.
* If you win, the winnings will be added to your balance.
## 4. Game Over:

* If your balance reaches zero, the game will end, and you will be notified.


**Code Structure**
1. SlotMachineApp: The main class that initializes the GUI and handles all game logic.
2. deposit: Method to prompt the user for a deposit amount.
3. prompt: Helper method to show a prompt dialog.
4. update_balance: Method to update the displayed balance.
5. get_number_of_lines: Method to get the number of lines the player wants to bet on.
6. get_bet: Method to get the bet amount from the player.
7. play_game: Method to handle a single round of the game.
8. spin_slot_machine: Method to simulate the slot machine spin.
9. print_outcome: Method to display the outcome of the slot machine spin.
10. check_winning: Method to check for winning lines and calculate winnings.
