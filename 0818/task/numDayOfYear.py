#coding=utf-8
#用函数实现输入某年某月某日 判断这一天是这一年的第几天,闰年也考虑进去 20160818
#是今年的地几天

def judge_leapyeay(year):

	if (year%4 == 0 and (year%100 !=0 or year%400==0)):
		print"是闰年" #是闰年就返回1 这对应下面的元组
		return 1
	else:
		print"不是闰年"#是闰年就返回0 这对应下面的元组
		return 0

#定义一个列表.里面存储 每个月的天数 通过添加0 把月份和下标对其
month_day_num=[0,31,[28,29],31,30,31,30,31,31,30,31,30,31]

while True:
	#提示用户输入的年份
	date = raw_input("请输入日期例如:(20160818)")
	year = int(date[0:4])
	month = int(date[4:6])
	day = int(date[-2:])
	# print(year)
	# print(month)
	# print(day)

	#判断输入的年份是否是闰年,是就返回1 最后加上1 ,不是就返回0,最后总数也不影响
	two_month_flag=judge_leapyeay(year)


	#根据月份计算天数
	sum_month=0
	tow_month=0
	i=0
	while i<month:#这里面注意 如果是818,8月整月数是不能取到的,取前7个月,加上天数
		if i!=2:#当判断不是2月份时.累加天数
			sum_month+=month_day_num[i]		
		else:#当为二月是,单独存储
			tow_month=month_day_num[i][two_month_flag]
			#当计算到2月是  把月的天数加到总天数
			sum_month=sum_month+tow_month	
		i+=1
	#计算最后的天数
	find_day=sum_month+day

	print("%d年%d月%d日,是今年的第%d天"%(year,month,day,find_day))
	print(find_day)



