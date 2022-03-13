# Bài 1: Nhập thông tin học sinh, tính điểm trung bình 3 môn
print("Đinh Tiến Cường")
a = int(input("Nhập số báo danh: "))
b = str(input("Nhập họ và tên: "))
c = float(input("Nhập điểm thi môn toán: "))
d = float(input("Nhập điểm thi môn lý: "))
e = float(input("Nhập điểm thi môn hóa: "))
dtb = (toan + ly + hoa) / 3
if dtb >= 6.5:
    xeploai = "Đạt"
else:
    xeploai = "Không đạt"
print("Số báo danh:", a, "Họ tên:", b, "Điểm trung bình:", dtb, "Xếp loại:", xeploai)