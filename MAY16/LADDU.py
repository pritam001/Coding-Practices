T = int(raw_input())

for i1 in range(0, T, 1):
    l_array = raw_input().split(" ")
    count = 0
    for i in range(0, int(l_array[0]), 1):
        line = raw_input().split(" ")
        if line[0] == "CONTEST_WON":
            bonus = 20 - int(line[1])
            if bonus < 0:
                bonus = 0
            count += 300 + bonus
        elif line[0] == "TOP_CONTRIBUTOR":
            count += 300
        elif line[0] == "BUG_FOUND":
            count += int(line[1])
        elif line[0] == "CONTEST_HOSTED":
            count += 50
    if l_array[1] == "INDIAN":
        print count/200
    else:
        print count/400
