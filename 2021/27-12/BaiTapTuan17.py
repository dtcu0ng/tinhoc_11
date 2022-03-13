# Bài 1
# Đinh Tiến Cường
n = int(input("Nhận số phần tử của dãy số: "))
a = []
for i in range(1, n+1, 1):
    print("Nhập số phần tử thứ", i)
    ai = int(input())
    a.append(ai)
a.sort()
print("Phần tử nhỏ nhất (min) của dãy số là:", a[0])
a.reverse()
print("Dãy số theo trật tự giảm dần:", a)
s = 0
for i in a:
    if i%5 == 0:
        s += i
print("Tổng cần tính là:", s)