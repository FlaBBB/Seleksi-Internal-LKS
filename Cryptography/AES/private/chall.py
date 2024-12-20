from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import binascii
import string

def key_gen():
    return ("".join(random.choice(string.digits) for _ in range(4)) * 4).encode()

KEY1, KEY2 = key_gen(), key_gen()
IV = random.randbytes(16)

print(IV.hex())

def encrypt(m):
    msg = pad(m.encode(), AES.block_size)
    cipher1 = AES.new(KEY1, AES.MODE_CBC, iv=IV)
    enc_msg = cipher1.encrypt(msg)
    cipher2 = AES.new(KEY2, AES.MODE_CBC, iv=IV)
    return cipher2.encrypt(enc_msg).hex()

FLAG = encrypt("GRFLKS24{what?_I_th0ugh7_it_wou1d_m4ke_it_more_s3cure_ajs756a2}")

def main():
    print(f"\nFlag      : {FLAG+IV.hex()[:16]}")
    p = binascii.unhexlify(input("Plaintext : ").strip()).decode()
    c = encrypt(p)
    print(f"Result    : {IV.hex()[16:]+c}")

if __name__ == "__main__":
    main()