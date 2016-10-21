#coding=utf-8

rows = int(raw_input('请输入打印菱形的行:'))
i = j= k = 1
for i in range(rows):
	#for j in xrange(rows -i):
	while j<rows-i:
		
		print " ",
		j+=1
	#for k in xrange(i*2-1):
	while k<(i*2-1):
		print "*",
		k+=1
	print '\n'
   

for i in range(rows):
	#for j in range(i):
	while j<i:
		pass
		print' '
	  	j += 1
	#for k in range(2 * (rows - i) - 1):
	while k<(2 * (rows - i) - 1):	
		 print "*",
		 k += 1
    
    

'''
rows = int(raw_input('请输入打印菱形的行:'))
#rows = int(raw_input('please enter a rows! '))
i = j = k =1#声明变量　ｉ用于控制外层循环．j 用于控制空格的个数
#k用于控制＊的个数
print "打印空心等菱形，这里去掉if-else条件判断就是实心的"
for i in range(rows):#变量i控制行数
    for j in range(rows - i):#(1,rows-i)
        print " ",
        j += 1
    for k in range(2 * i - 1):#(1,2*i)
        #if k == 0 or k == 2 * i - 2:
            print "*",
        # else:
        #     print " ",
        k += 1
    print "\n"
    i += 1
    #菱形的下半部分
for i in range(rows):
    for j in range(i):#(1,rows-i)
        print " ",
        j += 1
    for k in range(2 * (rows - i) - 1):#(1,2*i)
        # if k == 0 or k == 2 * (rows - i) - 2:
            print "*",
        # else:
        #     print " ",
        k += 1
    print "\n"
    i += 1

'''








