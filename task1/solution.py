from inspect import signature
from types import UnionType
from typing import Any, Callable


def strict(func: Callable) -> Callable:  # noqa
    """
    Декоратор для проверки соответствия типов переданных в вызов функции аргументов типам аргументов.

    Args:
        func: Метод, который нужно обернуть.

    Returns:
        Обёрнутый метод.
    """

    def wrapper(*args, **kwargs):
        sig = signature(func)
        bound_args = sig.bind(*args, **kwargs)

        for parameter_name, parameter_info in bound_args.signature.parameters.items():
            expected_types = parameter_info.annotation
            value = bound_args.arguments[parameter_name]
            is_any_type = (
                isinstance(expected_types, UnionType)
                and Any in expected_types.__args__
                or expected_types is Any
            )
            if is_any_type or isinstance(value, expected_types):
                continue
            raise TypeError(
                f"Argument '{parameter_name}' must be of type {expected_types}, not {type(value)}"
            )

        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def foo(a: int | float, b: Any) -> None:
    print(a, b)  # noqa


@strict
def foo_v2(a: int | float | Any, b: Any | str) -> None:
    print(a, b)  # noqa
