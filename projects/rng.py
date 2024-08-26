import random
print('Random Number Generator')

rngAmountMin = input('Select Minimum Value')
rngAmountMax = input('Select Maximum Value')

rng = random.randint(rngAmountMin, rngAmountMax)

print(rng)