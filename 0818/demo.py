#coding=utf-8
#编写一个函数,求三个数 的和,求起平均值,三个数传入
def addNum(*num):
	result=0
	for x in num:
		result +=x
	return result




def avg(*num):
	i =0
	lenNUm=len(num)
	for x in num:
		
	
	print("平均值为:%s"%(result/lenNUm))


#avg(12,12,2)

# q=addNum(12,11,11)
# print(q)