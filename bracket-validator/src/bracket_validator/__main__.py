from .validator import format_result


def main():
    text = input("Введіть рядок: ")
    print(format_result(text))


if __name__ == "__main__":
    main()
