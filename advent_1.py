import io
import math

def get_fuel(mass):
    return math.floor(int(mass) / 3) - 2

def get_fuel_rec(mass, total):
    if mass <= 6:
        return total

    cost = get_fuel(mass)
    total += cost
    return get_fuel_rec(cost, total)

def ans_1A():
    total = 0
    f = open("data/1.txt")
    for d in f:
        total += get_fuel(d)
        
    return total

def ans_1B():
    total = 0
    f = open("data/1.txt")
    for d in f:
        total += get_fuel_rec(int(d), 0)
    return total

print(ans_1A())
print(ans_1B())
