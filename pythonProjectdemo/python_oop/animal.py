'''

    写一个面向对象的例子：
    比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    创建子类【猫】，继承【动物类】
    重写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=短毛
    添加一个新的方法， 会捉老鼠，
    重写父类的‘【会叫】的方法，改成【喵喵叫】
    创建子类【狗】，继承【动物类】
    复写父类的__init__方法，继承父类的属性
    添加一个新的属性，毛发=长毛
    添加一个新的方法， 会看家
    复写父类的【会叫】的方法，改成【汪汪叫】
    在入口函数中创建类的实例
    创建一个猫猫实例
    调用捉老鼠的方法
    打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
    创建一个狗狗实例
    调用【会看家】的方法
    打印【狗狗的姓名，颜色，年龄，性别，毛发】

'''


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print("动物会跑")

    def call(self):
        print("动物有自己的叫声")


class Cat(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "短毛"

    def skill(self):
        print("捉到了老鼠")

    def call(self):
        print("喵喵叫")


class Dog(Animal):
    def __init__(self, name, color, age, sex):
        super().__init__(name, color, age, sex)
        self.hair = "长毛"

    def safe(self):
        print("会看家")

    def call(self):
        print("汪汪叫")


if __name__ == '__main__':
    cat1 = Cat("小猫", "white", 4, "fam")
    print(cat1.__dict__)
    c = cat1.skill()

    dog1 = Dog("小狗", "Yellow", 3, "fam")
    print(dog1.__dict__)
    dog1.safe()
