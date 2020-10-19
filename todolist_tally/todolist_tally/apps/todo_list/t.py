def func(start_money, month):
    money = start_money
    for m in range(month):
        money = money * 1.01 + start_money
    return money


print(func(1000, 360))
