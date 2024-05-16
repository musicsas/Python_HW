def task6(s: str) -> int:
    for l in range(len(s), 0, -1):
        for i in range(len(s) - l + 1):
            substring = s[i:i + l]
            if substring == substring[::-1]:
                return len(substring)
    return 0

# print(task6("cdaaabca"))
# print(task6("ab"))