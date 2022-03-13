# Bài 2: Tính diện tích hình thang
print("Đinh Tiến Cường")
h = float(input("Nhập chiều cao của hình thang (h): "))
a = float(input("Nhập độ dài cạnh đáy 1 (a): "))
b = float(input("Nhập độ dài cạnh đáy 2 (b): "))
if h > 0 and a > 0 and b > 0:
    s = h * ((a + b) / 2)
    print("Diện tích hình thang S =", s)
else:
    print("h, a, b phải là số nguyên dương (>0)")