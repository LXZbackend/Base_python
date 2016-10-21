#coding=utf-8
#用函数,输出100-200之间的素数
#除了1和本身能被整出,其他都不能被整除的数
import math
def suNum():
		#创建一个空列表,用与存放找到的素数
	suList = []
	for x in xrange(101,201):
		sqrt_num=int(math.sqrt(x))

		for y in xrange(2,sqrt_num+1):#这里用到了今天的位移,右位移就是除2 
			if x%y ==0:
				break
			if y == sqrt_num:
				suList.append(x)#这个列表中会有很多重复的
	return suList



su_num=set(suNum())#用集合的性质可以去重复,当然也可以再用一个空列表判断.
print(su_num)

'''
def func_get_prime(n):
	return fi
ler'''