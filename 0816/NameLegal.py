#coding=utf-8
#写一个程序，判断用户输入的标识符是否合法，根据数字，字母下划线等去判断！
#利用正则表达式．
import re
#倒入一个关键字包
import keyword
#将所有的关键字存在一个列表中
allKeyword = keyword.kwlist
myList = []
#循环的的将输入的字符串添加到列表中
while True:
	print　'连续输入两个回车是结束输入标识符'
	inputName = raw_input("请输入标识符")
	if inputName == '':
		break
	else:
		myList.append(inputName)
#遍历这个列表，和正则想匹配
for s in myList:
	#判断输入的标识符是否在　关键字列表中，如果在　则输出错误．如果不再则继续判断
	if s not in allKeyword:
		if re.match('[A-Za-z]',s):#判断是否是由大小写字母组成　　通过进入下面一个
			if re.search('[_]|\w',s):#判断是否含有下划线　
				print 'True'
			else:
				print "False"
		else:
			print 'False'
	else:
		print "你输入的是关键字"
