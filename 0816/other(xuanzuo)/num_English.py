#coding=utf-8

'''
列表,给出一个整值,返回代表改值的英文.比如输入89 返回"eigth-nine"
要求:返回符合英文语法规则的形式,比如输入"89" 返回"eigth-nine" 本联系的值限定在0-1000


***********
思路:对输入的字符串惊醒拆分,分离出 个位,十位,百位, 对应英文  在用字符串组合输出
首先得有rang(10)的英文

'''

#对这个一个三位数进行拆分.分别得到各个位的数
def chaifen_3(num):
	return_wei = []
	#除100 取整数就是百位
	bai_wei = num / 100
	return_wei.append(bai_wei)
	#除100取余数 在和10取整就是各位
	shi_wei = (num%100)/10
	return_wei.append(shi_wei)

	ge_wei = (num%100)%10
	return_wei.append(ge_wei)
	return return_wei

#定义一个函数,对两位数进行拆分

def chaifen_2(num):
	return_wei = []
	shi_wei = num/10
	return_wei.append(shi_wei)

	ge_wei = (num%100)%10
	return_wei.append(ge_wei)
	return return_wei



#创建列表 里面存储 rang(10)的英文,[10:100:20]的整数的英文
#这个列表是表示rang(20),因为20以内的英文很特别,需要单独列出,以上的可以通过组合
one_twnety = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
#列出各个整数阶段的[10:100:10],这里面的规律是40以上可以用4-9后面家ty
integer = ['hundred','ten','twenty','thirty','fourty','fifty','sixty','seventy','eightty','ninety']

#修复bug:当是整百数时,后面会出现zero 格式错误 列出整百的数,这些列表将单独输出  rang(100:1000:100)

bai_wei_integer = [100,200,300,400,500,600,700,800,900]
#修复bug:当是整十数是输出格式错误,列出整百的数,这些列表将单独输出  rang(30:100:20)
shi_wei_integer = [30,40,50,60,70,80,90]



#百位 hundred 例如 101  one hundred and one     159 one hundred and fifty-nine

#提示用户输入要输入的数字
input_num = int(raw_input("请输入一个0-1000的数字,我将返回给你他的英文: "))


if  input_num<1000 and input_num>0:
	#判断这个数书否是1000 是的话直接返回1000的英文


	if input_num == 1000:
		print "one thousand"

	#判断这个数的大小,如果小于20,则直接返回one_twnety对应的值
	elif input_num <=20:
		result=one_twnety[input_num]
		print(result)

		
	#修复bug:当是整百数时,后面会出现zero 格式错误 当输入的数为200,300 ....等整百数 就按这个格式输出
	elif input_num in bai_wei_integer:
		#单独取出 百位存在变量中
		bai_wei = input_num/100
		#从对应的列表中找到对应的英文
		bai_wei = one_twnety[bai_wei]
		#格式化输出

		print(bai_wei+" hundred ")


	
	#因为当百位为0时,还使用上面三位数拆分,输入会出现不合适的
	elif input_num>20 and input_num<100:

		#修复BUG:当是整十数是输出格式错误
		if input_num in shi_wei_integer:

			shi_wei = input_num/10
			shi_wei = integer[shi_wei]
			print(shi_wei)

		#调用两位的拆分方法  获取到十位 和各位的数 存在一个列表中
		else:
			temp=chaifen_2(input_num)

			#print(temp)
			#在对应的列表中找到英文
			shi_wei = integer[temp[0]]
			ge_wei = one_twnety[temp[1]]
			#格式化输出
			print (shi_wei+"-"+ge_wei)





#剩下就可以拆分了
	else:
		temp=chaifen_3(input_num)
		#print(temp)
		#拆分后的数数字存在一个列表中,而且是以整数存储 迭代他 用它为下标 去刚开始的列表中找相应的
		#调用三位数的拆分方法  获取到十位 和各位的数 存在一个列表中
		bai_wei = one_twnety[temp[0]]
		shi_wei = integer[temp[1]]
		ge_wei = one_twnety[temp[2]]
		#格式化输出
		print (bai_wei+" hundred and "+shi_wei+"-"+ge_wei)
else:
	print("你输入的不再这个范围内,请重新输入:")







