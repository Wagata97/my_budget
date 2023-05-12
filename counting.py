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

    if user_choose == 1:
        x = int(input('your income: '))
        my_balance += x
    elif user_choose == 2:
        x = int(input('your expense: '))
        my_balance -= x
    elif user_choose == 3:
        print('your balance: {}'.format(my_balance))
    else:
        print('incorrect data. Try again')


if __name__ == "__main__":
    main()

