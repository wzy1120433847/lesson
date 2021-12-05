# 作者:ZhaoYu Wang
# 日期:2021年10月12日

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0]=100      TypeError: 'tuple' object does not support item assignment
# print(dimensions[0])

for dimension in dimensions:
    print(dimension)

dimensions=(400,100,50)
for dimension in dimensions:
    print(dimension)