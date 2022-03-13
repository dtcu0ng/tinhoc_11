# Bài 3: In các dãy số
print("Đinh Tiến Cường")
for i in range(1, 100+1, 1): # in dãy số nguyên từ 1 đến 100
    print(i)
for i in range(2, 100+1, 2): # in dãy số nguyên chẵn từ 1 đến 100
    print(i)
for i in range(1, 100+1, 1): # in dãy số nguyên lẻ từ 1 đến 100
    if i % 2 != 0:
        print(i)