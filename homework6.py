# №1
x = 38
print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')

#примеры
a, b = 10, 5
if a > b: print('a > b')
if a > b and a > 0: print('ycnеx')
if (a > b) and (a > 0 or b < 1000): print('yспеx')
if 5 < b and b < 10: print('yспеx')

#можно сравнивать - числа, строки, списки...
if '34' > '123':
    print('усnех')
if '123' > '12':
    print('успех')
if [1, 2] > [1, 1]:
    print('успех')

#что нельзя сравнивать
#разные типы
if '6' > 5:
    print('успех')
if [5, 6] > 5:
    print('ycnех')
#но
if '6' != 5:
    print('успех')