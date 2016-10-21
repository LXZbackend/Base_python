#coding=utf-8
#写一个程序，判断用户输入的标识符是否合法，根据数字，字母下划线等去判断！
#利用正则表达式．
import re
myList = []
#循环的的将输入的字符串添加到列表中
while True:
	inputName = raw_put("请输入标识符")
	if inputName == '':
		break
	else
	myList.append(inputName)
#遍历这个列表，和正则想匹配

for x in myList:
	if re.match('[A-Za-z]',s):#判断是否是由大小写字母组成　　通过进入下面一个
		if re.search('[_]|\w',s):#判断是否含有下划线　
			print 'True'
		else:
			print "False"
	else:
		print 'False'
