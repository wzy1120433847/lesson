# 作者:ZhaoYu Wang
# 日期:2021年11月17日

import openpyxl

# 获取工作簿文件对象（打开文件）
work_book = openpyxl.load_workbook('data2.xlsx')
work_sheet = work_book.active

week=[]
info=[]
c = 0
sum = 0
for line in work_sheet:
    for i in range(242):
        week.append(line[i].value)
        if c!=0 and i >1 :
            sum+=line[i].value
    t=(line[0].value,line[1].value,sum)
    if c != 0: info.append(t)
    week.clear()
    sum = 0
    c+=1
info.sort(key=lambda x:(x[1],x[2],x[0]),reverse=True)
print(info)