def a(x, y):
    r = 0
    for _ in range(y):
        r |= ((x >> _) & 1 ^ 1) << _
    return r

def b(x, y, z):
    while y:
        x, y = x ^ y, (x & y) << 1
    return x & ((1 << z) - 1)

def c(x, y, z):
    while y:
        x, y = x ^ y, (a(x, z) & y) << 1
    return x & ((1 << z) - 1)

def d(x, y, z):
    r = x ^ y
    for _ in range(z):
        r |= (r >> _) & 1
    return r & 1

<%!
    import random
    flag = b"GRFLKS24{1_l0ve_B1t_0p3r4t10n5}"
    operations = [["b", "c"][random.randint(0, 1)] for _ in range(len(flag))]
    order = list(range(len(flag)))
    random.shuffle(order)
    shuffled_flag = [flag[order[i]] for i in range(len(order))]
    operands = []
    ct = []
    for i in range(len(flag)):
        operands.append(random.randint(0, 255))
        if operations[i] == "b":
            ct.append((shuffled_flag[i] + operands[i]) % 256)
        elif operations[i] == "c":
            ct.append((shuffled_flag[i] - operands[i]) % 256)
%>

flag = input("Enter the flag: ").strip().encode()

assert(a(c(len(flag), ${len(flag)}, 8), 1))
%for i in range(len(flag)):
assert(a(d(${operations[i]}(flag[${order[i]}], ${operands[i]}, 8), ${ct[i]}, 8), 1))
%endfor

print("Correct!")