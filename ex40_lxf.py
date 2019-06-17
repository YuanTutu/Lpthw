# 下面为常规打印成绩的方法
"""
std1 = {'name':'michael','score':98}
std2 = {'name':'mike','score':81}
def print_score(std):
    print('%s:%s' % (std['name'],std['score']))

print_score(std1)
print_score(std2)
"""
#定义类的方式打印成绩
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s'%(self.name,self.score))
#下述打印方式配合第三四行的定义方式会有错误
#std1.print_score()
#std2.print_score()
std1 = Student('michael',98)
bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',62)
bart.print_score()
lisa.print_score()
std1.print_score()
