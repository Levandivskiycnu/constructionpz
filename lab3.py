
import doctest


def reverse_words(text):
    """
    >>> reverse_words("abcd")
    'dcba'
    >>> reverse_words("abcd efgh")
    'dcba hgfe'
    >>> reverse_words("")
    ''
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'
    >>> reverse_words(123)
    Traceback (most recent call last):
    ...
    TypeError: Аргумент має бути рядком.
    """
    if not isinstance(text, str):
        raise TypeError("Аргумент має бути рядком.")

    if not text.isascii():
        raise ValueError("Дозволені тільки ASCII символи.")

    chars = list(text)
    start = 0

    while start < len(chars):
        if chars[start].isspace():
            start += 1
            continue

        end = start
        while end < len(chars) and not chars[end].isspace():
            end += 1

        positions = []
        letters = []

        for i in range(start, end):
            if chars[i].isalpha():
                positions.append(i)
                letters.append(chars[i])

        letters.reverse()

        for i, letter in zip(positions, letters):
            chars[i] = letter

        start = end

    return "".join(chars)


if __name__ == "__main__":
    doctest.testmod(verbose=True)

    text = input("Enter text: ")

    try:
        print("Result:", reverse_words(text))
    except (TypeError, ValueError) as error:
        print("Error:", error)
