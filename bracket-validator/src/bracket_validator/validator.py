OPENING = "({<"
CLOSING = ")}>"

PAIRS = {
    ")": "(",
    "}": "{",
    ">": "<",
}


def validate_brackets(text):
    """Перевіряє баланс (), {}, <>.

    Повертає (чи_валідний, список_позицій_помилок).
    Позиції нумеруються з нуля.
    """
    stack = []
    errors = []

    for position, char in enumerate(text):
        if char in OPENING:
            stack.append((char, position))
        elif char in CLOSING:
            if not stack:
                errors.append(position)
            elif stack[-1][0] == PAIRS[char]:
                stack.pop()
            else:
                # Неправильна пара: позначаємо відкривальну і закривальну дужки.
                errors.append(position)
                errors.append(stack.pop()[1])

    # Дужки, що залишилися у стеку, не були закриті.
    for char, position in stack:
        errors.append(position)

    errors = sorted(set(errors))
    return len(errors) == 0, errors


def format_result(text):
    """Формує результат перевірки з візуальним позначенням помилок."""
    is_valid, errors = validate_brackets(text)

    if is_valid:
        return "Рядок валідний"

    marker = [" "] * len(text)
    for position in errors:
        marker[position] = "^"

    positions = ", ".join(str(position) for position in errors)
    return (
        f"{text}\n"
        f"{''.join(marker)}\n"
        f"Дужки незбалансовані на позиціях: {positions}"
    )
