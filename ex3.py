# try:
#     number = int(input('Introdu un numar: '))
#     print(10 / number)
# except ValueError:
#     print('Nu ai introdus un numar valid')
# except ZeroDivisionError:
#     print('Nu poti imparti la zero')

numbers = [1, 2, 3]

try:
    print(numbers[2])
except IndexError:
    print('index in afara limetelor listei')
finally:
    print('Program terminat')