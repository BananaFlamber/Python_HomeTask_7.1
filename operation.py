

def operation(expression):
    """Вычисляет математическое выражение."""
    # Компиляция выражения в байт-код
    code = compile(expression, "<string>", "eval")

    # Валидация доступных имен
    for name in code.co_names:
        if name not in ALLOWED_NAMES:
            raise NameError(f"The use of '{name}' is not allowed")

    return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)