# Bài 1: Ghi dãy số 1 - 100 vào tệp bai1.txt
print(" - 11D0")
with open(r"E:\Bai1.txt", "w") as f:
    for i in range (101):
        f.write(str(i) + " ")