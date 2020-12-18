import random as rn
import datetime as dt

signs = ['+', '-']
err = 0
count = 2
start = dt.datetime.now()

for i in range(1, count+1):
    rn.seed()
    sign = rn.choice(signs)
    if sign == signs[0]:
        a = rn.randint(10, 80)
        b = rn.randint(10, 100 - a)
        c = a + b
    else:
        a = rn.randint(30, 100)
        b = rn.randint(10, a)
        c = a - b
    print()
    print(str(i)+'('+str(count)+').', a, sign, b, '= ?')
    while True:
        c_ = None
        try:
            c_ = int(input("Ответ: "))
        except:
            print("Ошибка, введено не целое число")
        if c != c_:
            print('Неправильно, попробуй еще раз')
            err = err + 1
        else:
            print('Молодец, правильно!')
            break
print('Примеры закончились')
print('Количество неправильных ответов', err)
print('потрачено времени', dt.datetime.now() - start)
