def run(*kids):
    # Loop through all the kids and print that the child performed the activity.
    for kid in kids:
        print(f"{kid} ran like a fool!")
run("Joe", "Jenna")
# Output: 
# "Joe ran like a fool!"
# "Jenna ran like a fool!"

def swing(*kids):
    for kid in kids:
        print(f"{kid} is swinging too high!")

swing("Marybeth", "Ariel", "Kevin", "Courtney")

def slide(*kids):
    for kid in kids:
        print(f"{kid} slid down the slide!")

slide("Mike", "Jack", "Jennifer", "Earl")

def hide_and_seek(*kids):
    for kid in kids:
        print(f"{kid} is playing hide and seek!")

hide_and_seek("Henry", "Heather", "Hayley", "Hugh")