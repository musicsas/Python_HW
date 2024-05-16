def task5(s: str) -> bool:
    s = s.lower()
    if s[:len(s) // 2] == s[::-1][:len(s) // 2]:
        return True

    return False

# print(task5("acbca"))
# print(task5("ab"))
