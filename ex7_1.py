print("Mary had a little lamb.")#一般打印
print("Its fleece was white as {}.".format('snow'))#直接格式化snow这个字符串并嵌入到前面的打印里面
print("And everywhere that Mary went.")#一般打印
print("."*10) #what'd that do?#输出十个点
"""
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
"""
#watch that comma at the end.try removing it to see what happens
"""
print(end1 + end2 + end3 + end4 + end5 + end6,end = ' ')#将end1-6连接起来打印
print(end7 + end8 +end9 +end10 + end11 +end12)#将end7-12链接起来输出
"""
#将习题8中的formatter函数的方式带入
formatter="{}{}{}{}{}{}{}{}{}{}{}{}"
print(formatter.format("c","h","e","e","s","e"," ","b","u","r","g","e","r"))
