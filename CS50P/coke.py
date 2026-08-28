inserted_value = 0
coke_price = 50
amount_due = coke_price
accepted_currencies = ['5','10','25']

while inserted_value < coke_price:
    print(f'Amount Due: {amount_due}')
    user_input = input('Insert Coin: ')
    for i,value in enumerate(accepted_currencies):
        if user_input != accepted_currencies[i]:
            continue
        else:
            user_input = int(user_input)
            inserted_value = inserted_value+user_input
            amount_due = coke_price-inserted_value
else:
    change_owed = inserted_value-coke_price
    print(f'Change Owed: {change_owed}')
