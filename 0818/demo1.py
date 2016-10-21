#coding=utf-8
def test(name,age=20):
	print("%s,%d"%(name,age))







def test1(age=1,*name):
	for x in name:
		print (x)
		print(age)

#test("haha")
test1("haha","asdfasd",19)
