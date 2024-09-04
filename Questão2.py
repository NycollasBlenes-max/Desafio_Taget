import random

num = random.randint(0,100)

a, b = 0, 1
while b < num:
    a, b = b, a + b

if b == num or num == 0:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} **não** pertence à sequência de Fibonacci.")