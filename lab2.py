from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CENT = Decimal("0.01")
DEFAULT_YEARS = 2


def money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def read_decimal(prompt, minimum=None, maximum=None, allow_zero=False):
    while True:
        raw = input(prompt).strip().replace(",", ".")

        try:
            value = Decimal(raw)
        except InvalidOperation:
            print("Помилка: введіть коректне число.")
            continue

        if not value.is_finite():
            print("Помилка: введіть скінченне число.")
            continue

        if minimum is not None and value < minimum:
            print(f"Помилка: значення має бути не менше {minimum}.")
            continue

        if maximum is not None and value > maximum:
            print(f"Помилка: значення має бути не більше {maximum}.")
            continue

        if not allow_zero and value == 0:
            print("Помилка: значення має бути більшим за нуль.")
            continue

        return value


def read_years():
    while True:
        raw = input(f"Термін депозиту в роках (Enter — {DEFAULT_YEARS}): ").strip()

        if raw == "":
            return DEFAULT_YEARS

        try:
            years = int(raw)
        except ValueError:
            print("Помилка: термін має бути цілим числом років.")
            continue

        if years <= 0:
            print("Помилка: термін має бути більшим за нуль.")
            continue

        if years > 100:
            print("Помилка: термін не може перевищувати 100 років.")
            continue

        return years


def main():
    print("=== ДЕПОЗИТНИЙ КАЛЬКУЛЯТОР ===")

    principal = read_decimal(
        "Початкова сума депозиту: ",
        minimum=Decimal("0.01")
    )

    annual_rate = read_decimal(
        "Річна процентна ставка (%): ",
        minimum=Decimal("0"),
        maximum=Decimal("1000"),
        allow_zero=True
    )

    years = read_years()
    months = years * 12
    monthly_rate = annual_rate / Decimal("1200")

    balance = money(principal)

    print("\nМісяць | На початок, грн | Відсотки, грн | На кінець, грн")
    print("-" * 66)

    for month in range(1, months + 1):
        interest = money(balance * monthly_rate)
        opening_balance = balance
        balance = money(balance + interest)

        print(
            f"{month:6} | "
            f"{opening_balance:15.2f} | "
            f"{interest:13.2f} | "
            f"{balance:14.2f}"
        )

    total_interest = money(balance - money(principal))

    print("\n=== ПІДСУМОК ===")
    print(f"Початковий депозит: {money(principal):.2f} грн")
    print(f"Річна ставка: {annual_rate:.2f}%")
    print(f"Термін: {years} років ({months} місяців)")
    print(f"Загальний дохід: {total_interest:.2f} грн")
    print(f"Сума наприкінці терміну: {balance:.2f} грн")


if __name__ == "__main__":
    main()
