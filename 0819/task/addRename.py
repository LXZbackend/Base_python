#coding=utf-8
import os
#用一个列表存储当当前目录所以的文件
all_file_name=os.listdir('./../test/')
folderName='./../test/'
#创建一个新的名字.用列表存起了
new_name=[]
for name in all_file_name:
	newName="LiGe_make "+name

	new_name.append(newName)



# for x in new_name:
# 	print(x)



file_num=len(all_file_name)
i=0
while i<file_num:
	os.rename(folderName+all_file_name[i],folderName+new_name[i])
	# print(all_file_name[i])
	# print(new_name[i])
	i+=1
#print(new_name)


