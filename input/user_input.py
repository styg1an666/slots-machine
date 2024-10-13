import time
from config.config import MAX_ATTEMPTS, MIN_AMOUNT, MAX_AMOUNT, MIN_LINES, MAX_LINES, MIN_BET, MAX_BET

def deposit():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            amount = float(input(f'How much would you like to deposit? \nMin. ${MIN_AMOUNT}  Max. ${MAX_AMOUNT} \n$ '))
            if MIN_AMOUNT <= amount <= MAX_AMOUNT:
                return amount
            else:
                print(f"Amount must be between ${MIN_AMOUNT} and ${MAX_AMOUNT}. Try again.")
        except ValueError:
            print("Invalid amount. Try again.")
        attempts += 1
    print("Too many invalid attempts. Please try again later.")
    time.sleep(60)
    return deposit()

def get_lines():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            lines = int(input(f'How many lines would you like to play? \nMin {MIN_LINES}  Max {MAX_LINES} \n'))
            if MIN_LINES <= lines <= MAX_LINES:
                return lines
            else:
                print(f'Number of lines must be between {MIN_LINES} and {MAX_LINES}.')
        except ValueError:
            print("Invalid number. Try again.")
        attempts += 1
    print("Too many invalid attempts. Please try again later.")
    time.sleep(60)
    return get_lines()

def get_bet():
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        try:
            bet = int(input(f'Bet amount per line? \nMin ${MIN_BET} Max ${MAX_BET} \n$ '))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f'Bet must be between ${MIN_BET} and ${MAX_BET}.')
        except ValueError:
            print("Invalid bet. Try again.")
        attempts += 1
    print("Too many invalid attempts. Please try again later.")
    time.sleep(60)
    return get_bet()
