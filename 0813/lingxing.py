#coding=utf-8
rows = raw_input("请输入要打印的行数")
rows = int(rows)
i=1
while i<=rows:
	j=1
	while j<=(i*2-1):	
	j+=1		
	
	print ""
	i+=1





 #i表示的行数，j控制的空格，k控制的是＊

'''
for i in range(rows):#变量i控制行数
	for j in range(rows - i):#(1,rows-i)
		print " ",
		j += 1
	for k in range(2 * i - 1):#(1,2*i)
		if k == 0 or k == 2 * i - 2:
			print "*",
		else:
			print " ",
		k += 1
	print "\n"
	i += 1
	#菱形的下半部分
for i in range(rows):
	for j in range(i):#(1,rows-i)
		print " ",
		j += 1
	for k in range(2 * (rows - i) - 1):#(1,2*i)
		if k == 0 or k == 2 * (rows - i) - 2:
			print "*",
		else:
			print " ",
		k += 1
	print "\n"
	i += 1
 '''