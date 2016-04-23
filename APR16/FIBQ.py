import itertools
import math

line = raw_input()
line = line.split()
N = int(line[0])
M = int(line[1])
line = raw_input()
A = line.split()
for j in range(0, len(A), 1):
    A[j] = int(A[j])

output_array = []


def func(list1):
    output = 0
    for L in range(1, len(list1)+1):
        for subset in itertools.combinations(list1, L):
            output += fib(sum(list(subset)))
    output_array.append(output % 1000000007)
    return 1


def opt_mul(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    if y == 2:
        return x*x % 1000000007
    if y == 3:
        return x*x*x % 1000000007
    if y % 2 == 0:
        return 2*opt_mul(x, y/2) % 1000000007
    else:
        return 2*opt_mul(x, y/2)*x % 1000000007


def func2(list1):
    _phi = (5.**0.5 + 1.)/2.
    _phi2 = (5.**0.5 - 1.)/2.
    A = lambda n: opt_mul(_phi, n)
    B = lambda n: pow(-1, n) * opt_mul(_phi2, n)
    prod = lambda it: reduce(lambda x, y: x*y, it)
    subset_sum = lambda s: (prod(A(n)+1 for n in s) - prod(B(n)+1 for n in s))/5**0.5
    output_array.append(int(subset_sum(list1)) % 1000000007)
    return 1


def fib(x):
    if x == 0 or x == 1:
        return 1
    elif x % 2 == 0:
        return (fib(x/2) * fib(x/2) + fib(x/2 - 1) * fib(x/2 - 1)) % 1000000007
    else:
        return (fib(x/2) * fib(x/2 + 1) + fib(x/2 - 1) * fib(x/2)) % 1000000007

for i in range(0, M, 1):
    line = raw_input()
    line = line.split()
    if line[0] == 'C':
        X = int(line[1])
        Y = int(line[2])
        A[X - 1] = Y
    if line[0] == 'Q':
        L = int(line[1])
        R = int(line[2])
        func2(A[(L-1):R])

for item in output_array:
    print(item)
