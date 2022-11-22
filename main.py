import operation
from input import menu_input, check_menu_item, input_value, input_op
from output import menu, print_char, print_memory

"""


Сценарий взаимодействия с программой
1. Отобразить меню с операциями (с целыми числами)
2. Пользователь вводит пункт меню
3. Обратотка выбора пользователя
   3.1 Если пользователь правильно выбрал пункт меню (1 - 4)
       то предлагаем ввести числа (обработка чисел)
       Иначе вывести ошибку и попросить выбрать п. меню по новой
       
Обработка чисел
1. Если пользователь ввел числа
   то выполнить операцию (+, - ...)
   Иначе вывести ошибку и вернуться в меню  TODO

Програмные сущности:
Меню, Калькулятор, Вывод, Проверка данных, (Логгер, Файл менеджер ....)

View
- Вывод меню
- Результат расчетов (операций)
- Подскаски

Model
- Калькулятор

Controller
- обработка запросов пользователя

"""



while True:
    print_memory()
    menu()
    menu_item = menu_input()
    if not check_menu_item(menu_item):
        print('Некорректные данные')
        continue
    elif menu_item=='Q': break

    print_char("a")
    a = input_value()
    print_char("b")
    b = input_value()

    operation.memory = operation.calculate(a, b, menu_item)
    print(f"Результат операции: {a} {menu_item} {b} = {operation.memory}")