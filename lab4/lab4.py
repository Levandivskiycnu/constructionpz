import re
import sys

LOG_PATTERN = re.compile(r'"([^"]*)" (\d{3}) (\d+)(?:\s|$)')


def calculate_traffic(file_path):
    sent_bytes = 0
    received_request_bytes = 0

    with open(file_path, "r", encoding="utf-8") as file:
        # Файл читається поступово, рядок за рядком.
        # Генератор не зберігає всі рядки в пам'яті.
        lines = (line for line in file)

        for line in lines:
            match = LOG_PATTERN.search(line)

            if match:
                request = match.group(1)
                response_bytes = int(match.group(3))

                sent_bytes += response_bytes
                received_request_bytes += len(request.encode("utf-8"))

    return sent_bytes, received_request_bytes


def main():
    file_path = sys.argv[1] if len(sys.argv) > 1 else "nginx.log"

    try:
        sent, received = calculate_traffic(file_path)
        print(f"Надіслано сервером: {sent:,} байт")
        print(f"Отримано (рядки запитів): {received:,} байт")
        print("Примітка: лог не містить розміру всіх вхідних HTTP-заголовків і тіл запитів.")
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")


if __name__ == "__main__":
    main()
