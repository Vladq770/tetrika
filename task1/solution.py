def strict(func):
    def wrapper(*args, **kwargs):
        # Получение аннотаций типов аргументов
        annotations = func.__annotations__
        # Объединение позиционных и именованных аргументов
        all_args = list(args) + list(kwargs)

        # Проверка соответсвия типов
        for i, (name, expected_type) in enumerate(annotations.items()):
            if i < len(all_args): # Если есть аргументы
                if not isinstance(all_args[i], expected_type):
                    raise TypeError(f"Argument {name} must be {expected_type}, got {type(all_args[i])}.")
                
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# test
print(sum_two(1, 2))
print(sum_two(1, 2.4))