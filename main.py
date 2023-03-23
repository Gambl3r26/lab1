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

def z24():
    print ('какие цвета смешать?')
    i = str(input())
    v = str(input())
    if i == ('red') or i == ('blue') or i == ('yellow') and v == ('red') or v == ('blue') or v == ('yellow'):
        if i == ('red') or v == ('red') and i == ('blue') or v == ('blue'):
            w = ('violet')
            print(w)
        elif i == ('red') or v == ('red') and i == ('yellow') or v == ('yellow'):
            s = ('orange')
            print(s)
        elif i == ('blue') or v == ('blue') and i == ('yellow') or v == ('yellow'):
            t = ('green')
            print(t)
        else:
            print(i)
    else:
        print('ошибка')

def z242():
    str = input("enter first color: ")
    str += input("enter second color:")
    if "red" in str and "blue" in str:
        print("violet")
    elif "red" in str and "yellow" in str:
        print("orange")
    elif "blue" in str and "yellow" in str:
        print("green")
    else:
        print("error")
z242()
