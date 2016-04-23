T = int(raw_input())


# return bool if path found for x * y area
def path_found(x, y):
    if x == 1 or y == 1:
        if x*y == 2:
            return True
        else:
            return False
    if x == 2 or y == 2:
        return True
    if x == 3 or y == 3:
        if (x*y) % 2 == 0:
            return True
        else:
            return False
    if x*y % 2 == 0:
        return True
    else:
        return False

for i in range(0, T, 1):
    line = raw_input()
    line = line.split(" ")
    N = int(line[0])
    M = int(line[1])
    found = path_found(N, M)

    if found:
        print "Yes"
    else:
        print "No"
