import io

dir_map = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def ans_3A():
    f = open("data/3.txt")
    wire_pos = {}
    curr = (0, 0)
    curr_wire = 0
    cross_overs = []
    for wire in f:
        curr_wire += 1
        print ("Processing Wire: " + str(curr_wire))
        curr = (0, 0)
        dirs = wire.split(",")
        for dir in dirs:
            d = dir[0]
            dist = int(dir[1:])
            for i in range(0, int(dist)):
                curr = (curr[0] + dir_map[d][0], curr[1] + dir_map[d][1])
                if curr in wire_pos and wire_pos[curr] != curr_wire:
                    cross_overs.append(curr)
                else:
                    wire_pos[curr] = 1

    print(str(cross_overs))
    return min(cross_overs, key=lambda x: abs(x[0]) + abs(x[1]))

def ans_3B():
    f = open("data/3.txt")
    wire_pos = {}
    curr = (0, 0)
    curr_wire = 0
    cross_overs = []
    for wire in f:
        curr_wire += 1
        curr = (0, 0)
        dirs = wire.split(",")
        total_dist = 1
        for dir in dirs:
            d = dir[0]
            dist = int(dir[1:])
            for i in range(0, int(dist)):
                curr = (curr[0] + dir_map[d][0], curr[1] + dir_map[d][1])
                if curr in wire_pos and wire_pos[curr][0] != curr_wire:
                    cross_overs.append([curr, total_dist + wire_pos[curr][1]])
                else:
                    wire_pos[curr] = [curr_wire, total_dist]
                total_dist += 1
    
    print(str(cross_overs))
    return min(cross_overs, key=lambda x: x[1])

#print(ans_3A())
print(ans_3B())