T = int(raw_input())

for i in range(0, T, 1):
    N = int(raw_input())
    string = raw_input()
    count_R = 0
    count_G = 0
    count_B = 0
    for char in string:
        if char == "R":
            count_R += 1
        if char == "G":
            count_G += 1
        if char == "B":
            count_B += 1

    print count_R + count_G + count_B - max(count_R, count_G, count_B)
