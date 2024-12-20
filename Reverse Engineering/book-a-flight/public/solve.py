encoded = open('encoded.txt', 'r').read().strip().split(',')

for i in range(20):
    for l in range(len(encoded)):
        print(chr(int(encoded[l],16) - i), end='')