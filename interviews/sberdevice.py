# Пт 01 апр 2021
# Мой телеграм на всякий случай - @Nilov Александр Нилов

# Задача 1. Найти два максимальных значения в массиве

# Задача 2. Правильно сбалансированные скобочные последовательности
"""
    Правильно сбалансированные скобочные последовательности
        Дано:
            - Строка
                - Состоит из различных типов скобок {}[]()
                - Символы в произвольном порядке

        Результат:
            - Узнать, является ли скобочная последовательность сбалансированной

        Примеры входных двнных:
            - Сбалансированые
                - "{{([][])}()}"
                - "[[{{(())}}]]"
                - "[][][](){}"
            - Не сбалансированые
                - "([)]"
                - "((()]))[{()]"
                - "}{"
"""
def is_balaning(strs: str) -> bool:
    """
    {{
    }}}}

    {}  }}
    ]
    """
    if not strs:
        return True

    stack = []

    for ch in strs:

        if ch in "{[(":
            stack.append(ch)
        elif not stack:
            return False


        if stack[-1] == '{' and ch == '}':
            stack.pop()
        elif stack[-1] == '(' and ch == ')':
            stack.pop()
        elif stack[-1] == '[' and ch == ']':
            stack.pop()
        else:
            raise Exception("не ожидаемый символ")

    if not stack:
        return True

    return False



assert is_balancing("") == True
assert is_balancing("([)]") == False
assert is_balancing("{}}}") == False

# Случайно в чатике увидел и скачал

# Есть матрица NxN, состоящая из 0 и 1,
# и отражающая расположения кораблей на поле для морского боя.

# Поле может быть любого размера, но обязательно квадратное.
# Кораблей может быть любое количество
# Размер кораблей — от 1х1 до 1хN
# Корабли никак не соприкасаются друг с другом.
# Могут располагаться горизонтально и вертикально
# Необходимо подсчитать количество кораблей.
# Матрицу можно менять

# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0

#1

# 0 1 0 0
# 0 0 0 0
# 1 1 0 0
# 0 0 0 0

#2

# [] -> 0

def find_ship(matrix: list[list[int]], x: int, y: int):
    if matrix[x][y] != 1:
        return None, None, None
    if x+1 < len(matrix) and matrix[x+1][y] == 1:
        direction = 0
    elif y+1 < len(matrix) and matrix[x][y+1] == 1:
        direction = 1
    else:
        return x, y, None
    if direction == 0:
        pointer = 2
        while x+pointer < len(matrix) and matrix[x+pointer][y] == 1:
            pointer += 1
        return x+pointer-1, y, direction
    else:
        pointer = 2
        while y+pointer < len(matrix) and matrix[x][y+pointer] == 1:
            pointer += 1
        return x, y+pointer-1, direction



def ship_count(matrix: list[list[int]]) -> int:
    count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if matrix[x][y] != 1:
                continue
            else:
                _x, _y, d = find_ship(matrix, x, y)
                # print(_x, _y, d)
                if _x is None:
                    continue
                count += 1
                matrix[x][y] = 0
                if d is None:
                    continue
                elif d == 0:
                    for pointer_x in range(x+1, _x+1):
                        matrix[pointer_x][y] = 0
                else:
                    for pointer_y in range(y+1, _y+1):
                        matrix[x][pointer_y] = 0
    return count

# дано два отсортированных массива
# требуется составить из них один отсортированный массив
# выполнить способом с наименьшей сложностью


def merge_sorted(a_list: list[int], b_list: list[int]) -> list[int]:
    merged_list: list[int] = list()
    if not a_list:
        return b_list
    if not b_list:
        return a_list
    a_pointer, b_pointer = 0, 0
    while a_pointer <= len(a_list) and b_pointer <= len(b_list):
        if a_pointer == len(a_list):
            return merged_list + b_list[b_pointer:]
        if b_pointer == len(b_list):
            return merged_list + a_list[a_pointer:]
        if a_list[a_pointer] <= b_list[b_pointer]:
            merged_list.append(a_list[a_pointer])
            a_pointer += 1
        else:
            merged_list.append(b_list[b_pointer])
            b_pointer += 1
    return merged_list

