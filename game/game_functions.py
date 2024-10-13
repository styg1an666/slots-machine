import random

def is_winner(columns, lines, bet, multiplier):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if symbol != column[line]:
                break
        else:
            winnings += multiplier[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]
        column = [random.choice(current_symbols) for _ in range(rows)]
        for symbol in column:
            current_symbols.remove(symbol)
        columns.append(column)

    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        print(" | ".join([column[row] for column in columns]))
