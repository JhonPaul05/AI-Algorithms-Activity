import random

population=[random.randint(0,10) for i in range(5)]

for i in range(5):
    population=sorted(population)
    population[-1]=random.randint(0,10)
    print(population)
