#coding=utf-8
'''
随机数,设计一个"石头 ,剪刀,布"游戏,有时又叫"Rochambeau",
你小时候可能玩过,下面是规则,你和你的对手同一时间做出特定的手势,必须是下面的一种:
石头  剪刀 布
 胜利者从下面的规则中产生,
 尽量少使用if
********
思路:把用户输入的 和计算机随即产生的组成一个字符串,在输赢平局的元组匹配
在那匹配到了 查看元组 就是结果
'''
import random


#创建元组 定义各种规则
#赢了的所有情况
player_win = ('02','10','21')
#平局所有情况
equation=('00','11','22')                                           
#输了的所有情况
computer_fail = ('20','01','12')


#提示用户输入
player = raw_input('请输入：剪刀(0)  石头(1)  布(2):')

#用随机数产生计算机输入
computer = str(random.randint(0,2))


#将两个结果组成一个字符串
str_result = player + computer

#用while 判断循环 如果这个字符在那个元组中 就会返回true 就打印相应的结果

while str_result in player_win: #如果组成的字符串在获胜的这个元组中则会返回true,打印或者
	print"恭喜你,玩家你赢了"
	break                    #结束死循环
while str_result in equation:
	print "平局,你可以再来一句"
	break
while str_result in computer_fail:
	print"不要气馁,电脑赢了"
	break




#测试结果
# print(str_result)
# print (type(str_result))






