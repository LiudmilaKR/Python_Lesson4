# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = int(input('Введите степень k многочлена: '))
# list = []
# import random
# for i in range(1, k + 2):
#     a = random.randrange(0, 100)
#     b = str(a)
#     list.append(b)
# # print(list)

# polinom = ''
# if list[k] == '0':
#     polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(k))
# elif list[k] == '1':
#     polinom_new = polinom.join('x**' + str(k))
# else:
#     polinom_new = polinom.join(list[k] + '*x**' + str(k))

# for i in range(k - 1, 0, -1):
#     if list[i] == '0':
#         polinom_new = polinom_new + ''
#     elif list[i] == '1':
#         polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
#     elif i == 1:
#         polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x')
#     else:
#         polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x**' + str(i))
# if list[0] == '0':
#     polinom_new = polinom_new + ''
# else:
#     polinom_new = polinom_new + ' + ' + polinom.join(list[0])
# print(polinom_new)

# with open ('input.txt', 'w', encoding='utf-8') as file:
#     file.write(polinom_new)

# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

k1 = int(input('Введите степень первого многочлена: '))
k2 = int(input('Введите степень второго многочлена: '))

def Polinomium(k):
    list = []
    import random
    for i in range(1, k + 2):
        a = random.randrange(0, 100)
        b = str(a)
        list.append(b)

    polinom = ''
    if list[k] == '0':
        polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(k))
    elif list[k] == '1':
        polinom_new = polinom.join('x**' + str(k))
    else:
        polinom_new = polinom.join(list[k] + '*x**' + str(k))

    for i in range(k - 1, 0, -1):
        if list[i] == '0':
            polinom_new = polinom_new + ''
        elif list[i] == '1':
            polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
        elif i == 1:
            polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x')
        else:
            polinom_new = polinom_new + ' + ' + polinom.join(list[i] + '*x**' + str(i))
    if list[0] == '0':
        polinom_new = polinom_new + ''
    else:
        polinom_new = polinom_new + ' + ' + polinom.join(list[0])
    return polinom_new

polinom1 = Polinomium(k1)
polinom2 = Polinomium(k2)
print(polinom1)
print(polinom2)

polinom1 = polinom1.split(" + ")
polinom2 = polinom2.split(" + ")
print(polinom1)
print(polinom2)


# # with open ('input.txt', 'w', encoding='utf-8') as file:
# #     file.write(polinom_new)
