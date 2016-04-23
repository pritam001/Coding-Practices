import itertools
import time
T = int(raw_input())


def hamming_distance(str1, str2):
    output = 0
    for i in range(0, len(str1), 1):
        if str1[i] != str2[i]:
            output += 1
    return output


def good_str(str1):
    for i in range(0, len(str1), 1):
        j = 1
        while (i + 2*j) < len(str1):
            if str1[i] == str1[i + j] == str1[i + 2*j]:
                return False
            j += 1

    return True


def func_str(str1, str2, k):
    output = 0

    for i in range(0, len(str1), 1):
        if str1[i] != str2[i]:
            output += 1
            if output > k:
                return False
        j = 1
        while (i + 2*j) < len(str1):
            if str1[i] == str1[i + j] == str1[i + 2*j]:
                return False
            j += 1

    return True

for i in range(0, T, 1):
    line = raw_input()
    line = line.split(" ")
    A = int(line[0])
    K = int(line[1])
    s = raw_input()

    if A == 3:
        a_found = False
        b_found = False
        c_found = False
        all_found = False
        for i in range(0, len(s), 1):
            if s[i] == 'a':
                a_found = True
            if s[i] == 'b':
                b_found = True
            if s[i] == 'c':
                c_found = True
            if a_found and b_found and c_found:
                all_found = True
                break

        if not all_found and len(s) > 8:
            print 0
            continue

        alpha_list = 'abc'
    elif A == 2:
        if len(s) > 8:
            print 0
            continue
        alpha_list = 'ab'
    else:
        alpha_list = 'a'

    count = 0
    for p in itertools.product(alpha_list, repeat=len(s)):
        temp_str = ''.join(p)
        if func_str(temp_str, s, K):
            count += 1
    print count


