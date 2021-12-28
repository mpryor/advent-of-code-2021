
def input(a):
    def closure():
        registers[a] = inputs.pop(0)
    return closure

def load_reg(b):
    if b in registers.keys():
        return registers[b]
    return b

def add(a, b):
    def closure():
        registers[a] = registers[a] + int(load_reg(b))
    return closure

def mul(a, b):
    def closure():
        registers[a] = registers[a] * int(load_reg(b))
    return closure

def div(a, b):
    def closure():
        registers[a] = registers[a] // int(load_reg(b))
    return closure

def mod(a, b):
    def closure():
        registers[a] = registers[a] % int(load_reg(b))
    return closure

def eql(a, b):
    def closure():
        registers[a] = 1 if registers[a] == int(load_reg(b)) else  0
    return closure

curr_num = 99999999999999

code = open("monad").readlines()
program = []
for line in code:
    parts = line.split()
    if len(parts) == 2:
        ins, a = parts
        program.append(input(a))
    else:
        ins, a, b = parts
        fnc = None
        if ins == "add":
            fnc = add(a, b)
        if ins == "mul":
            fnc = mul(a, b)
        if ins == "div":
            fnc = div(a, b)
        if ins == "mod":
            fnc = mod(a, b)
        if ins == "eql": 
            fnc = eql(a, b)
        program.append(fnc)

while True:
    registers = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    inputs = [int(c) for c in str(curr_num)]
    for fnc in program:
        fnc()

    if registers['z'] == 0:
        break
    else:
        curr_num -= 1

    print(curr_num)

print(curr_num)