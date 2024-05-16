from typing import List

def task2(l: List[int]) -> List[int]:
    l.sort()
    if l[-1] * l[-2] * l[-3] > l[0] * l[1] * l[-1]:
        return l[-3:]

    return [l[0], l[1], l[-1]]

# print(task2([1, 2, 3, 4]))
# print(task2([-1, -2, -3, 4]))
