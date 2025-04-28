# Q: 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度
# example: abcabcbb


def func(s):
    res = 0
    sub_s = ""

    for c in s:
        if c not in sub_s:
            sub_s += c
            res = max(len(sub_s), res)
        else:
            sub_s = sub_s[sub_s.index(c) + 1:] + c

    return res


ss = ["abcabcbb", "abcabcd", "abcde"]
for s in ss:
    res = func(s)
    print("Result: " + str(res))
