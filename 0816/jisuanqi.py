#coding=utf-9
#用户输入，对字符串进行去空格处理．这个处理包括字符串前后　中间的处理．虽然提供的方法但是不完善
str_input = raw_input("请输入运算的数字：")
process_str_list = []
#对这个字符串进行去空格处理
i=0
for x in str_input:
	if x != " ":
		process_str_list.append(x)


