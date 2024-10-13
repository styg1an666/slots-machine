from input.user_input import deposit, get_lines, get_bet
from game.game_functions import get_spin, print_slots, is_winner
from config.config import SYMBOL_COUNT, SYMBOL_MULTIPLIER, ROWS, REELS

def spin(balance):
    lines = get_lines()
    while True:
        bet_per_line = get_bet()
        bet_total = lines * bet_per_line
        if bet_total > balance:
            print(f"Insufficient balance. Available: ${balance}")
        else:
            break

    slots = get_spin(ROWS, REELS, SYMBOL_COUNT)
    print(f'Total bet: {bet_total}. Good luck!')
    print_slots(slots)
    winnings, winning_lines = is_winner(slots, lines, bet_per_line, SYMBOL_MULTIPLIER)
    if winnings > 0:
        print(f"You won ${winnings} on lines ", *winning_lines)
    else:
        print(f"You won ${winnings}. Better luck next time!")
    return winnings - bet_total

def main():
    balance = deposit()
    while True:
        print(f"Current balance: ${balance}")
        if input("Press Enter to play or 'q' to quit: ") == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}. Goodbye!")

if __name__ == "__main__":
    main()
