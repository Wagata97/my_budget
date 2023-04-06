print("""
Hello in App My Budget.
Please choose option which you are interested:
 1 - payment 
 2 - paycheck
 3 - balance
  """)

my_balance = 0
choose = input('> ')

while True:
    if not choose.isdecimal():
        print('Incorrect data. Please, try again.')
    pass
