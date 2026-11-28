
import re
from dateutil.parser import parse


def extract_datetime(text):
    pattern = r"^On\s+(.*?)\s*,?\s*Test User"

    match = re.search(pattern, text)

    if not match:
        return None

    date_string = match.group(1).strip().rstrip(",")

    try:
        date = parse(date_string, fuzzy=True)
        return date.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return None

if __name__ == "__main__":
    text = "On Sun, 13 Oct 2024 19:01:18 +0800, Test User <test@test.me> wrote:"
    print(extract_datetime(text))