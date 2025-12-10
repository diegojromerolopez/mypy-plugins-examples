from mypy_pure import pure


@pure
def impure_io() -> None:
    print("Hello world")

@pure
def impure_file_io() -> None:
    with open("test.txt", "w") as f:
        f.write("test")

def __impure_helper() -> None:
    print("Side effect")

@pure
def calls_impure() -> None:
    __impure_helper()
