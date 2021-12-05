# 作者:ZhaoYu Wang
# 日期:2021年11月16日
flag = True
str = input("输入：")
pos = 0
str+="$"




def judge(ch):
    if ch >= '0' and ch <= '9':
        return 'n'
    elif (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        return 'a'
    else:
        return ch


def error(ch):

    global flag
    global pos
    if flag == True:
        return
    else :
        flag=False
    print("\nerror:",ch,",position",pos,"\n",end='')


def match (kind, ch):
    global pos
    print(kind,":",ch,"\n",end='')
    pos+=1

def atom ():
    global flag,pos
    if not flag:
        return
    ch = judge(str[pos])
    if ch =='n' :
        match('n',str[pos])
    elif ch == 'a':
        match('a',str[pos])
    elif ch == '$':
        print("accept\n",end='')
    else:
        flag=False
        error(ch)

def lexp():
    global flag,pos
    if not flag :
        return
    ch = judge(str[pos])
    if ch =='n' or ch =='a' :
        print(" ",end='')
        atom()
    elif ch == '(':
        print(" ",end='')
        list()
    elif ch == '$':
        print("accept\n",end='')
    else:
        flag = False
        error(ch)

def lexp_seq1():
    global flag,pos
    if not flag :
        return
    ch = judge(str[pos])
    if ch == 'n' or ch =='a' or ch =='(':
        print(" ",end='')
        lexp()
        print(" ",end='')
        lexp_seq1()
    elif ch ==")" :
        match('r',')')
    elif ch == '$':
        print("accept\n",end='')
    else:
        flag = False
        error(ch)

def list():
    global flag,pos
    if not flag:
        return
    match('l','(')
    print(" ",end='')
    lexp_seq1()
    if str[pos]==')':
        match('r',')')
    else:
        flag = False
        error(str[pos])

lexp_seq1()



