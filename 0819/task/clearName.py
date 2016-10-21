#coding=utf-8
#实现效果,对特定目录下的所有文件的名称进行 ,去掉重复的名字.

#暂时的思路时就是 .列出当前目录的文件名称,存在一个列表中,遍历列表.中的第一个元素,用第一个元素的
#的第一个字母去匹配第二元素..第三个....如果都相等. 匹配第一个元素的第二个字母...一直找到有一个不相同的.则说明,在这个字母之前是重复的,直接获得下标,截取剩下的字符.从新命名

import os
#创建一列表用于存储文件名称
file_name=os.listdir("./../test/")
folderName = "./../test/"
#创建一个变量,用于存储,找到文件名不同的下标
difference_index=0


#得到列表的长度 
len_list=len(file_name)
#得到其中一个元素的长度
len_ele=len(file_name[0])


# print(len_list)
# print(len_ele)


#***************************核心思想***********************
i=0 #创建一个外层循环,用于控制列表中的第几个元素
while i<len_ele:
	j=0  #创建变量,控制文件名的每个字母
	while j<len_list:
		#这里面比较,用每个元素的的第一个字母和其他其他几个元素的第一个字母比较
		#如果相同 再把每个元素的第二个字母和第一个元素的第二个字母比较
		#......抽象出来.以第一个元素的字母为标转,如果找到不相同的字母就返回这个下标.

		#后面的也不用比较了.则这个下标之前的都是 相同的.去掉即可
		if file_name[j][i]!=file_name[0][i]:
			difference_index=i  #将不同的下标得到
			# print(difference_index)
			# print(type(difference_index))
		j+=1

	i+=1

	
	


#修改名字  
k=0 #定义一个循环变量
while k<len_list: #修改的名字为,取原来名字,不同字母之后的所以名字
	os.rename(folderName+file_name[k],folderName+file_name[k][difference_index:])
	# print(all_file_name[i])
	# print(new_name[i])
	k+=1