from pwn import *
import binascii
from Crypto.Cipher import DES
from tqdm import tqdm

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def blocks(enc):
    return [enc[i:i+16] for i in range(0, len(enc), 16)]
    
def send(strings):
    io.sendline(strings)
    result = io.recvline().decode().strip()
    print("result: {}\n".format(blocks(result)))
    io.recvuntil(b'?')
    return result

def encrypt(key, msg):
    des_ = DES.new(key, DES.MODE_ECB)
    return des_.encrypt(msg)

def decrypt(key, msg):
    try:
        des_ = DES.new(key, DES.MODE_ECB)
        return des_.decrypt(msg)
    except:
        return False

# connect 
io = remote('mercury.picoctf.net', 3620)

io.recvline()
flag = io.recvline().decode().strip()
print("\ncipher: {}\n".format(blocks(flag)))
io.recvuntil(b'?')

# test
test_plain = 'a' * 7
print('test =', test_plain)
test_cipher = send(binascii.hexlify(test_plain.encode()))

# exploit
def exploit():
    print("Start exploit...\n")
    x1 = {}
    x2 = {}

    for i in tqdm(range(1000000), "Encrypt X1"):
        k = (f"{i:06}" + "  ").encode()
        x = encrypt(k, pad(test_plain))
        x1[x] = k
                     
    for i in tqdm(range(1000000), "Encrypt X2"):
        k = (f"{i:06}" + "  ").encode()
        x = decrypt(k, binascii.unhexlify(test_cipher))
        x2[x] = k

    x1_set = set(x1.keys())
    x2_set = set(x2.keys())

    for enc in x1_set.intersection(x2_set):
        print("\nKEY FOUND!")
        key_1 = x1[enc]
        key_2 = x2[enc]
        print('key 1 =', key_1)
        print('key 2 =', key_2)
        return [key_1, key_2]
                
key_pair = exploit()

x = decrypt(key_pair[1], binascii.unhexlify(flag))
flag = decrypt(key_pair[0], x)

print("\nflag =", flag.decode().strip())