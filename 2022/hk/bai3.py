print("Đinh Tiến Cường - 11D0")
a = str(input("Nhập xâu a: "))
b = str(input("Nhập xâu b: "))
if len(a) > len(b):
    print("Xâu a dài hơn xâu b")
elif len(b) < len(a):
    print("Xâu b dài hơn xâu a")
else:
    print("Hai xâu bằng nhau")
t = len(a + b)
print("Độ dài hai xâu: " + str(t))
q = (a + b)
print("Xâu ghép a + b: " + q)
