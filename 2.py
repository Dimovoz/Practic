a = int(input('Введите число А: '))
b = int(input('Введите число В: '))
c = int(input('Введите число С: '))

if a == b or b == c or a == c:
    print('!ERROR!',
          'same numbers')
elif a > b and a < c:
    print(a)
elif a < b and b < c or a > b and b > c:
    print(b)

elif a < b and b > c:
    print(c)


