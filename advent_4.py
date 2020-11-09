
def valid_passwords(low, high):
    valid_count = 0
    for i in range(low, high):
        s = str(i)
        p = s[0]
        double = set()
        double.add(p)
        found_double = False
        increasing = True
        for c in s[1:]:
            if int(c) < int(p):
                increasing = False
                break
            p = c
            if c in double:
                found_double = True
            else:
                double.add(c)
        
        if found_double and increasing:
            valid_count += 1

    return valid_count

def more_valid_passwords(low, high):
    valid_count = 0
    for i in range(low, high):
        s = str(i)
        p = s[0]
        doubles = {}
        doubles[p] = 1
        found_double = False
        increasing = True
        for c in s[1:]:
            if int(c) < int(p):
                increasing = False
                break
            p = c
            if c in doubles:
                doubles[c] += 1
            else:
                doubles[c] = 1
        
        for double in doubles:
            if doubles[double] == 2:
                found_double = True
        
        if found_double and increasing:
            valid_count += 1

    return valid_count

print(more_valid_passwords(246515, 739105))