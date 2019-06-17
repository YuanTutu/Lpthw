name = 'Zed A.Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
#尝试数据转换
#英寸转换厘米
height_cm=height*2.54
#磅转换千克
weight_kg=weight*0.453
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
#原本没有round()函数，测试四舍五入
print(f"He's {round(height_cm)} cm tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {round(weight_kg)} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky,try to get it exactly right
total = age + height + weight
print(f"If I add {age},{height},and {weight} I get {total}.")
