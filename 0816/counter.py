#coding=utf-8
#编写一个计算机，能够实现输入两个数的加减乘除

#提示用户输入两个数，对输入的字符串进行拆分，找到两个数　和运算规则
result = 0
print ("输入两个数的运算，每输入一个字符后用一个空格隔开")
intput_str= raw_input("请直接输入两个数的运算（例如１ ＋ ２）：")
#去除字符串左边的空格
intput_str = intput_str.lstrip()
#去除字符串右边的空格
intput_str = intput_str.rstrip()

#将输入的字符串进行切割．存入一个列表中
str_list = intput_str.split(" ")

#输出　分割的字符串
#print (str_list)

#得到两个数,为了保证除法，保证一个数为浮点数
num1 = float(str_list[0])
num2 = int (str_list[-1])
#得到中间的运算符
operational = str_list[1]

#输出看是否是运算符
#print (operational)

#这样　输入的字符串中就能提取出　数字和运算符了
if operational== '+':
	result = num1 + num2
	print("%d %s %d = %d "%(num1,operational,num2,result))
elif operational =='-':
	result = num1 - num2
	print("%d %s %d = %d "%(num1,operational,num2,result))
elif operational =='*':
	result = num1 * num2
	print("%d %s %d = %d "%(num1,operational,num2,result))
elif operational =='/':
	if num2!= 0:
		result = num1 / num2
		print("%d %s %d = %d "%(num1,operational,num2,result))
	else:
		print"除数不能为0"

else:
	print("您输入的运算符有误，请从新输入")


