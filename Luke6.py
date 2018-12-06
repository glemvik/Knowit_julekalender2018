limit = 18163106 + 1
nulltungetall = 0

for number in range(1, limit):
    zeroes = str(number).count('0')
    others = len(str(number)) - zeroes

    if zeroes > others:
        nulltungetall += number

print(nulltungetall)
