#Bài 1
import math
print=("Trần Lan Anh")
a=float(input("Nhập a"))
b=float(input("Nhập b"))
c=float(input("Nhập c"))
if a != 0 and c != -1:
    s=((7*a*a-6*b) / (c+1)) + 2/a
    print("s=", s)
else:
    print("Phương trình vô nghĩa")