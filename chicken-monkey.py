def chicken_monkey(start, stop):
    for i in range(start, stop):
        if i%5 == 0 and i%7 == 0:
            print("ChickenMonkey") 
        elif i%5 == 0:
            print("Chicken")
        elif i%7 == 0:
            print("Monkey")
        else:
            print(i)

chicken_monkey(1, 101)