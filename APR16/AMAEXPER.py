T = int(raw_input())
N = int(raw_input())
output_array = []


class Node:
    def __init__(self, initdata, initname, parent_num):
        self.num = initdata
        self.name = initname
        self.child_num_list = []
        self.parent_num = parent_num
        node_list.append(self)

    def get_num(self):
        return self.num

for i in range(0, T-1, 1):
    line = raw_input()
    line = line.split(" ")
    u = int(line[0])
    v = int(line[1])
    w = int(line[2])


for i in output_array:
    print i
