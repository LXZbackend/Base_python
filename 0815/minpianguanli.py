#coding=utf-8
# 第一步：打印出菜单,输入的数字对应的功能
# 1.增加用户　２，删除用户　３　修改用户　４　查询用户　５退出
# 创建刚开始的用户列表
# 封装共同的打印　封装一个函数
#创建列表
userList = ['李献铸','余飞','耿秀兵','李鹏飞']
#这是打印用户的信息的方法

def printList(listinfo):
	i=0
	for x in listinfo:
		print("%d:%s"%(i,x)),
		
		i+=1
	print("")
while True:
	
	print("-"*30)
	print("1.增加用户，２.删除用户，３．修改用户，４．查询用户，5.退出")
	print("-"*30)



	numInput = raw_input("请输入对应的菜单序号")
	numInput = int(numInput)

	if (numInput == 1):
		#显示已经有的用户
		printList(userList)
		useradd = raw_input("请输入增加人的姓名：")
		userList.append(useradd)
		printList(userList)

	elif (numInput ==2):
		printList(userList)
		userRemo = raw_input("请输入要删除人的姓名:")
		userList.remove(userRemo)
		printList(userList)

	elif (numInput == 3 ):
		printList(userList)
		updateUserNum = raw_input("请输入要修改人的序号:")
		
		updateUserNum = int(updateUserNum)
		newName = raw_input("请输入新的名字:")
		userList[updateUserNum]=newName
		printList(userList)
	elif (numInput == 4):
	    findUserName = raw_input("请输入查询人的姓名：")
	    if findUserName not in userList:
	    	print("你查询的用户不存在!!")
	else:
		break
	   
