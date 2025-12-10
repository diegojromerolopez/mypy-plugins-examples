from mypy_pure import pure


@pure
def add(a: int, b: int) -> int:
    return a + b

@pure
def multiply(a: int, b: int) -> int:
    return a * b

@pure
def pure_string_concat(s1: str, s2: str) -> str:
    return s1 + s2

@pure
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
