#题目

#给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略空格、字母的大小写。

#示例

#输入："A man, a plan, a canal: Panama"，输出：true

get = eval(input())
get = get.lower()
li = []
for i in range(len(get)):
	for k in 'abcdefghijklmnopqrstuvwxyz':
		if get[i] == k:
			li.append(k)
tmp = True
for i in range(len(li)):
	if li[i] != li[-i-1]:
		tmp = False
print(tmp)