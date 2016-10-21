#coding=utf-8
#接受用户输入的数字

def  addNum(num):
	i=1
	sum=0
	while i<=num:
		sum+=i
		i+=1
	return sum



inputNum = raw_input("请输入一个数，我将返回给你累积和：")
inputNum = int(inputNum)

print("从１到%s的累加和为:%s"%(inputNum,addNum(inputNum)))
