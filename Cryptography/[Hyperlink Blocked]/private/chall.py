from Crypto.Util.number import getPrime, bytes_to_long
import os

flag = b"GRFLKS24{KRIS!_KRIS!!_KRISSS!!!_TH4TS_A_V3RY_V3RY_N1C3_DE4L!_HAEAHAEAHAEAH}"
flag += os.urandom(130-len(flag))

m = bytes_to_long(flag)
p,q = getPrime(512), getPrime(512)
r, s = p+q, q-p
c = pow(m,19,p*q)

print(f"{r = }")
print(f"{s = }")
print(f"{c = }")