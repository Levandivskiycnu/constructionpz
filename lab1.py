def main():
    fahrenheit = int(input("Введіть температуру за Фаренгейтом: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"Температура за Цельсієм: {round(celsius, 1)}")


if __name__ == "__main__":
    main()