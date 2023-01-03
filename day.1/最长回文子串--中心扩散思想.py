# 给定一个字符串，找出该字符串中最长回文子串的长度。

# 示例 1

# 输入："abc"，输出：0

# 示例 2

# 输入："abcbe"，输出：3

# 示例 3

# 输入："acdcecdcf"，输出：7

#!!!!!!!!!!
# 中心扩散法
get = eval(input())
get = "#" + get + "&"
m = 0
for i, ch in enumerate(get):
    j = 1
    s = 0
    if i == 0:
        continue
    elif i == len(get) - 1:
        break
    else:
        while get[i - j] == get[i + j]:
            s = 1
            j += 1
            s += 2
        if s > m:
            m = s
print(m)
