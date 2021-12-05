# 作者:ZhaoYu Wang
# 日期:2021年11月20日

def make_pizza(size,*topppings):
    print("\nmakeing a "+str(size)+"inch,toppings:")
    for toppping in topppings:
        print("- ",toppping)
