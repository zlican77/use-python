#题目

#给定一个十进制整数字符串，判断它是否是 4 的幂。

#示例 1

#输入："16"，输出：true

#示例 2

#输入："101"，输出：false

#示例 3

#输入："70368744177664"，输出：true

get = eval(eval(input()))
while get % 4 == 0:
    get = get // 4
if get == 1:
    print('true')
else:
    print('false')
