#coding=utf-8
#递归的求阶乘
def jiecheng(num):
	result=1
	if num>1:
		result = num *(jiecheng(num-1))
	else:
	 	result =1
	return result

# result=jiecheng(15)
# print(result)


#匿名函数
test1 = lambda a:a*3.14
b = 123
print test1(b)