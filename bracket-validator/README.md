# Bracket Validator

Простий валідатор для перевірки правильності закривання дужок `()`, `{}`, `<>`.

## Запуск

```bash
python -m bracket_validator
```

## Використання як пакета

```python
from bracket_validator import validate_brackets, format_result

print(validate_brackets("<div>(test)</div>"))
print(format_result("<div>{ test }}</div>"))
```

`validate_brackets()` повертає `(True/False, список позицій помилок)`. Позиції нумеруються з нуля.

## Тести

```bash
python -m unittest discover -s tests -v
```
