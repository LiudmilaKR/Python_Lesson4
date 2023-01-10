# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = int(input('Введите степень k многочлена: '))
# import random

# def polinomium(n):
#     my_list = []
#     for i in range(1, n + 2):
#         my_list.append(str(random.randrange(0, 100)))
        
#     polinom = ''
#     if my_list[n] == '0':
#         polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(n))
#     elif my_list[n] == '1':
#         polinom_new = polinom.join('x**' + str(n))
#     else:
#         polinom_new = polinom.join(my_list[n] + '*x**' + str(n))

#     for i in range(n - 1, 0, -1):
#         if my_list[i] == '0':
#             polinom_new = polinom_new + ''
#         elif my_list[i] == '1' and i != 1:
#             polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
#         elif i == 1 and my_list[i] != '1':
#             polinom_new = polinom_new + ' + ' + polinom.join(my_list[i] + '*x')
#         elif i == 1 and my_list[i] == '1':
#             polinom_new = polinom_new + ' + ' + polinom.join('x')
#         else:
#             polinom_new = polinom_new + ' + ' + polinom.join(my_list[i] + '*x**' + str(i))

#     if my_list[0] == '0':
#         polinom_new = polinom_new + ''
#     else:
#         polinom_new = polinom_new + ' + ' + polinom.join(my_list[0])
#     return polinom_new

# with open ('input.txt', 'w', encoding='utf-8') as file:
#     file.write(polinomium(k))

# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# k1 = int(input('Введите степень первого многочлена: '))
# k2 = int(input('Введите степень второго многочлена: '))
# import random

# def polinomium(n):
#     my_list = []
#     for i in range(1, n + 2):
#         my_list.append(str(random.randrange(0, 100)))
    
#     polinom = ''
#     if my_list[n] == '0':
#         polinom_new = polinom.join(str(random.randrange(2, 100)) + '*x**' + str(n))
#     elif my_list[n] == '1':
#         polinom_new = polinom.join('x**' + str(n))
#     else:
#         polinom_new = polinom.join(my_list[n] + '*x**' + str(n))

#     for i in range(n - 1, 0, -1):
#         if my_list[i] == '0':
#             polinom_new = polinom_new + ''
#         elif my_list[i] == '1' and i != 1:
#             polinom_new = polinom_new + ' + ' + polinom.join('x**' + str(i))
#         elif i == 1 and my_list[i] != '1':
#             polinom_new = polinom_new + ' + ' + polinom.join(my_list[i] + '*x')
#         elif i == 1 and my_list[i] == '1':
#             polinom_new = polinom_new + ' + ' + polinom.join('x')
#         else:
#             polinom_new = polinom_new + ' + ' + polinom.join(my_list[i] + '*x**' + str(i))

#     if my_list[0] == '0':
#         polinom_new = polinom_new + ''
#     else:
#         polinom_new = polinom_new + ' + ' + polinom.join(my_list[0])
#     return polinom_new

# polinom1 = polinomium(k1)
# polinom2 = polinomium(k2)

# with open ('input1.txt', 'w', encoding='utf-8') as file:
#     file.write(polinom1)
# with open ('input2.txt', 'w', encoding='utf-8') as file:
#     file.write(polinom2)

# polinom1 = polinom1.split(" + ")[::-1]
# polinom2 = polinom2.split(" + ")[::-1]

# my_dict1 = {}
# for item in polinom1:
#     if item == 'x':
#         my_dict1[item] = 1
#     elif item.find('*x**') >= 0:
#         my_dict1[item[-4:]] = item[:-5]
#     elif item.find('x**') >=0:
#         my_dict1[item[-4:]] = 1
#     elif item.find('*x') >=0:
#         my_dict1[item[-1:]] = item[:-2]
#     else:
#         my_dict1[0] = polinom1[0]

# my_dict2 = {}
# for item in polinom2:
#     if item == 'x':
#         my_dict2[item] = 1
#     elif item.find('*x**') >= 0:
#         my_dict2[item[-4:]] = item[:-5]
#     elif item.find('x**') >=0:
#         my_dict2[item[-4:]] = 1
#     elif item.find('*x') >=0:
#         my_dict2[item[-1:]] = item[:-2]
#     else:
#         my_dict2[0] = polinom2[0]

# my_dict = {}
# for i in my_dict1.keys():
#     for j in my_dict2.keys():
#         if i == j:
#             my_dict[i] = str(int(my_dict1[i]) + int(my_dict2[j]))

# my_dict = my_dict1 | my_dict
# my_dict = my_dict2 | my_dict

# my_text = ''
# for k, v in my_dict.items():
#     if k == 0:
#         my_text = my_text + v
#     elif v == 1:
#         my_text = my_text + ' + ' + str(k)
#     else:
#         my_text = my_text + ' + ' + v + '*' + str(k)
# if my_text.startswith(' + '):
#     my_text = my_text[3:]
# # print(my_text)
# with open ('input.txt', 'w', encoding='utf-8') as file:
#     file.write(my_text)