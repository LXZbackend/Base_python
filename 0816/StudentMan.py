#coding=utf-8
'''

 1.编写“学生管理系统”，要求如下：
  必须使用自定义函数，完成对程序的模块化
  学生信心至少包含：姓名、年龄、学号，除此以外可以适当添加
  必须完成的功能：添加、删除、修改、查询、退出
'''
#创建一个列表用来存储学生的信息
user_info = []



def menuInfo():
	# 1. 输出功能选项
	print("-"*30)
	print("    python版学生管理系统 V8.8")
	print("1  添加学生信息")
	print("2  删除学生信息")
	print("3  修改学生信息")
	print("4  查询学生信息")
	print("5  退出系统")
	print("-"*30)


	

#定义一个增加用户信息的函数
def add_student_info():
	#提示用户输入学生的姓名
	add_user_name = raw_input("请输入添加学生的姓名:")

	#提示输入学生的年龄
	add_user_age = raw_input("请输入添加学生的的年龄:")
	#提示输入学生的籍贯
	add_user_brithLocal = raw_input("请输入添加学生的的籍贯:")
	#创建一个字典,用来暂时存放输入的学生信息
	temp_dict = {}
	#把各种信息存入字典中
	temp_dict["name"] = add_user_name
	temp_dict["age"] = add_user_age
	temp_dict["addr"] = add_user_brithLocal
	#test

	#print (temp_dict)
	#把字典追加在列表中

	user_info.append(temp_dict)
	print(user_info)
#定义一个删除学生信息的函数
def del_student_info():
	if len(user_info) == 0:
		print("*"*10)
		print("很抱歉，当前系统中，没有任何学生信息")
		print("*"*10)
		
	#调用格式化输出函数
	form_print_info()
	 #让用户输入删除的序号
	del_num = int(raw_input("请输入删除的学生的序号:"))
	 #删除
	if del_num<len(user_info) and del_num>=0:
		del user_info[del_num]
		print(user_info)



#定义一个更新学生信息的函数
def update_student_info():
	form_print_info()
	#输入修改的学生编号
	modifyNum = int(raw_input("请输入修改的学生编号:"))
	#输入新的姓名
	name = raw_input("请输入新的姓名:")
	#输入新的年龄
	age = raw_input("请输入新的年龄")
	#输入新的地址
	addr = raw_input("请输入新的籍贯:")


	#把信息进行组装
	temp_dict = {}
	temp_dict["name"] = name
	temp_dict["age"] = age
	temp_dict["addr"] = addr


	#输出提示修改的提示信息,并询问是否确认修改
	print("*"*40)
	print("您是否把")
	#这个为修改前的信息
	print(user_info[modifyNum])
	print("*"*40)
	print("修改为")
	#这个为打算修改成的信息
	print(temp_dict)
	#添加到系统中

	#让用户确认修改的数据
	confirm_update = raw_input("是否确认修改（yes/no）")
	#对输入的字符转换成小写,并且判断
	confirm_update = confirm_update.lower()
	if confirm_update == 'yes':
		user_info[modifyNum]=temp_dict
	#再次输出这是学生列表中的信息
	form_print_info()


#定义查找是否存在学生的函数
def find_student_info():
	#提示用户输入要查询的人的姓名
	find_name = raw_input("请输入要查询人的姓名:")
	for info in user_info:
		if info['name'] == find_name:
			print("-"*40)
			print("***** 恭喜您找到了 *****")
			print("-"*40)
		else:
			print('-'*15+'!'+'-'*15)
			print("没有找到该用户的信息!请从新确认!")

	
#格式的输出学生信息
def form_print_info():
	i = 0
	for info in user_info:
		print (" 序号   姓名    年龄    籍贯")
		print ("%d   %s    %s    %s"%(i,info["name"],info["age"],info["addr"]))


#死循环
while True:
	
	menuInfo()
	#用户的菜单输入
	menu_input = raw_input("请输入选择的菜单序号")
	menu_input = int(menu_input)


	#添加用户操作
	if menu_input == 1:
		add_student_info()


	#删除学生信息	
	elif menu_input == 2:
		del_student_info()


	#修改学生信息
	elif menu_input == 3:
		update_student_info()
		
	#查找学生的姓名
	elif menu_input == 4:
		find_student_info()
		



	elif menu_input == 5:
		confirm =raw_input("亲，你确定要退出系统么？~~~~(>_<)~~~~（yes/no）")
		confirm = confirm.lower()

		if confirm=='yes':
			break