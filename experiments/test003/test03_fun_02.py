# 作者:ZhaoYu Wang
# 日期:2021年10月27日
from collections import Counter
input = input("请输入一个数字")
input = int(input)
num = []
num_count={}
for i in range(2,input+1):
    num_count[i]=0
    while input % i ==0:
        num.append(i)
        num_count[i]+=1
        input /= 2
result = Counter(num)
c = 0
s = ''
for key,values in result.items():
    if c != 0:
        s+="*"
    s+=str(key)+"^"+str(values)
    c+=1
print(s)

