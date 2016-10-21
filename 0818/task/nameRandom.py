#coding=utf-8
#需求 随即输出班级人的名字,假如有迟到的人,增加其,下次选中概率
#导入随机数包,并且生成一个随即数
'''
本来的思路是 创建一个列表 获取列表的长度,利用下标获取,随机数.
但是在random中找到一个方法,直接在列表中随即选取一个元素.


确认这个列表的长度,生成该长度的随机数
name_list_len = len(all_Student_Name)

生成一个0-len 的随机数.注意列表下标比长度少1
random_Num = random.randint(0,name_list_len-1)
print(all_Student_Name[random_Num])
'''
import random

#定义一个列表,其中存储所有人的姓名
all_Student_Name = ['lixianzu','yufei','gengxiubing','lipengfei']
#random.choice 实在列表中随即返回一个元素.
#print(random.choice(all_Student_Name))


#想增大某个元素的概率,第一种方法就是 增加该元素在列表中的次数
'''加权随即算法一般应用在一下场景,有一个集合S,里面的比如有ABCD 这是我们想从中随即抽取一项
单数抽取的概率不同,一般来说,我们可以给各项附一个权重,抽取的概率,正比于这个权重,那么上述几个就成了
{A:5,B:2,c:2,d:1}
把序列按权重值扩展成 list[A,A,A,A,A,B,B,C,C,D]
	param list:待选取的序列
	param weight:list对应的权重序列
	return:选取的值

'''

def weight_choice(list,weight):
	new_list = []
	for i,val in enumerate(list):
		# print(i)  i是下标
		# print(val)  val 是对应的元素
		new_list.extend(val * weight[i])
	return random.choice(new_list)


print(weight_choice(['A','B','C','D'],[5,2,2,1]))





'''
	方法二:计算权重总和sum,然后在1到sum之间随即选取一个数,之后遍历整个集合,统计遍历的项
	的权重之和 如果大于等于R 就停止遍历,选择遇到的项


'''
list =['A','B','C','D','E']
def weight_choice2(weight):
 	'''
 	param weight :list对应的权重序列
 	return : 选取的值在原列表里的索引

 	'''


 	t = random.randint(0,sum(weight)-1)
 	for i,val in enumerate(weight):
 		t -=val
 		if t<0:
 			return i 

print(list[weight_choice2(5,2,2,1,2,3)])
接
'''
	可以先对原始序列按照权重排序.


'''