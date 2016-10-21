#coding=utf-8

#用一个变量接受一个输入的数字
receive =input('请输入1-7之间的一个数')
if(receive == 1):
    print("今天是星期一")
elif(receive == 2):
    print("今天是星期二")
elif(receive == 3):
    print ("今天是星期三")
elif(receive == 4):
    print("今天是星期四")
elif(receive == 5):
    print("今天是星期五")
elif(receive == 6):
    print("今天是星期六")
elif(receive == 7):
    print("今天是星期天")
else:
    print("你是不是傻，输入有误")
