#coding=utf-8
rows =  raw_input("请输入打印的行数")
rows = int(rows)
i=1# i控制行数　j控制每行的空格　控制每行的＊
while i<=rows:
	j = 1
	while j<=rows-i:
		print(" "),
		j+=1
	k = 1
	while k<=(2*i-1):
	  print ("*"),
	  k+=1

	print ""
	i+=1
m=1　#重新定义的一个变量，不能用i不然会死循环．因为上面的会一直执行
while m<=rows-1:
	j = 1
	while j<=m:#打印的
		print(" "),
		j+=1
	k = 1
	while k<=((rows-m)*2-1):
	  print ("*"),
	  k+=1

	print ""
	m+=1
 											
