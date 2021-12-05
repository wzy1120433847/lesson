# 作者:ZhaoYu Wang
# 日期:2021年10月03日

squares = [value**2 for value in range(1,11)]
print(squares)

# test
num = list(range(1,100000001))
print(min(num))
print(max(num))
import time;  # 引入time模块

t1 = time.time()
print ("time1:", t1)
c=sum(num)
t2 = time.time()
print ("time2",t2)
print("t2-t1",t2-t1)
c=0
for i in range(1,100000001):
    c+=i
t3=time.time()
print("t3-t2",t3-t2)
