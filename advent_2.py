import io

def process_opcode(arr, i):
    if i > len(arr) or i < 0 or arr[i] == 99:
        return False

    process = arr[i]
    if process == 1:
        arr[arr[i + 3]] = arr[arr[i + 1]] + arr[arr[i + 2]]
        return True
    elif process == 2:
        arr[arr[i + 3]] = arr[arr[i + 1]] * arr[arr[i + 2]]
        return True
    else:
        return False

def ans_2A():
    f = open("data/2.txt")
    arr = []
    for d in f:
        arr = [int(x) for x in d.split(",")]

    arr[1] = 12
    arr[2] = 2
    i = 0
    keep_running = True
    while keep_running:
        keep_running = process_opcode(arr, i)
        i += 4
    return arr[0]


def ans_2B():
    search = 19690720
    f = open("data/2.txt")
    orig = []
    for d in f:
        orig = [int(x) for x in d.split(",")]

    noun = 0
    verb = 0
    arr = orig[:]
    while arr[0] != search:
        arr = orig[:]
        if noun == 99:
            noun = 0
            verb += 1
        else:
            noun += 1
        arr[1] = noun
        arr[2] = verb
        i = 0
        keep_running = True
        while keep_running:
            keep_running = process_opcode(arr, i)
            i += 4
    return (100 * noun) + verb

print(ans_2B())