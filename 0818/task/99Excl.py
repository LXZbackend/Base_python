#coding=utf-8
#打印99乘法表

#设置两个循环一个控制外面,一个控制里面
'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=4 
1*4=4 2*4=8
1*5=5 2*5=10
1*6=6 2*6=12 .........


'''
def multiplication():
	print"9x9table"
	for i in xrange(1,10):#i的取
		for j in xrange(1,i+1):
		#	print j,'x',i,'=',j*i,'\t'
			print("%d * %d = %d\t"%(j,i,j*i)),
		print('\n')
			
multiplication()