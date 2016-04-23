import math
T = int(raw_input())


def pow_opt(x, y):
    output = 0
    if y == 0:
        return 1
    if y == 1:
        return x % 1000000007
    if y == 2:
        return x*x % 1000000007
    if y == 3:
        return x*x*x % 1000000007
    if y == 4:
        return x*x*x*x % 1000000007
    if y:
        temp = pow(x, int(math.floor(y/4)))
        output = temp % 1000000007
        if y % 4 == 0:
            output = (output * output * output * output) % 1000000007
        elif y % 4 == 1:
            output = (output * output * output * output * x) % 1000000007
        elif y % 4 == 2:
            output = (output * output * output * output * x * x) % 1000000007
        elif y % 4 == 3:
            output = (output * output * output * output * x * x * x) % 1000000007
    return output

for i in range(0, T, 1):
    line = raw_input()
    line = line.split(" ")
    N = int(line[0])
    K = int(line[1])
    if K == 1:
        print 0
        continue

    count = 0
    temp = bin(N - 1).split("0b")[1]
    y = K - 1
    output = K
    for i in reversed(temp):
        if int(i) % 2 != 0:
            output = (output * y) % 1000000007
        count += 1
        y = (y * y) % 1000000007
    print output
