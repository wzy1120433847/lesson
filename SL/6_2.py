# 作者:ZhaoYu Wang
# 日期:2021年10月12日

alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_pos']=0
alien_0['y_pos']=125
print(alien_0)
alien_0['color']='yellow'
print(alien_0)


# 删除键值对
# {'color': 'yellow', 'points': 5, 'x_pos': 0, 'y_pos': 125}
del alien_0['color']
print(alien_0)
# {'points': 5, 'x_pos': 0, 'y_pos': 125}

# 由类似对象组成的字典
favourite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
print(favourite_languages)
# {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
print("Sarah's favourite_language is "+favourite_languages['sarah']+".")

num={
    'a':1,
    'b':2,
    'c':3,
    'd':4
}
for i in num:
    print(i,num[i])