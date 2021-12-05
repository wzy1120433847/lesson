# 作者:ZhaoYu Wang
# 日期:2021年10月19日

def make_pizza(*toppings):
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

def build_profile(first,last,**userinfo):
    profile = {}
    profile['first_name']=first
    profile['last']=last
    for key ,value in userinfo.items():
        profile[key]=value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)


def make_sandwiches (*materials):
        print((type(materials)))
        print("add",materials)

make_sandwiches('aaa')
make_sandwiches('bb','bbbbvvv')
make_sandwiches('dwad','1deff','dwdw')


def make_sandwiches2(**materials):
    print((type(materials)))
    print("add", materials)


make_sandwiches2(aaa=1)


