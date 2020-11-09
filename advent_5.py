
def get_opcode(inst):
    s = str(inst)
    if len(s) == 1:
        return int(s)

    if (len(s) == 2 and s[0] == 0):
        return int(s[1])
    
    return int(s[len(s) - 1:len(s)])

def get_opmodes(s):
    t = str(s)
    if len(t) <= 2:
        return [0]

    ret = []
    for c in t[:2]:
        ret.append(int(c))
    return ret

def get_value(mode, arr, i):
    print("Mode: " + str(mode) + " value " + str(arr[i]))
    if mode == 1:
        return int(arr[i])
    if mode == 0:
        return int(arr[arr[i]])

def process_opcode(arr, i):
    if i > len(arr) or i < 0 or arr[i] == 99:
        return -1

    print("index: " + str(i) + " inst: " + str(arr[i]))
    op_code = get_opcode(arr[i])
    print("opcode " + str(op_code))
    op_mode = get_opmodes(arr[i])
    if len(op_mode) < 2:
        op_mode = op_mode * 2
    print("opmodes " + str(op_mode))
    if op_code == 1:
        arr[arr[i + 3]] = get_value(op_mode[0], arr, i + 1) + get_value(op_mode[1], arr, i + 2)
        return 4
    elif op_code == 2:
        arr[arr[i + 3]] = get_value(op_mode[0], arr, i + 1) * get_value(op_mode[1], arr, i + 2)
        return 4
    elif op_code == 3:
        arr[arr[i + 1]] = input("enter code")
        return 2
    elif op_code == 4:
        print(arr[i + 1])
        return 2
    else:
        return -1


def ans_5A():
    f = open("data/5.txt")
    for d in f:
        arr = [int(x) for x in d.split(",")]

    keep_running = 0
    i = 0
    while keep_running != -1:
        keep_running = process_opcode(arr, i)
        i += keep_running

ans_5A()