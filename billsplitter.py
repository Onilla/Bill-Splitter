import random
print("Enter the number of friends joining (including you):")
count = int(input())
guests = {}
if count < 1:
    print("No one is joining for the party")
else:
    print()
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(count):
        name = input()
        guests[name] = 0
    print()
    print("Enter the total bill value:")
    bill = int(input())
    print()
    bill_for_one = round((bill / count), 2)
    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    answer = input()
    if answer == "Yes":
        bill_for_one = round((bill / (count - 1)), 2)
        lucky = random.choice(list(guests.keys()))
        print()
        print(lucky + " is the lucky one!")
        print()
        for j in guests:
            guests[j] = bill_for_one
        guests[lucky] = 0
        print(guests)
    else:
        bill_for_one = round((bill / count), 2)
        for j in guests:
            guests[j] = bill_for_one
        print("No one is going to be lucky")
        print()
        print(guests)
