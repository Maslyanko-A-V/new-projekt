print("Введите начальную точ")
x1 = float(input('A: '))
y1 = float(input('B: '))
print("\nВведите конечную точ")
x2 = float(input('A: '))
y2 = float(input('B: '))

print("Уравнение прямой, проходящей через эти точки:")
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff == 0:
    print("X = ", x1)
elif y_diff == 0:
    print("Y = ", y1)
else:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("Y = ", k, " * X + ", b)
