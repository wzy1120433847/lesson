# 作者:ZhaoYu Wang
# 日期:2021年11月21日

class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        print(f"{self.name} Restaurant is {self.type}")

    def open_restaurant(self):
        print(f"{self.name} is opening")


my_restaurant = Restaurant('aaa','bbb')
print(f" The name of the restaurant is {my_restaurant.name},The type of the restaurant is {my_restaurant.type}")
