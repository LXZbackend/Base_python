#coding=utf-8
#先提示用户多次输入路径，最后显示一个完成的路径，比如/home/python/ftp/share
myWay = []
gen = "/"
print("-"*30)
print("按两个空格即为输入完成")
print("-"*30)
while True:
	
	way = raw_input("请分开多次输入路径:")
	if way!='  ':
		myWay.append(way)
		
	else:
		break
myWay.insert([])
print ("你输入的路径为:%s"%gen.join(myWay))

