# Bài 1: Nhập họ tên học sinh, điểm. In thông tin về học sinh và điểm trung bình
print("Đinh Tiến Cường")
hoten = str(input("Nhập họ tên học sinh: "))
ngaysinh = str(input("Nhập ngày tháng năm sinh: "))
gioitinh = str(input("Nhập giới tính: "))
toan = float(input("Nhập điểm môn Toán: "))
ly = float(input("Nhập điểm môn Vật lý: "))
hoa = float(input("Nhập điểm môn Hóa: "))
anh = float(input("Nhập điểm môn Anh: "))
van = float(input("Nhập điểm môn Văn: "))
avg = (toan + ly + hoa + anh + van) / 5
print("Họ tên học sinh:", hoten)
print("Ngày tháng năm sinh:", ngaysinh)
print("Giới tính:", gioitinh)
print("Điểm trung bình:", avg)
