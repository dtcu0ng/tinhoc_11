# Đinh Tiến Cường
# Bài 1: + Nhập số nguyên n, khởi tạo list a, sau đó sinh n số ngẫu nhiên bằng hàm random (rd) từ -300 cho đến 300 rồi đặt chúng vào list a dùng a.append sau đó in ra màn hình list đó.
# + Nhập số nguyên k, khởi tạo biến tính tổng s, sử dụng vòng lặp: từ các phần tử đã random ở trên nếu các phần tử đó chia hết cho k thì tính tổng các số đó.
print("Đinh Tiến Cường")
import random as rd
n = int(input("Nhập n: ")) # nhập số nguyên n
a = [] # khởi tạo list a
for i in range(n): # khởi tạo vòng lặp bằng 
    x = rd.randint(-300,300) # sinh số ngẫu nhiên từ -300 đến 300 
    a.append(x) # thêm số vừa sinh ngẫu nhiên vào list a vừa tạo.
print(a) # in ra màn hình list a.
k = int(input("Nhập số nguyên k: ")) # nhập số nguyên k
s = 0 # khởi tạo biến s
for i in a: 
    if i%k == 0: # nếu i chia hết cho k:
        s += i # tổng (s) = tổng (s) + i
print("Tổng cần tính là: ", s)