# Bài 4: Nhập họ tên học sinh, lớp, năm sinh. Kiểm tra tuổi học sinh và lớp của học sinh đó
print("Đinh Tiến Cường")
hoten = str(input("Nhập họ và tên: "))
lop = str(input("Nhập lớp: "))
namsinh = int(input("Nhập năm sinh: "))
if lop == "11D0":
    print("Học sinh thuộc lớp 11D0")
else:
    print("Học sinh không thuộc lớp 11D0")
if 2021 - namsinh > 16:
    print("Học sinh trên 16 tuổi")
else:
    print("Học sinh không trên 16 tuổi")
