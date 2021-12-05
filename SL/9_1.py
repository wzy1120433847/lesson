# 作者:ZhaoYu Wang
# 日期:2021年11月20日

class Dog:
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性，name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗收到命令时蹲下"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """模拟小狗收到命令时打滚"""
        print(f"{self.name} rolled over!")


my_dog = Dog('Whillie', 6)

print(f"my dog's name is {my_dog.name}")
print(f"my dog is {my_dog.age} years old")






# f string
name = "HUAWEI"
print(f"my name is {name}")

num = 2
print(f"I have {num} apples")

price = 95.5
print(f"it is {price}$")

print(f"They have {2 + 5 * 2} apples")

name = "HUAWEI"
print(f"{name:>20}")  # 左填充
print(f"{name:<20}")  # 右填充
print(f"{name:^20}")  # 居中填充

print(f"{name:_<20}")
print(f"{name:_>20}")
print(f"{name:_^20}")

a = 12
b = -25
print(f"{a:+}")  # +12
print(f"{b:+}")  # -25

print(f"{a:-}")  # 12
print(f"{b:-}")  # -25

print(f"{a: }")  # 12 (前面右空格)
print(f"{b: }")  # -25

a = 123.456

# 只指定width
print(f"{a:10}")  # 123.456

# 只指定0width
print(f"{a:010}")  # 000123.456

# 使用width.precision
print(f"{a:8.1f}")  # 123.5
print(f"{a:8.2f}")  # 123.46
print(f"{a:.3f}")  # 123.456

a = "Hello"
# 当发生截断的时候，如果不指定填充符，默认使用空格填充
print(f"{a:10.3}")  # Hel
# 在发生截断的时候，使用指定的填充符
print(f"{a:_>10.3}")  # _______Hel
print(f"{a:_<10.3}")  # Hel_______


#  f-string针对date、datetime和time对象，进行年月日、时分秒等信息提取
from datetime import *
# today()返回本地时间的一个date对象
a = date.today()
print(a)  # 2021-11-21
print(type(a))  # <class 'datetime.date'>
print(f"{a:%Y---%m---%d}")  # 2021---11---21


my_dog.sit()
my_dog.roll_over()
