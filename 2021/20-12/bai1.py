# Bài 1: Viết chương trình nhập n số nguyên, tính tổng các số vừa nhập. Tìm min của các số đó.
# Đinh Tiến Cường
print("Đinh Tiến Cường")
n = int(input("Nhập n: "))
sum = 0
a = []
for i in range(1, n + 1, 1):
    if i < n + 1:
        print("Nhập số thứ", i)
        b = int(input())
        sum += b
        a.append(b)
print("Tổng các số vừa nhập:", sum)
a.sort()
min = a[0]
print("Số nhỏ nhất:", min)
