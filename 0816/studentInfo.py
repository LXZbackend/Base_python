#coding=utf-8
#通过键盘输入学生信息
#首先创建学生的基本信息
Name ='Name'
age ='age'
sex='sex'


#创建一个一个存储学生信息的列表
Student_list=[]
#创建一个字典．用于存储键盘的输入对应的信息

while True:


	print("*"*70)
	print("1.增加学生信息，２.删除学生，３．修改学生信息，４．查询学生信息，5.退出")
	print("*"*70)
	opNum = raw_input("请输入对应的菜单序号：")
	opNum = int(opNum)
	if (opNum == 1):

		#infoTemp = {"Name":"lixianzhu","age":"19","sex":"man"}
		infoTemp = {}
		#将每个学生的姓名单独存在一个列表中，方便以后对学生姓名是否存在进行判断
		namelist = []


		#通过键盘输入学生信息
		input_Name = raw_input("请输入学生的%s:"%Name)
		

		
		if input_Name not in namelist:
			namelist.append(input_Name)
			input_age = raw_input("请输入学生的%s:"%age)
			input_sex = raw_input("请输入学生的%s:"%sex)

			infoTemp[Name] = input_Name
			infoTemp[age] = input_age
			infoTemp[sex]  = input_sex
			Student_list.append(infoTemp)
		else:
			print("该姓名已经存在了")
			continue
		print(infoTemp)

	#  elif(opNum == 2):
	#  #打印出现在已经有的列表信息
	# 	print(Student_list)
	# 	del_name = raw_input(cdss"请输入删除学生的姓名:")
	# #定义一个i遍历已经存储的列表中全部名字，并与输入的相匹配，如果相同，则删除该下标的学生信息
	# 	i=0
	# 	for num in Student_list:
	# 		if Student_list[i][Name]==del_name:
	# 			del　Student_list[i]
	# 			i+=1
