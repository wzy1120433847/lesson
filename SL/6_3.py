# 作者:ZhaoYu Wang
# 日期:2021年10月12日

#  遍历所有的键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    'aaaa':123132,
    'dwwdwd':48887,
    'zdwf':3333,
    'cc':3333
}

for key,value in user_0.items():
    print('\n'+key)
    print(value)

# 遍历所有的键
for key in user_0.keys():
    print(key)
# 查看某个键是否不在字典中
if 'address' not in user_0.keys():
    print('No Address')

# 对键进行排序再输出
for key in sorted(user_0.keys()):
    print(key.title())

print('\n')
# 遍历所有的值
for value in user_0.values():
    print(value)
print('\n')
# 遍历值，去除重复元素
for value in set(user_0.values()):
    print(value)

# 6_3 测试题
people=('a','b','c','d')
survey={'a':1,'c':2}

for person in people:
    if person in survey.keys():
        print('done')
    else:
        print('quickly!',person)