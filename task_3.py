# Author = Jameel Aledrees
# Group = P3132
# Date = 05.10.2025

import re

field = (
    r'(?:'
    r'\*'
    r'|\d+'
    r'|\d+-\d+'
    r'|\*/\d+'
    r'|\d+-\d+/\d+'
    r'|\d+(?:,\d+)+'
    r')'
)

cron_pattern = re.compile(
    r'^' + field + r'\s+' +
           field + r'\s+' +
           field + r'\s+' +
           field + r'\s+' +
           field + r'$'
)

def is_valid_cron(expr: str) -> bool:
    return bool(cron_pattern.match(expr.strip()))

if __name__ == "__main__":
    print("Введите cron-выражение:")
    expr = input().strip()
    if is_valid_cron(expr):
        print("Корректно")
    else:
        print("Некорректно")
