def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.
    cash = 0
    for (key, value) in coins.items():
        
        if key == "pennies":
            cash = cash + value*.01
        elif key == "nickels":
            cash = cash + value*.05
        elif key == "dimes":
            cash = cash + value*.1
        elif key == "quarters":
            cash = cash + value*.25
    print(f"You have ${cash} in coins.")

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)

