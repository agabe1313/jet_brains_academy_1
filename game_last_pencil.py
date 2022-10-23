import random

names = ["Aga", "Piotrek"]
i = 0
global pencils
global turn
msg_numeric = "The number of pencils should be numeric"
msg_positive = "The number of pencils should be positive"
msg_choose = "Choose between Aga and Piotrek"
msg_values = "Possible values: '1', '2' or '3'"
msg_2many = "Too many pencils were taken"

while True:
    try:
        pencils = int(input("How many pencils would you like to use:"))
    except ValueError:
        print(msg_numeric)
        continue
    else:
        if pencils > 0:
            break
        elif pencils < 0:
            print(msg_numeric)
            continue
        else:
            print(msg_positive)
            continue

while True:
    name = input("Who will be the first (Aga, Piotrek):")
    if name == names[i]:
        i = i
        break
    elif name == names[i + 1]:
        i += 1
        break
    else:
        print(msg_choose)
        continue

while pencils > 0:
    print("|" * pencils)
    if i == 0:
        turn = input(f"{names[i]}'s turn:")
        try:
            turn = int(turn)
        except ValueError:
            print(msg_values)
            continue
        else:
            if turn not in {1, 2, 3}:
                print(msg_values)
                continue
            if turn > pencils:
                print(msg_2many)
                print(msg_values)
                continue
            else:
                i = 1
    else:
        print(f"{names[i]}'s turn:")
        x = pencils
        if pencils % 4 == 1:
            turn = random.randint(1, 3) if pencils >= 3 else random.randint(1, x)
        elif pencils % 4 == 0:
            turn = 3
        elif pencils % 4 == 2:
            turn = 1
        elif pencils % 4 == 3:
            turn = 2
        i = 0
        print(turn)
    pencils -= turn

if pencils == 0:
    print(f"{names[i]} won!")
