# 作者:ZhaoYu Wang
# 日期:2021年10月18日

unconfirmed_users = ['a', 'b', 'c']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)
    print("current_user" + current_user)
    print("unconfirmed_users", unconfirmed_users)  # pop是永久性的

print("unconfirmed_users+++", unconfirmed_users)
print("confirmed_users", confirmed_users)

# 删除包含特征值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
# 设置一个标志，指出调查是否继续
polling_activate = True

while polling_activate:
    # 提示输入名字和回答
    name = input("what is name ?")
    response = input("which mountain would you like to climb somdday?")

    # 将答卷收入字典
    responses[name] = response

    # 看看还有没有人
    repeat = input("another (yes/no)")
    if repeat == 'no':
        polling_activate = False

for name ,response in responses.items():
    print(name,response)
