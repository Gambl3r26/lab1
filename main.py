def z21():
    i = 0
    print('Введите пароль')
    pw1 = input()
    print('Повторно введите пароль')
    pw2 = input()
    if pw1 == pw2:
        print('пароль принят')
    else:
        print('пароль не принят')

def z22():
    print('номер места')
    i = int(input())
    if i <= 36:
        print('купе')
    else:
        print('боковое')
    if i % 2 == 0 :
        print('верхнее')
    else:
        print('нижнее')

def z23():
    i=int(input())
    if i % 4 == 0 and i % 100 == 0:
        print(i, 'високосный')
    elif i % 400 == 0:
        print(i, 'високосный')
    else:
        print(i, 'не високосный')
z23()


