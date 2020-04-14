dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

def calc_coins(cash):
    original_amount = cash
    piggyBank["quarters"] = int(cash//.25)
    if piggyBank["quarters"] != 0:
        cash = float('%.2f' % (cash%.25))
        # print(f"remaining after calculating quarters: {cash}")
    piggyBank["dimes"] = int(cash//.1)
    if piggyBank["dimes"] != 0:
        cash = float('%.2f' % (cash%.1))
        # print(f"remaining after calculating dimes: {cash}")
    piggyBank["nickels"] = int(cash//.05)
    if piggyBank["nickels"] != 0:
        cash = float('%.2f' % (cash%.05))
        # print(f"remaining after calculating nickels: {cash}")
    piggyBank["pennies"] = int(cash//.01)
    cash = float('%.2f' % (cash%.01))
    # print(f"remaining after calculating pennies: {'%.2f' % cash}")
    
    print(piggyBank)
    print()
    for (key, value) in piggyBank.items():
        print(f"I have {value} {key} in my piggy bank.")
    print()
    print(f"All together that's ${original_amount}!")
calc_coins(dollarAmount)
