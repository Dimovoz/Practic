a = int(input('Введите длину стороны А: '))
b = int(input('Введите длину стороны В: '))
c = int(input('Введите Длину стороны С: '))

if a == b == c:
    print('Равносторонний')
elif (a != b and b != c) or ( a == b and b != c) or (b == c and c != a):
    print('Равнобедренный')
elif a != b != c:
    print('Разносторонний')
