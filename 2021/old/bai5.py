# Bài 5
# Nhập số nguyên n từ bàn phím tới khi gặp số 0 thì dừng. Tính tổng các số vừa nhập
print("Đinh Tiến Cường")
n = int(input("Nhập số: "))
sum = 0 + n
while n != 0:
    n = int(input("Nhập tiếp số: "))
    sum += n
print("Tổng các số vừa nhập:", sum)

