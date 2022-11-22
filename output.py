import operation

MENU_ITEMS = {
   "Q": "Выход",
   "+": "a + b",
   "-": "a - b",
   "*": "a * b",
   "/": "a / b",
   "S": " MS ",
   "R": " MR "
}


def print_memory():
    print(f"Число в памяти: {operation.memory}")


def menu():
    for index, item in MENU_ITEMS.items():
        print(f"{index} - {item}")
    print("Выберите пункт меню: ", end="")


def print_char(ch):
    print(f"Введите {ch}: ", end="")