from typing import List


def task3(l: List[int]) -> bool:
    for i in range(len(l) - 1):
        if l[i + 1] <= l[i]:
            return False
    return True


# print(task3([1, 2, 3, 4]))
# print(task3([-1, -2, 4, -3, 4]))
# print(task3([2, 2, 2]))
