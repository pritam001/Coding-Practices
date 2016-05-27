line = raw_input().split(" ")
N = int(line[0])
W = int(line[1])
L = int(line[2])
output = 1000000000000000
array = []

for i in range(0, N, 1):
    line = raw_input().split(" ")
    H = int(line[0])
    R = int(line[1])
    array.append((H, R))
    month = 0
    while (H + R*month) < L:
        month += 1
    output = min(output, month)

m_value = output - 1
summation = 0
while summation < W:
    summation = 0
    m_value += 1
    for i in range(0, N, 1):
        if (array[i][0] + array[i][1]*m_value) < L:
            summation += 0
        else:
            summation += (array[i][0] + array[i][1]*m_value)
            # print str(H) + " + " + str(R) + " * " + str(m_value) + " added to " + str(summation)

print m_value
