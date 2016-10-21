#coding=utf-8
#1.二进制加解密,把从文本中的所有字符都变成字符对应的整数,加密就是加上密码,把运算完的整数在转成字符,存储.解密就是相反


#封装成为一个加密方法
def add_passwd(file,passwd):#类似于拷贝代码 只是在拷贝过程中对字符操作

	old_file = open(file,'rb')

	houzui_index = file.rfind('.')

	new_file_name=file[0:houzui_index]+"_add_pwd"+file[houzui_index:]#获取新的名称
	print(new_file_name)

	#打开一个新文件
	new_copy_Fname = open(new_file_name,'wb')
	#以每行的方式打开文件

	old_content=old_file.read(1) #循环的取每个字符

	while len(old_content)>0:
	
		num_old_content=(ord(old_content)+(passwd))#把字符转成整数,在和整数密码加
		# print(num_old_content)
		# print(type(num_old_content))

		new_copy_Fname.write(chr(num_old_content))#把整数转成字符存储.
		#print(num_old_content)
		#旧的文件继续读下一行
		old_content=old_file.readline(1)#把指针移到下一个字符,循环


	old_file.close()
	new_copy_Fname.close()





def deciphering(file,passwd):

	old_file = open(file,'rb')

	houzui_index = file.rfind('.')

	new_file_name=file[0:houzui_index]+"_dec_pwd"+file[houzui_index:]
	print(new_file_name)

	#打开一个新文件
	new_copy_Fname = open(new_file_name,'wb')
	#以每行的方式打开文件

	old_content=old_file.read(1)

	while len(old_content)>0:
		#把字符用转成整形,在加上解密密码再转成字符
		num_old_content=(ord(old_content)-(passwd))
		
		new_copy_Fname.write(chr(num_old_content))
		#print(num_old_content)
		#旧的文件继续读下一行
		old_content=old_file.readline(1)


	old_file.close()
	new_copy_Fname.close()






#死循环
while True:

	print("请根据菜单输入操作:")
	print("1.加密文件     2.解密文件    3.退出")

	num = int(raw_input("请输入序号:"))

	if num ==1:
		#输入一个要加密的文件名
		add_passwdfile=raw_input("请输入要加密的文件名字:")
		#在输入一个要加密的密码
		passwd=int(raw_input("请输入加密的密码:"))
	

		add_passwd(add_passwdfile,passwd)


	elif num ==2:
		undo_passwdfile=raw_input("请输入要解密的文件名字:")
		#在输入一个要解密的密码
		undo_passwd=int(raw_input("请输入解密的密码:"))
		deciphering(undo_passwdfile,undo_passwd)

	elif num ==3:
		break
	else:
		print("*"*30)
		print("你输入有误,请从新输入:")
		print("*"*30)
		continue


