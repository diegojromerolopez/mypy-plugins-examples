from mypy_raise import raising


@raising([ValueError])
def not_raising() -> None:
    print("Hello world")


@raising([])
def raising_exception() -> None:
    raise ValueError("An exception")
