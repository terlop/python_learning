from cgi import print_directory
from re import L
from this import d
from tkinter import E


dict1 = {1:'string', 2: 'word', 3: 'slovo'}
print(dict1[1])
dict1[4] = 'stroka' # присвание по несуществующему ключу создает новую пару
print(dict1[4])

# ключами словаря могут быть только неизменяемые типы


# Словари можно использовать для реализации разреженных структур данных (например многомерных массивов):
# Здесь мы используем словарь для представления трехмерного массива который пуст за исключением 2-х позиций: (2, 3, 4) и (7, 8, 9)
# ключи здесь являются кортежами которые регистрируют координаты непустых яччеек
# по итогу вместе выделения памяти под крупную и почти пустую 3-х мерную матрицу мы применяем простой 2-х эл-тный массив
matrix = {}
matrix[(2, 3, 4)] = 88
matrix[(7, 8, 9)] = 99
x = 2; y = 3; z = 4 # ; oтделяет операторы
matrix[(x, y, z)]
print(matrix)
print(matrix[(x, y, z)]) # 88
# доступ к пустой ячейке тут вызовет исключение тк они физически не хранятся

# чтобы избежать вызова ошибки при обращении к пустой ячейке есть способы:
if (2, 3, 6) in matrix:
    print(matrix[(2, 3, 6)])
else:
    print(0)
# or
try:
    print(matrix[(2, 3, 6)])
except KeyError:
    print(0)

# способ изюежания ошибки через метод get() который позволяет избежать ошибки при отстутствии ключа
print(matrix.get((2, 3, 6), 0)) # 0
print(matrix.get((2, 3, 4), 0)) # 88

dict_gens1 = {}
dict_gens1['name'] = 'ayaka'
dict_gens1['element'] = 'kryo'
dict_gens1['region'] = 'inadzuma'
print(dict_gens1)
print(dict_gens1['element'])

# вложение в словарь
dict_gens2 = {'name': 'tartgalia', 'element': ['hydro', 'electro'], 'weapon': {'real weapon':'bow', 'hydro weapon':['sword', 'spear', 'bow']}}
print(dict_gens2)
print(dict_gens2['weapon']['hydro weapon']) # вывод данных из списка вложенного в словарь вложенного в словарь

# помещаем словарь в список
list1 = []
list1.append(dict_gens2)
print(list1[0]['weapon']['hydro weapon']) # вызов того же что мы вызывали выше только теперь весь словарь еще и в списке

#
