'''
算数运算符
1.加法运算符：+
2.减法运算符：-
3.乘法运算符：*
4.除法运算符：/
5.取余运算符：%
6.取整运算符：//
7.指数运算符：**
'''
print("算数运算符")
print(321+12)   # 加法运算符 输出333
print(321-12)   # 减法运算符 输出309
print(321*12)   # 乘法运算符 输出3852
print(321/12)   # 除法运算符 输出26.75
print(321//12)  # 取整运算符 输出26
print(321%12)   # 取余运算符 输出9
print(321**12)  # 指数运算符 输出1196906950228928915420617322241

'''
运算符优先级
先算乘除，后算加减
'''
print("运算符优先级")
print(2+3*5)         # 输出17
print((2+3)*5)       # 输出25
print((2+3)*5**2)    # 输出125
print(((2+3)*5)**2)  # 输出625

'''
赋值运算符
1.赋值运算符：=
2.加法赋值运算符：+=
3.减法赋值运算符：-=
4.乘法赋值运算符：*=
5.除法赋值运算符：/=
6.取余赋值运算符：%=
7.取整赋值运算符：//=
8.指数赋值运算符：**=
'''
print("赋值运算符")
a = 10
b = 3
a += b  # 等价于 a = a + b
print(a)  # 输出13
a*=a + b  # 等价于 a = a * (a + b)
print(a)  # 输出208

'''
比较运算符和逻辑运算符
1.比较运算符：

    ==  等于
    !=  不等于
    >   大于
    <   小于
    >=  大于等于
    <=  小于等于
2.逻辑运算符：

    and  与
    or   或
    not  非
'''
print("比较运算符和逻辑运算符")
flag0 = 1==1             # 输出True
flag1 = 3>2              # 输出True
flag2 = 2<1              # 输出False
flag3 =flag1 and flag2   # 输出False
flag4 = flag1 or flag2   # 输出True
flag5 = not flag0        # 输出False
print('flag0:',flag0)
print('flag1:',flag1)
print('flag2:',flag2)
print('flag3:',flag3)
print('flag4:',flag4)
print('flag5:',flag5)
print(flag1 and not flag2)  # 输出False
print(1>2 or 2==3)          # 输出False

'''
运算符和表达式应用举例
'''
print("华氏温度转摄氏温度")
f =(float(input("请输入华氏温度:")))  # 输入华氏温度
c = (f-32)/1.8  # 华氏温度转摄氏温度公式
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')  # 输出摄氏温度

'''
计算圆的周长和面积
'''
print("计算圆的周长和面积")
import math
r = float(input("请输入圆的半径:"))  # 输入圆的半径
c = 2*math.pi*r  # 圆的周长公式
s = math.pi*r**2  # 圆的面积公式
print(f'圆的周长:{c:.1f}')
print(f'圆的面积:{s:.1f}')

'''
判断闰年
'''
print("判断闰年")
year = int(input("请输入年份："))  # 输入年份
if (year%4==0 and year%100!=0) or (year%400==0):  # 判断是否为闰年
    print(f'{year}是闰年')
else:
    print(f'{year}不是闰年')
