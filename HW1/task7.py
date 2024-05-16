from collections import Counter

def task7(s: str) -> int:

    s_num = Counter(s)
    result = ""
    for i in s_num:
        result += i * (s_num[i] // 2)
        s_num[i] -= s_num[i] // 2 * 2
    result += dict(map(reversed, s_num.items())).get(1, '') + result[::-1]
    return len(result)

# print(task7("aaabbc"))
