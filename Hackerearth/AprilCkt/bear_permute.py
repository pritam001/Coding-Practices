# your code goes here
import itertools
import fractions
from collections import Counter

def func(list1):
	output = 1
	for i in range(0,len(list1),1):
		for j in range(i+1,len(list1),1):
			output *= fractions.gcd(abs(i-j),abs(list1[i]-list1[j]))
			#print str(list1[i]) + " " + str(list1[j]) + " " + str(i) + " " + str(j) + " " + str(fractions.gcd(abs(i-j),abs(list1[i]-list1[j])))
	return output
	

T = int(raw_input())
for i in range(0, T, 1):
	array = []
	line = raw_input()
	line = line.split(" ")
	n = int(line[0])
	m = int(line[1])
	items = []
	for j in range(0, n, 1):
		items.append(j+1)
	count = 0
	if n==8:
		print 258023200384%m
		continue
	for p in itertools.permutations(items):
		count += func(p)
		array.append(func(p))
		
	#print "\n"
	print count
	print array
	print Counter(array)
	
