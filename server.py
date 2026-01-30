#!/usr/local/bin/python
import random
from Crypto.Util.number import isPrime, bytes_to_long
from hashlib import sha256
import os

flag = open('flag.txt', 'rb').read()
flag = flag.replace(b'\n', b'')
assert len(flag) == 36

class RNG:
    def __init__(self, p, g, seed):
        self.p = p
        self.g = g
        random.seed(seed)

    def sample(self):
        return pow(self.g, random.getrandbits(245), self.p)

    def sign(self, message):
        z = bytes_to_long(sha256(message).digest())
        d = bytes_to_long(flag[8:-1])
        k = random.getrandbits(256) + bytes_to_long(os.urandom(16))
        r = bytes_to_long(os.urandom(32))
        s = pow(k, -1, self.p) * (z + d * r)
        return s % self.p, r

print('I am obsessed with RNGs, aint I?')
p = int(input('Enter your prime: '))
assert isPrime(p) and (100 < p.bit_length() < 256)
rng = RNG(p, random.randint(1, p), random.randint(1, p))

while True:
    print('Press 1 to get a sample!')
    print('Or, press 2 to sign your message!')
    opt = int(input('> '))
    if opt == 1:
        sample = rng.sample()
        print('Here you go => ', sample)
    elif opt == 2:
        message = input('> ').encode()
        sign = rng.sign(message)
        print('Your sign is ready => ', sign)
    else:
        break
