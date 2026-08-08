'''
BMI 计算
'''
height = float(input("请输入身高(米):"))
weight = float(input("请输入体重(千克):"))
bmi = weight / (height ** 2)
print(f'bmi={bmi:.1f}')
if 18.5 <= bmi < 24:
    print("体重正常")
elif bmi < 18.5:
    print("体重过轻")
else:
    print("体重过重")

'''
分段函数求值
'''
x = float(input("请输入自变量x的值:"))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'y={y:.1f}')

'''
百分制成绩转换为等级制成绩
'''
score = float(input("请输入百分制成绩:"))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(f'等级制成绩为:{grade}')

'''
计算三角形的周长和面积
'''
a = float(input("请输入三角形的第一条边长:"))
b = float(input("请输入三角形的第二条边长:"))
c = float(input("请输入三角形的第三条边长:"))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'三角形的周长为:{perimeter:.1f}')
    print(f'三角形的面积为:{area:.1f}')
else:
    print("输入的边长不能构成三角形")
