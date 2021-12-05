# 作者:ZhaoYu Wang
# 日期:2021年10月18日


# 字典列表
alien_0={'color':'green','point':5}
alien_1={'color':'yellow','point':10}
alien_2={'color':'red','point':15}

aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

# 代码自动生成
aliens = []
for alien_num in range(0,30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

print("total num",str(len(aliens)))

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='red'
        alien['speed']='fast'
        alien['points']=10

for alien in aliens:
    print(alien)

# 列表存储在字典中
pizza = {
    'crust':'thick',
    'topping':['mushrooms','extra cheese']
}
print("crust"+pizza['crust'])
for topping in pizza['topping']:
    print("topping",topping)


users={
    'aeinstein':{
        'first':"aaa",
        'last':'bbb',
        'address':'ccc'
    },
    'mucrle:':{
        'first':'aaa222',
        'last':'bbb222',
        'address':'ccc222'
    }
}

for username , userinfo in users.items():
    for one , two in userinfo.items():
        print(one,"+++",two)


favourite={
    'one':['1','2'],
    'two':['3','4','5']
}
for name ,places in favourite.items():
    print(name)
    for place in places:
        print(name,"like",place)

cities = {
    "city_one":{
        'country':'one',
        'population':'10000',
        'fact':'1111111'

    },
    "city_two":{
        'country': 'two',
        'population': '20000',
        'fact': '222222'
    },
    "city_three":{
        'country': 'three',
        'population': '30000',
        'fact': '333333'
    }

}
for city ,cityinfo in cities.items():
    for first , content in cityinfo.items():
        print(first,content)
