# Bài 2
# Tính giá trị biểu thức
print("Đinh Tiến Cường")
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
if x**2 + y**2 <= 1:
     z = x**2 + y**2
     print("z =", z)
elif x**2 + y**2 > 1 and y >= x:
     z = x + y
     print("z =", z)
elif x**2 + y**2 > 1 and y < x:
     print("z = 0,5")