from typing import List


def task1(l: List[int]) -> List[int]:
    l.sort()
    if l[0]*l[1] > l[-2]*l[-1]:
        return l[:2]
    else:
        return l[-2:]


# print(task1([1,2,3,4]))
# print(task1(list(range(100000))))
# print(task1([-1,-2,-3,4]))