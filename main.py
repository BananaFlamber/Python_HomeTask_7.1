from operation import operation as oper


def main():
    """Читает и рассчитывает введенное выражение"""
    print(WELCOME)
    while True:
        # Читаем пользовательский ввод
        try:
            expression = input(f"{PS1} ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Поддержка специальных команд
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # Вычисление выражения и обработка ошибок
        try:
            result = evaluate(expression)
        except SyntaxError:
            # Некорректное выражение
            print("Вы ввели некорректное выражение.")
            continue
        except (NameError, ValueError) as err:
            # Если пользователь попытался использовать неразрешенное имя
            # или неверное значение в переданной функции
            print(err)
            continue

        # Выводим результат, если не было ошибок
        print(f"Результат: {result}")