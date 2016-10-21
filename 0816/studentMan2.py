#coding=utf-8
'''
1.编写“学生管理系统”，要求如下;
必须使用自定义函数，完成对程序的模块化
学生信心至少包含：姓名、年龄、学号，除此以外可以适当添加
必须完成的功能：添加、删除、修改、查询、退出
'''
#创建一个列表 用于存储学生的信息
student_info = []


def menu_info():
	# 1. 输出功能选项
	print("-"*30)
	print("    python版学生管理系统 V8.8")
	print("1  添加学生信息")
	print("2  删除学生信息")
	print("3  修改学生信息")
	print("4  查询学生信息")
	print("5  退出系统")
	print("-"*30)

#定义一个添加学生信息的函数
def addStudent_info():
	#创建一个字典,用于存放添加的信息
	temp_info = {}
	#提示用户输入学生的各种信息
	#1.添加学生的学号
	student_ID = raw_input("请输学生的学号:")
	#2.添加学生的姓名
	name = raw_input("请输入学生的姓名:")

	#对输入的ID 和姓名同时进行存在性判断,如果管理系统中没有则可以添加,有了就不能添加
	# for info in student_info:
		# if info[name] == name:
		# #if not ((info[name] == name) and (info[student_ID] == student_ID ): 	#3.添加学生的年龄
	age = raw_input("请输入学生的年龄:")
	#4.添加学生的籍贯
	addr = raw_input("请输入学生的籍贯:")

	#把输入的信息添加到字典中
	temp_info["ID"] = student_ID
	temp_info["name"] = name
	temp_info["age"] = age
	temp_info["addr"] = addr
	#将字典存在最开始的列表
	student_info.append(temp_info)
	print(student_info)

#定义删除学生信息的函数
def delStudent_info():
	if len(student_info)==0:
			print"学生的系统信息为空"

	else:
		print_info()
		#提示用户删除的序号,通过序号删除学生
		del_num = int(raw_input("请输入删除的学生信息的序号"))
		#判断输入的是否符合
		student_info_lenght=len(student_info)
		if del_num<student_info_lenght and student_info_lenght>0:
			del student_info[del_num]
			#打印出这时候的学生信息表
			print(student_info)




#创建一个函数,格式化输出已经存在的学生信息
def print_info():
	#输入学生信息
	i=0
	for info in student_info:
		print ("序号    学号    姓名    年龄    地址  ")
		print("%d       %s      %s      %s     %s"%(i,info["ID"],info["name"],info["age"],info["addr"]))

def update_info():

	#创建一个字典,用于存放添加的信息
	temp_info = {}
	print_info()
	#提示用户输入序号修改学生的信息
	input_num = int(raw_input("请输入修改学生的序号:"))


	update_name = raw_input("请输学生的新姓名:")
	update_ID = raw_input("请输学生的新学号:")
	update_age = raw_input("请输入学生的新年龄:")
	#4.添加学生的籍贯
	update_addr = raw_input("请输入学生的新籍贯:")

	#把输入的信息添加到字典中
	temp_info["ID"] = update_ID
	temp_info["name"] = update_name
	temp_info["age"] = update_age
	temp_info["addr"] = update_addr

	#提醒用户是否确认修改
	print("你是否把")
	#打印原来的数据
	print(student_info[input_num])
	print("修改成")
	#打印修改的数据
	print(temp_info)
	#让用户确认修改的数据
	confirm_update = raw_input("是否确认修改（yes/no）")
	confirm_update=confirm_update.lower
	if confirm_update=="yes":
		student_info[input_num]=temp_info
	print_info()





#定义查找是否存在学生的函数
def find_student_info():
	#提示用户输入要查询的人的姓名
	find_name = raw_input("请输入要查询人的姓名:")
	for info in student_info:
		if info['name'] == find_name:
			print("-"*40)
			print("***** 恭喜您找到了 *****")
			print("-"*40)
		else:
			print('-'*15+'!'+'-'*15)
			print("没有找到该用户的信息!请从新确认!")
			print('-'*15+'!'+'-'*15)





# while True:
	

	#打印菜单,调用函数
	menu_info()
	#接受用户输入的选择,进行判断并且做出相对应的操作
	user_input = raw_input("请输入选择操作的菜单序号:")
	user_input = int(user_input)


	#添加用户信息
	if user_input == 1:
		addStudent_info()

	#删除用户信息
	elif user_input == 2:
		delStudent_info()




	#修改学生的信息
	elif user_input == 3:

		update_info()

	#查找用户
	elif user_input == 4:
		find_student_info()

	elif user_input == 5:
		
		confirm =raw_input("亲，你确定要退出系统么？~~~~(>_<)~~~~（yes/no）")
		confirm = confirm.lower()

		if confirm=='yes':
			break
	else:
		print('-'*15+'!'+'-'*15)
		print("输入的菜单序号有误,请从新选择!")
		print('-'*15+'!'+'-'*15)
			
			
