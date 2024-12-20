from pwn import xor

FLAG = open('flag.txt', 'rb').read()

# GRFLKS24{
# LUBANGSAT

open('dist', 'wb').write(xor(FLAG, b"LUBANGSAT"))