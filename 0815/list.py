#
#coding=utf -8
while True:
    days = input('请输入你这个月上班的天数：')
    if days <= 31:
        break
    else:
        print("输入错误，请重新输入。")
times = days * 2
price = 5
addPic = 0											
i = 1
while i <= times:	
	if addPic <= 100:
		addPic += price
	elif addPic > 100 and addPic <= 150:
		addPic += price * 0.8
	elif addPic > 150 and addPic <= 400:
		addPic += price * 0.5
	else:
		addPic += price
	i += 1
print("The month addPic of subway is %0.2f" %addPic)	
