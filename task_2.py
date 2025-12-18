# Author = Jameel Aledrees
# Group = P3132
# Date = 05.10.2025

import re

MY_GROUP = "P3132"

pattern = re.compile(
    r'^'
    r'([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)'
    r'\s+'
    r'([А-ЯЁ])\.([А-ЯЁ])\.'
    r'\s+'
    r'(P\d{4,5})'
    r'$'
)

def filter_students(text: str) -> str:
    result = []
    lines = text.strip().split("\n")

    for line in lines:
        line = line.strip()
        m = pattern.match(line)

        if not m:
            result.append(line)
            continue

        surname, i1, i2, group = m.groups()

        if group != MY_GROUP:
            result.append(line)
            continue

        if i1 == i2:
            continue  # удалить студента

        result.append(line)

    return "\n".join(result)

if __name__ == "__main__":
    print("Введите список студентов (несколько строк). Завершите ввод пустой строкой:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    output = filter_students(text)

    print("Результат:")
    print(output)
