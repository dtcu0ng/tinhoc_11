
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

max = a
min = a

if max < b:
    max = b
if max < c:
    max = c
print("Số lớn nhất:", max)

if min > b:
    min = b
if min > c:
    min = c
print("Số nhỏ nhất:", min)