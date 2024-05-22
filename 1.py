a = int(input('Введите длину стороны А: '))
b = int(input('Введите длину стороны В: '))
c = int(input('Введите Длину стороны С: '))

if a == b == c:
    print('Равносторонний')
    
elif a != b and a != c and b != c:
    print('Разносторонний')

else:
    print('Равнобедренный')
