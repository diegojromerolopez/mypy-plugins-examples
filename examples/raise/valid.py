from mypy_raise import raising


@raising([ValueError, AssertionError, TypeError])
def assert_positive(a: int) -> None:
    if not isinstance(a, int):
        raise ValueError("a must be an integer")
    if a == 0:
        raise AssertionError('Value must be positive. It is zero')
    if a < 0:
        raise AssertionError('Value must be positive. It is negative')

