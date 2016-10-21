#coding=utf-8
#用户输入，对字符串进行去空格处理．这个处理包括字符串前后　中间的处理．虽然提供的方法但是不完善
str_input = raw_input("请输入运算的数字：")
process_str_list = []
process_str=' '
#创建一个列表用于存储运算符的列表
operator_list = ['+','-','*','/']
operational = ''


#对这个字符串进行去空格处理
#对字符错进行便利　判断时否为空格，不是就存下来，最后一个新的字符串就是去空格的
#这里是自己写的一个去空格的方法　但是转换成列表里，字符串本身有一个方法　str.replace(" ",'')
f
or x in str_input:
	if x != " ":
		#将非空的字符串存在列表中
		process_str_list.append(x)


#print(process_str_list)
#通过循环判断输入的列表到底使用什么运算符　　并保存下来
for x in operator_list:
	if x in process_str_list:
		operational=x
#print (operational)	
#把这个列表转成字符串
process_str=process_str.join(process_str_list)

#调用　partition 生成一个元组通过刚开始运算符划分三部分，分别是，运算符，和运算符两边的数
#输出测试
#print(process_str.partition(operator))
# print process_str
# print (type(process_str))
tuple_input = process_str.partition(operational)


#通过对元组的截取　得到两个数字
num1 = tuple_input[0]
num2 = tuple_input[2]

#去除每个字符串字符之间的空格　例如('4 2 3 4 2 3 ', '+', ' 2 3 4 2 2 3 4')

num1 = num1.replace(" ",'')
num2 = num2.replace(" ",'')

#再把字符串转化成整数
num1 = float(num1)
num2 = float(num2)

#得到运算符
operational = tuple_input[1]


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



