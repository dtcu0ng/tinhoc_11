print("Lê Gia Bảo- 11D0") 
n = int(input("Nhập số lượng phần tử của dãy số, N = : "))
a = []
for i in range(n): 
    print("Nhập phần tử thứ ", i+1)
    ai = int(input())
    a += [ai]

Min = a[0]
cs = 0
for j in a: 
    if j < Min: 
        Min = j
        cs_m = a.index(j)
        print(Min, " ",cs_m)
print("Giá trị nhỏ nhất của dãy là:", Min)
input()
i = n 
while (i > 1):
    for j in range(n-1):
        if a[j] < a[j+1]:
            tam = a[j]
            a[j] = a[j+1]
            a[j+1] = tam
    i -= 1
print("Dãy số đã được sắp xếp:")
print(a)
input()
s = 0 
for i in a: 
    if i%5 == 0:
        s += i
print("Tổng cần tính là: ",s)