# -*- coding：utf-8 -*- 
# 
# 作者:OneNut
# 日期:2021年09月29日


with open('C:\\Users\\HP\\Desktop\\result.txt', 'a+') as f:
    f.seek(0)
    f.truncate()  # 清空文件
    for line in open("C:\\Users\\HP\\Desktop\\test1.txt","r",encoding='UTF-8'):   #设置文件对象
        len1=len(line[:-1])
        len2=len(set(line[:-1]))
        if len1-len2<4 :
            f.write(line[:-1])
            f.write("\n")



