# 作者:ZhaoYu Wang
# 日期:2021年10月06日
import sympy
from sympy import *
x = Symbol('x')
X=(solve(3395.31*x**6-((3395.31/6+3395.31*0.0057)*(x**6-1)/(x-1))),[x])
ans=X[0]
for i in range(0,len(ans)):
    if isinstance(ans[i],sympy.core.numbers.Float) and ans[i]>1 :
        I=(ans[i]-1)*12
        print(I)

#  11.63%
#  不愿意

