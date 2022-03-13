# Bài 2: Nhập thông tin học sinh gồm họ tên, ngày sinh
# địa chỉ, lớp, điểm TB học kỳ 1 (lưu ý nhập tiếng việt không dấu)
# Mỗi thông tin trên 1 dòng
print(" - 11D0")
hoten = input("Nhập họ tên: ")
ngaysinh = input("Nhập ngày sinh: ")
diachi = input("Nhập địa chỉ: ")
lop = input("Nhập lớp: ")
diemtb = float(input("Nhập điểm trung bình: "))
with open(r"E:\ThongTin.txt","w") as f:
    f.write(hoten + "\n")
    f.write(ngaysinh + "\n")
    f.write(diachi + "\n")
    f.write(lop + "\n")
    f.write(str(diemtb) + "\n")