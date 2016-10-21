#coding=utf-8
#输入一个数,判断其是否是闰年
#闰年能被四百整除.     能被四整除,但是不能被100整除

def judge_leapyeay(year):

	if (year%4 == 0 and (year%100 !=0 or year%400==0)):
		print"是闰年"
	else:
		print"不是闰年"



#提示用户输入一个年份
day = int(raw_input("请输入要判断的年份:"))

judge_leapyeay(day)