def result(a, c, b):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b


def one_digit(v):
    return v.is_integer() and -10 < v < 10


def lazy(a, c, b):
    msg = ""
    if one_digit(a) is True and one_digit(b) is True:
        msg += msg_[6]
    if a == 1 or b == 1 and c == "*":
        msg += msg_[7]
    if a == 0 or b == 0 and c in ["+", "-", "*"]:
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


msg_ = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy",
        " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0
msg_index = 0

while True:
    x, oper, y = input(msg_[0]).split()
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue
    else:
        operators = ["+", "-", "*", "/"]
        if oper not in operators:
            print(msg_[2])
        else:
            try:
                lazy(x, oper, y)
                print(result(x, oper, y))
            except ZeroDivisionError:
                print(msg_[3])
                continue
            else:
                while True:
                    answer_1 = input(msg_[4])
                    if answer_1 == "y":
                        if one_digit(result(x, oper, y)) is False:
                            memory = result(x, oper, y)
                        else:
                            msg_index = 10
                            while msg_index <= 12:
                                answer_3 = input(msg_[msg_index])
                                if answer_3 == "y":
                                    msg_index += 1
                                else:
                                    break
                            if msg_index > 12:
                                memory = result(x, oper, y)
                                break
                        break
                    elif answer_1 == "n":
                        break
                    else:
                        continue
        while True:
            answer_2 = input(msg_[5])
            if answer_2 not in ["n", "y"]:
                continue
            else:
                break
        if answer_2 == "y":
            continue
        elif answer_2 == "n":
            break
