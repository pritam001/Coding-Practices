T = int(raw_input())

for i in range(0, T, 1):
    line = raw_input()
    K = int(raw_input())
    line = line.split(" ")
    R = int(line[0])
    G = int(line[1])
    B = int(line[2])

    count = 0

    minimum = min(R, G, B)

    if K <= minimum:
        count += 3*(K - 1)
        K = 1
    else:
        count += 3*minimum
        R -= minimum
        G -= minimum
        B -= minimum
        K -= minimum

    if R == 0:
        minimum = min(G, B)
        if K <= minimum:
            count += 2*(K - 1)
            K = 1
        else:
            count += minimum + K - 1

    elif G == 0:
        minimum = min(R, B)
        if K <= minimum:
            count += 2*(K - 1)
            K = 1
        else:
            count += minimum + K - 1
    elif B == 0:
        minimum = min(G, R)
        if K <= minimum:
            count += 2*(K - 1)
            K = 1
        else:
            count += minimum + K - 1

    count += 1
    print count
