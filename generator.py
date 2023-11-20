import random, string

chars = string.ascii_letters + string.digits + "!@#$%&*()-_/?\|;:~'`^[]}{=+"

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(8)))