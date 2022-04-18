print("Đinh Tiến Cường - 11D0")
import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > 0 and b > 0 and c > 0 and a + b > c and b + c > a:
    chuvi = a + b + c
    p = chuvi / 2
    dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
    with open("bai2.txt", "w") as f:
        f.write("a= " + str(a) + "\n")
        f.write("b= " + str(b) + "\n")
        f.write("c= " + str(c) + "\n")
        f.write("Chu vi = " + str(chuvi) + "\n")
        f.write("Dien tich = " + str(dientich) + "\n")
else:
    print("Các cạnh không thỏa mãn điều kiện.")