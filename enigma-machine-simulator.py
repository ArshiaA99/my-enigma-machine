import random

alphabet = 'abcdefghijklmnopqrstuvwxyz ' # I included space in the alphabet, because I liked it more this way

# Rotors
r1 = list(alphabet)
random.seed(42)
random.shuffle(r1)
r1 = ''.join(r1)

r2 = list(alphabet)
random.seed(43)
random.shuffle(r2)
r2 = ''.join(r2)

r3 = list(alphabet)
random.seed(44)
random.shuffle(r3)
r3 = ''.join(r3)

# Reflector
def reflector(c):
    c = c.lower()
    x = alphabet[len(alphabet)-alphabet.find(c)-1]
    return x

# How enigma machine works:
def enigma_one_char(c):
    c = c.lower()
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    reflected = reflector(c3)
    c3 = alphabet[r3.find(reflected)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]
    return c1

def rotate_rotors():
    global r1, r2, r3
    r1 = r1[1:] + r1[0]
    if state % 27:
        r2 = r2[1:] + r2[0]
    if state % (27*27):
        r3 = r3[1:] + r3[0]


plain = 'Hello my name is Arshia If you decode this message I would be surprised'
cypher = ''
state = 0

for c in plain:
    state += 1
    cypher += enigma_one_char(c)
    rotate_rotors()

print(cypher)
