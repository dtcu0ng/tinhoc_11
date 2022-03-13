# Bài 3
# Tính giá trị biểu thức
print("Đinh Tiến Cường")
s = 0
n = int(input("Nhập n: "))
for i in range(1, n+1, 1):
    s = s + i / (i + 1)
print("S = ", s)