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



flag = input("Enter the flag: ").strip().encode()

assert(a(c(len(flag), 31, 8), 1))
assert(a(d(c(flag[11], 103, 8), 5, 8), 1))
assert(a(d(b(flag[17], 23, 8), 72, 8), 1))
assert(a(d(b(flag[6], 188, 8), 238, 8), 1))
assert(a(d(b(flag[27], 112, 8), 160, 8), 1))
assert(a(d(c(flag[2], 151, 8), 175, 8), 1))
assert(a(d(c(flag[22], 196, 8), 111, 8), 1))
assert(a(d(c(flag[29], 209, 8), 100, 8), 1))
assert(a(d(b(flag[24], 29, 8), 81, 8), 1))
assert(a(d(c(flag[28], 66, 8), 44, 8), 1))
assert(a(d(c(flag[4], 64, 8), 11, 8), 1))
assert(a(d(b(flag[23], 69, 8), 183, 8), 1))
assert(a(d(b(flag[5], 241, 8), 68, 8), 1))
assert(a(d(c(flag[9], 84, 8), 221, 8), 1))
assert(a(d(b(flag[16], 19, 8), 85, 8), 1))
assert(a(d(c(flag[18], 213, 8), 159, 8), 1))
assert(a(d(b(flag[19], 14, 8), 109, 8), 1))
assert(a(d(b(flag[8], 96, 8), 219, 8), 1))
assert(a(d(c(flag[20], 59, 8), 245, 8), 1))
assert(a(d(c(flag[1], 114, 8), 224, 8), 1))
assert(a(d(c(flag[7], 189, 8), 119, 8), 1))
assert(a(d(c(flag[26], 115, 8), 190, 8), 1))
assert(a(d(b(flag[3], 255, 8), 75, 8), 1))
assert(a(d(c(flag[14], 78, 8), 23, 8), 1))
assert(a(d(b(flag[15], 21, 8), 116, 8), 1))
assert(a(d(c(flag[25], 72, 8), 44, 8), 1))
assert(a(d(b(flag[0], 214, 8), 29, 8), 1))
assert(a(d(b(flag[12], 142, 8), 190, 8), 1))
assert(a(d(b(flag[13], 182, 8), 44, 8), 1))
assert(a(d(b(flag[30], 131, 8), 0, 8), 1))
assert(a(d(b(flag[10], 199, 8), 38, 8), 1))
assert(a(d(b(flag[21], 113, 8), 225, 8), 1))

print("Correct!")