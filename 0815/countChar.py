#coding=utf-8
#从键盘输入字符
myString = raw_input("请输入需要统计的英文字符")
i=0
#创建一个列表　用于存储统计的字母
numString =[]
findNumString =[]#这是用于存储 字符和数字统计后的列表
#创建一个用于存储去重复的列表
notRepeat=[]
for x in myString:
	num=myString.count(x)
	numString.append(num)
	#用打印格式的方法形成新的列表
	findNumString.append("%s:%d"%(myString[i],numString[i]))
	i+=1
#从就得列表中取出元素，在新的列表中判断，如果没有则添加，有什么都不做
for x in findNumString:
	if x not in notRepeat:
		notRepeat.append(x)
#打印出最后的列表
print(notRepeat)
	