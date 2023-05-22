choose = {1: 'PAYMENT', 2: 'PAYCHECK', 3: 'BALANCE'}


def main():
    while True:
        print("""
    Hello in App My Budget.
    Please choose option which you are interested:
      1 - payment 
      2 - paycheck
      3 - balance
    """)
        user_choose = int(input('My choose > '))
        if user_choose == 1:
            income()
        elif user_choose == 2:
            expense()
        elif user_choose == 3:
            balance()
        else:
            print('incorrect data. Try again')
            continue


my_balance = 0


def income():
    global my_balance
    payment = int(input('Your income: '))
    my_balance += payment
    print('My balance: ', my_balance)


def expense():
    global my_balance
    paycheck = int(input('Your expense: '))
    my_balance += paycheck
    print('My balance: ', my_balance)


def balance():
    print('My balance: ', my_balance)


if __name__ == "__main__":
    main()

