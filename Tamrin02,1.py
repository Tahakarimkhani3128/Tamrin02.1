import math

def solve_quadratic(a, b, c):
     discriminant = b**2 - 4*a*c  # محاسبه دلتا

     if discriminant > 0:
          root1 = (-b + math.sqrt(discriminant)) / (2*a)
          root2 = (-b - math.sqrt(discriminant)) / (2*a)
          return f"دو ریشه حقیقی: {root1} و {root2}"
     elif discriminant == 0:
          root = -b / (2*a)
          return f"یک ریشه حقیقی مضاعف: {root}"
     else:
           return "ریشه‌های مختلط هستند و در مجموعه اعداد حقیقی قرار ندارند."



a = float(input("مقدار a: "))
b = float(input("مقدار b: "))
c = float(input("مقدار c: "))

result = solve_quadratic(a, b, c)
print(result)