#coding=utf-8
rows=raw_input("请输入行数")
rows = int (rows)
i=1 
j=1
#打印上三角　前面空格逐渐递减，＊　逐渐递增　
while i<=rows:
	print(' '*(rows-i)+'*'*(i*2-1))
	i+=1
while j<=rows-1:
	#print(' '*j+'*'*(rows-j)+'*'*(rows-j-1))
	print(' '*j+'*'*((rows-j)*2-1))
	
	j+=1