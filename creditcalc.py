import math
import argparse

parser = argparse.ArgumentParser(description="This program will calculate the parameters of your loan")
parser.add_argument("--type", choices=["annuity", "diff"],
                    help="Select type: annuity or diff")
parser.add_argument("--interest",
                    help="Specify the interest rate as a positive number")
parser.add_argument("--principal", type=int,
                    help="Specify the principal as a positive integer number")
parser.add_argument("--periods", type=int,
                    help="Specify number of periods as a positive integer number")
parser.add_argument("--payment", type=int,
                    help="Specify the monthly payment as a positive integer number")
args = parser.parse_args()


def func_1(i_r, payment, principal):    # calculates number of annuity monthly payments
    periods = math.ceil(math.log(payment / (payment - i_r * principal), i_r + 1))
    years = periods // 12
    months = periods % 12
    if months == 1:
        if years == 0:
            print(f'It will take {months} month to repay the loan!')
        elif years == 1:
            print(f'It will take {years} year and {months} month to repay the loan!')
        else:
            print(f'It will take {years} years and {months} month to repay the loan!')
    elif months == 0:
        if years == 1:
            print(f'It will take {years} year to repay the loan!')
        else:
            print(f'It will take {years} years to repay the loan!')
    elif years == 0:
        print(f'It will take {months} months to repay the loan!')
    elif years == 1:
        print(f'It will take {years} year and {months} months to repay the loan!')
    else:
        print(f'It will take {years} years and {months} months to repay the loan!')
    sum_of_payments = payment * periods
    print(f"Overpayment={sum_of_payments - principal}")


def func_2(i_r, principal, periods):    # calculates annuity monthly payment amount
    payment = math.ceil(principal * ((i_r * math.pow(i_r + 1, periods)) / (math.pow(i_r + 1, periods) - 1)))
    print(f'Your monthly payment = {payment}!')
    sum_of_payments = payment * periods
    print(f"Overpayment={sum_of_payments - principal}")


def func_3(i_r, payment, periods):    # calculates annuity loan principal
    principal = math.floor(payment / ((i_r * math.pow(i_r + 1, periods)) / (math.pow(i_r + 1, periods) - 1)))
    print(f'Your loan principal = {principal}!')
    sum_of_payments = payment * periods
    print(f"Overpayment={sum_of_payments - principal}")


def func_4(i_r, principal, periods):    # calculates differentiated monthly payments amount
    sum_of_payments = 0
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + i_r * (principal - (principal * (m - 1) / periods)))
        print(f"Month {m}: payment is {payment}")
        sum_of_payments += payment
    print(f"\nOverpayment={sum_of_payments - principal}")


if args.interest is None:
    print("Incorrect parameters")
else:
    i = float(args.interest) / 100 / 12
    if args.type == "annuity" and i > 0:
        if args.principal and args.principal > 0 and args.payment and args.payment > 0:
            func_1(i, args.payment, args.principal)
        elif args.principal and args.principal > 0 and args.periods and args.periods > 0:
            func_2(i, args.principal, args.periods)
        elif args.payment and args.payment > 0 and args.periods and args.periods > 0:
            func_3(i, args.payment, args.periods)
        else:
            print("Incorrect parameters")
    elif args.type == "diff" and i > 0 and args.principal and args.principal > 0 and args.periods and args.periods > 0:
        func_4(i, args.principal, args.periods)
    else:
        print("Incorrect parameters")
