# Đinh Tiến Cường
# Bài 2: Nhập số lượng n phần tử của dãy số, dùng vòng lặp để sinh n số ngẫu nhiên trong khoảng -300 đến 300, đặt chúng vào list a, rồi sau đó sắp xếp các phần tử theo thứ tự từ bé đến lớn.
print("Đinh Tiến Cường")
import random as rd
n = int(input("Nhập số lượng phần tử của dãy số , N = "))
a = []
for i in range(n):
    ai = rd.randint(-300, 300)
    a += [ai]
print("list vừa tạo:")
print(a)
i = n
while(i > 1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            tam = a[j]
            a[j] = a[j+1]
            a[j+1] = tam
    i -= 1
print("Dãy số đã được sắp xếp:")
print(a)
input()