#coding=utf-8
#编写方法实现对列表　元组的最大最小值
#创建两个测试的类型
testList = [12,32,2,14,5,43,234,54]
testTuple = (21,234,543,2,4,453,46,12)

#定义函数 求最大值
def max(obj): #形参是传输的是列表或者元组
	max = obj[0]#假设一个列表的开头是最大值
	myLen=len(obj)
	i=1
	
	while i<myLen:#遍历这个数组，如果max小于后面的元素　就把该元素赋值给max 
		if max<obj[i]:
			 max=obj[i]
		i+=1
	return max


#定义函数，求最小值
def min(obj): #形参是传输的是列表或者元组
	min = obj[0]#假设一个列表的开头是最大值
	myLen=len(obj)
	i=1
	
	while i<myLen:#遍历这个数组，如果max小于后面的元素　就把该元素赋值给max 
		if min>obj[i]:
			 min=obj[i]
		i+=1
	return min



#用一个变量接受返回的值并格式化输出

list_max = max(testList)
list_min = min(testList)
print(testList),
print("中最大值:%d"%list_max),
print("最小值:%d"%list_min)

tuple_max = max(testTuple)
tuple_min = min(testTuple)
print(testTuple),
print("中最大值:%d"%tuple_max),
print("最小值:%d"%tuple_min)