# Đinh Tiến Cường
# Bài 3: Nhập số lượng n phần tử của dãy số, nhập các phần tử vào biến ai bằng vòng lặp, sau đó đặt chúng vào list a, đặt max = a[0], 
# so sánh các giá trị trong list và đưa ra giá trị lớn nhất trong list đó và chỉ số của nó.
print("Đinh Tiến Cường")
n = int(input("Nhập số lượng phần tử của dãy số, N = : "))
a = []
for i in range(n):
     print("Nhập phần tử thứ ", i+1)
     ai = int(input())
     a += [ai]
Max = a[0]
cs = 0
for j in a:
    if j > Max:
        Max = j
        #cs_m = cs
        cs_m=a.index(j)
        print(Max, '  ',cs_m)
    #cs += 1
print("Giá tri lớn nhất của dãy là:", Max)
print("Chỉ số của Max là: ", cs_m)
input()