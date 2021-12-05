# 作者:ZhaoYu Wang
# 日期:2021年10月27日
str1="123"
str2="abc"
str3="123abc"
str4="123abc()-=/"
# isalnum() 检测字符串是否由字母和数字组成
print("isalnum() 方法检测字符串是否由字母和数字组成")
print(str1,"isalnum()",str1.isalnum())
print(str2,"isalnum()",str2.isalnum())
print(str3,"isalnum()",str3.isalnum())
print(str4,"isalnum()",str4.isalnum())
# isalpha() 方法检测字符串是否只由字母组成
print("isalpha() 方法检测字符串是否只由字母组成")
print(str1,"isalpha()",str1.isalpha())
print(str2,"isalpha()",str2.isalpha())
print(str3,"isalpha()",str3.isalpha())
print(str4,"isalpha()",str4.isalpha())
# isdigit() 方法检测字符串是否只由数字组成
print("isdigit() 方法检测字符串是否只由数字组成")
print(str1,"isdigit()",str1.isdigit())
print(str2,"isdigit()",str2.isdigit())
print(str3,"isdigit()",str3.isdigit())
print(str4,"isdigit()",str4.isdigit())
# isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
print("isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。")
print(str1,"isdecimal()",str1.isdecimal())
print(str2,"isdecimal()",str2.isdecimal())
print(str3,"isdecimal()",str3.isdecimal())
print(str4,"isdecimal()",str4.isdecimal())
s=u"1265"
print(s,"isdecimal()",s.isdecimal())
# isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
print("isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。")
print(str1,"isnumeric()",str1.isnumeric())
print(str2,"isnumeric()",str2.isnumeric())
print(str3,"isnumeric()",str3.isnumeric())
print(str4,"isnumeric()",str4.isnumeric())
s="1265"
print(s,"isdecimal()",s.isdecimal())
# isspace() 方法检测字符串是否只由空白字符组成。
print("isspace() 方法检测字符串是否只由空白字符组成。")
print(str1,"isspace()",str1.isspace())
c1=""
c2="   "
c3="\n"
c4="\t"
print(c1,"isspace()",c1.isspace())
print(c2,"isspace()",c2.isspace())
print("\\n","isspace()",c3.isspace())
print("\\t","isspace()",c4.isspace())
# isupper() 方法检测字符串中所有的字母是否都为大写。。
print("isupper() 方法检测字符串中所有的字母是否都为大写。")
c1 = "aaa"
c2 = "BBB"
c3 = "aaaBBB"
print(c1,"isupper()",c1.isupper())
print(c2,"isupper()",c2.isupper())
print(c3,"isupper()",c3.isupper())
# islower() 方法检测字符串中所有的字母是否都为小写。。
print("islower() 方法检测字符串中所有的字母是否都为小写。")
c1 = "aaa"
c2 = "BBB"
c3 = "aaaBBB"
print(c1,"islower()",c1.islower())
print(c2,"islower()",c2.islower())
print(c3,"islower()",c3.islower())
#  zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
print("zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。")
print(str1.zfill(20))
#  center()  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。
print("center()  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。")
print(str2.center(30,'+'))
print(str2.center(30,'-'))
# ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
print("ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串")
print(str2.ljust(30,'+'))
print(str2.ljust(30,'-'))
# rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
print("rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。")
print(str2.rjust(30,'+'))
print(str2.rjust(30,'-'))
# startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围
print("startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围")
print(str2,"startswith('a')",str2.startswith('a'))
print(str2,"startswith('a',0)",str2.startswith('a',0))
print(str2,"startswith('a',0,3)",str2.startswith('a',0,3))
print(str2,"startswith('a',1)",str2.startswith('a',1))
print(str2,"startswith('a',1,3)",str2.startswith('a',1,3))
# endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。
print("endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数'start'与'end'为检索字符串的开始与结束位置。")
print(str2,"endswith('c')",str2.endswith('c'))
print(str2,"endswith('bc',1)",str2.endswith('bc',1))
print(str2,"endswith('abc',0,3)",str2.endswith('abc',0,3))
print(str2,"endswith('bc',2)",str2.endswith('bc',2))
print(str2,"endswith('abc',1,3)",str2.endswith('abc',1,3))





