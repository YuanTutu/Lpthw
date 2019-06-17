#creat a mapping of state to abbreviation
states = {#创建字典映射美国的州和简称
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}

#creat a basic set of states and some cities in them
cities = {#创建字典将美国州的简称和某个城市的全称映射
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'#字典中增加更多城市
cities['OR'] = 'Portland'

#print out some cities
print('-'*10)
print("NY State has: ",cities['NY'])#用州的简称获取城市全称
print("OR State has: ",cities['OR'])

#print some states
print('-'*10)
print("Michigan's abbreviation is: ",states['Michigan'])#用州的全称获取简称
print("Florida's abbreviation is: ",states['Florida'])

#do it by using the state then cities dict
print('-'*10)
print("Michigan has: ",cities[states['Michigan']])#全称——简称——再全称
print("Florida has: ",cities[states['Florida']])

#print every state abbreviation 
print('-'*10)
for state,abbrev in list(states.items()):#intems()将字典中的所有项以列表形式返回，但是形式是无顺序的，调用list()将元素转换成列表，列表再分别带入两个变量里面
    print(f"{state} is abbreviated {abbrev}")#先输出全称再输出简称

#print every city in state
print('-'*10)
for abbrev,city in list(cities.items()):#和第38行做的事情其实是一样的
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")#通过上面的代码获取简称之后再返回全称

print('-'*10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')#get()返回指定键的值，如果值不在字典里面就返回none。states.get(key,default=None)

if not state:
    print("Sorry,no Texas.")

#get a city with a default value
city = cities.get('TX','Does Not Exist')#调用get()返回指定键‘TX’和默认值'Does Not Exist'赋值给变量city
print(f"The city for the state 'TX' is :{city}")#打印变量，需要注意的打印的只有上面的默认值，键是不会打印的。
