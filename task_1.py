# Author = Jameel Aledrees
# Group = P3132
# Date = 05.10.2025

import re

# Регулярное выражение для корректного времени (HH:MM или HH:MM:SS)
time_pattern = re.compile(
    r'\b('
    r'(?:[01]\d|2[0-3])'
    r':'
    r'(?:[0-5]\d)'
    r'(?:'
    r':'
    r'(?:[0-5]\d)'
    r')?'
    r')\b'
)

def replace_time(text: str) -> str:
    return time_pattern.sub("(TBD)", text)

if __name__ == "__main__":
    print("Введите текст:")
    user_input = input()
    result = replace_time(user_input)
    print("Результат:")
    print(result)
