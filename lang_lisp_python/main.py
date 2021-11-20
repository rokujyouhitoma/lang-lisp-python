def read_expr() -> str:
    return input()


def main():
    print("main")
    while True:
         print("lisp > ", end="")
         expr = read_expr()
         print(expr)


if __name__ == "__main__":
    main()
