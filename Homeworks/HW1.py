import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_random_prime():
    while True:
        num = random.randint(2, 100) 
        if is_prime(num):
            return num


m1 = [[0 for x in range(3)] for y in range(3)]

for i in range(3):  
    for j in range(3): 
        m1[i][j] = get_random_prime()  


for row in m1:
    print(row)
