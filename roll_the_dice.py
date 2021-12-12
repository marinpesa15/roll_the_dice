import random

random = random.Random()

n = 100
w1 = 0
w2 = 0
w3 = 0
w4 = 0
w5 = 0
w6 = 0

print("Rolling the dice.../")
for i in range(n):
    num = random.randint(1, 6)
    if num == 1:
        w1 += 1
    elif num == 2:
        w2 += 1
    elif num == 3:
        w3 += 1
    elif num == 4:
        w4 += 1
    elif num == 5:
        w5 += 1
    elif num == 6:
        w6 += 1

print(f"""
w1 = {w1}
w2 = {w2}
w3 = {w3}
w4 = {w4}
w5 = {w5}
w6 = {w6}
""")

