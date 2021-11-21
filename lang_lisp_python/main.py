from dataclasses import dataclass

@dataclass
class Env:
    pass


def default_env():
    data = {}
    return Env(data, None)


def read_expr() -> str:
    return input()


def main():
    print("main")
    env = default_env();
    while True:
         print("lisp > ", end="")
         expr = read_expr()
         print(expr)


if __name__ == "__main__":
    main()
