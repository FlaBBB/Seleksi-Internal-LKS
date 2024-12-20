from pwn import xor

flag = open("dist", "rb").read()

prefix = b"LUBANGSAT"
# prefix = b"MPUSSLUMA"
# prefix = b"GRFLKS24{"

for i in range(len(prefix)):
    print(f"Result {i}:")
    print(xor(flag[i:], prefix))

# open('res.txt', 'wb').write(xor(flag, prefix))