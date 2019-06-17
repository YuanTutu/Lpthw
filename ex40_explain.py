class Person(object):
    """从廖雪峰的文章评论里面看到的关于类/实例等概念的一些解释"""
#这里就是初始化你将要创建的实例的属性
    def __init__(self, hight,weight,age):
        self.hight = hight
        self.weight = weight
        self.age = age

#定义你将要创建的实例所有用的技能
    def paoniu(self):
        print("你拥有泡妞的技能")

    def eat(self):
        print("你拥有吃饭的技能")

#开始创建实例
zhangsan = Person(170,50,29)
lisi = Person(172,54,24)

#你的实例开始使用它的技能
zhangsan.paoniu()
lisi.eat()
