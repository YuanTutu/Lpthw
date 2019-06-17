from sys import argv#从sys库里导入argv模块

script,filename = argv

print(f"We will reading the file {filename}")
print("Opening the file...")

target = open(filename)

print(target.read())

target.close()
