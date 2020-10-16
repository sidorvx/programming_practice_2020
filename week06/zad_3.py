def menu():
    print('1) Круг')
    print('2) Прямоугольник')
    print('3) Треугольник')
    print('0) Завершение')


def circle():
    r = float(input('Нужен радиус:'))
    return 'Ответ: {}'.format(r**2*__import__('math').pi)


def rectangle():
    a, b = list(map(float, input('Стороны прямоугольника:').split()))
    return 'Ответ: {}'.format(a*b)


def triangle():
    print('1. По Герона')
    print('2. По высоте')
    ans = input()
    if ans == '1':
        a, b, c = list(map(float, input('Стороны треугольника:').split()))
        p = (a + b + c) / 2
        return 'Ответ: {}'.format((p*(p-a)*(p-b)*(p-c))**.5)
    elif ans == '2':
        a, h = list(map(float, input('Сторона и высота к ней:').split()))
        return 'Ответ: {}'.format(a*h/2)
    else:
        return 'Третьего не дано'


while True:
    menu()
    ans = input()

    if ans == '1':
        print(circle())
    elif ans == '2':
        print(rectangle())
    elif ans == '3':
        print(triangle())
    elif ans == '0':
        break
    else:
        print('Boy next door')