from Crypto.Util.number import getPrime, bytes_to_long
import os

KROMER = b"[Hyperlink Blocked]"
KROMER += os.urandom(0x82-len(KROMER))

HEAVEN = bytes_to_long(KROMER)
AWESOME,PRICE = getPrime(0x200), getPrime(0x200)
BIG,SHOT = AWESOME+PRICE, PRICE-AWESOME
FREEDOM = pow(HEAVEN,0x13,AWESOME*PRICE)

print(f"{BIG = }")
print(f"{SHOT = }")
print(f"{FREEDOM = }")