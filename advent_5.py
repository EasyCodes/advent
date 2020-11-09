

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