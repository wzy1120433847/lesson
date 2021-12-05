# 作者:ZhaoYu Wang
# 日期:2021年10月12日

cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'Audi'
print(car=='audi')
print(car.lower()=='audi')  #  lower 暂时性，不改变原有值


age = 12
if age <4:
    print('0')
elif age < 18:
    print('5')
else:
    print('10')

a = ''
if a :
    print('1')
else:
    print('2')

