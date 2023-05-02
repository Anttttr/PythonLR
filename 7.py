count = 0
M = 0
a = 10000000
while count < 5:
    c = 0
    M = 0
    for i in range(a//2, 1, -1):
        if a % i == 0:
            c += 1
            M += i
        if M > 10000:
            break
        if c == 2:
            count += 1
            print(M)
            break
    a += 1
