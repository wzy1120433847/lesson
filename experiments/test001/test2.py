# -*- coding：utf-8 -*- 
# 
# 作者:OneNut
# 日期:2021年09月29日

from collections import Counter
words = []  # 建立一个空列表
for line in open("C:\\Users\\HP\\Desktop\\test2.txt","r",encoding='UTF-8'):   #设置文件对象
    index = 0  # 遍历所有的字符
    start = 0  # 记录每个单词的开始位置
    while index < len(line[:-1]):  # 当index小于长度
        start = index  # start来记录位置
        while line[:-1][index] != " " and line[:-1][index] not in [".", ","]:  # 若不是空格，点号，逗号
            index += 1  # index加一
            if index == len(line[:-1]):  # 若遍历完成
                break  # 结束
        words.append(line[:-1][start:index])
        if index == len(line[:-1]):# 若遍历完成
            break
        while line[:-1][index] == " " or line[:-1][index] in [".", ","]:
            index += 1
            if index == len(line[:-1]):
                break


print(words)
result = Counter(words)
print(result)
d = sorted(result.items(), key=lambda x: x[1], reverse=True)
print(type(d[0]))
for key in d[0]:
    print(key)

