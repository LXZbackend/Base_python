#coding=utf-8

# 学生管理系统

# 用来保存学生信息
nameList = []

while True:

	# 1. 输出功能选项
	print("-"*30)
	print("    python版学生管理系统 V8.8")
	print("1  添加学生信息")
	print("2  删除学生信息")
	print("3  修改学生信息")
	print("4  查询学生信息")
	print("5  退出系统")
	print("-"*30)

	# 2. 等待用户进行选择
	optionNum = int(raw_input("请进行选择（数字）:"))

	# 3. 根据用户的选择执行相应的是事情

	# 添加新信息
	if optionNum==1:

		#3.1 提示用户输入学生的名字并获取
		name = raw_input("请输入姓名:")

		#3.2 提示用户输入学生的籍贯并获取
		addr = raw_input("请输入籍贯:")


		#3.3.1 把姓名和籍贯进行组装
		tempInfo = {}

		tempInfo['name']=name
		tempInfo['addr']=addr

		#3.3 添加到系统中
		nameList.append(tempInfo)

		# for test
		# print(nameList)


	elif optionNum==2:

		if len(nameList)==0:
			print("*"*10)
			print("很抱歉，当前系统中，没有任何学生信息")
			print("*"*10)
			continue

		i = 0

		# 先提示当前所有的信息
		for info in nameList:
			print("%d     %s    %s"%(i, info['name'], info['addr']))
			i+=1

		# 让用户选择要删除的信息
		delNum = int(raw_input("请输入要删除的学生序号(数字):"))

		# 删除
		if delNum<len(nameList) and delNum>=0:
			del nameList[delNum]


	elif optionNum==3:
		# 先提示当前所有的信息

		i=0
		for info in nameList:
			print("%d     %s    %s"%(i, info['name'], info['addr']))
			i+=1

		# 输入要修改的学生序号
		modifyNum = int(raw_input("请输入要修改的学生序号(数字):"))


		# 输入新的姓名
		#3.1 提示用户输入学生的名字并获取
		name = raw_input("请输入新的姓名:")

		#3.2 提示用户输入学生的籍贯并获取
		addr = raw_input("请输入新的籍贯:")

		#3.3.1 把姓名和籍贯进行组装
		tempInfo = {}

		tempInfo['name']=name
		tempInfo['addr']=addr

		#3.3 添加到系统中
		nameList[modifyNum] = tempInfo

		# 输入新的籍贯

		# 再次确认

		# 修改

	elif optionNum==4:

		name = raw_input("请输入要查询的姓名:")

		for info in nameList:
			if info['name'] == name:
				print("**** 恭喜您找到了 *****")


	elif optionNum==5:
		confirm =raw_input("亲，你确定要退出系统么？~~~~(>_<)~~~~（yes/no）")

		confirm = confirm.lower()

		if confirm=='yes':
			break


