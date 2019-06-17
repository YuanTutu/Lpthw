#100台车
cars = 100
#车内乘坐人数
space_in_a_car = 4.0
#司机人数
drivers = 30
#乘客人数
passengers = 90
#没有开出去的车的数量
cars_not_driven = cars - drivers
#可以开的车的数量
cars_driven = drivers
#车队最多承载多少人
carpool_capacity = cars_driven * space_in_a_car
#每辆车平均携带乘客数
average_passengers_per_car = passengers / cars_driven
#测试用
#average_passengers_per_car = carpool_capacity / passengers


print("There are", cars,"cars available")
print("There are only",drivers,"drivers available.")
print("There will be",cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today")
print("We have",passengers,"to carpool today.")
print("We need to put about",average_passengers_per_car,"in each car.")
