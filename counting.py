choose = {1: 'PAYMENT', 2: 'PAYCHECK', 3: 'BALANCE'}


def main():
    global user_choose
    print("""
        Hello in App My Budget.
        Please choose option which you are interested:
        1 - payment 
        2 - paycheck
        3 - balance""")

    my_balance = 0

    while True:
        choose = input('> ')
        if not choose.isdecimal():
            print('Please, enter a number')
        else:
            user_choose = int(choose)
            break

    if choose == 1:
        income()
    elif choose == 2:
        expense()
    elif choose == 3:
        balance()
    else:
        print('incorrect data. Try again')

def income():
    pass

def expense():
    pass

def balance():
    pass


if __name__ == "__main__":
    main()

