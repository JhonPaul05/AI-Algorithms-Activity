import random

population = [random.randint(0,31) for i in range(6)]

def fitness(x):
    return x*x

for generation in range(5):
    population = sorted(population, key=fitness, reverse=True)
    print("Generation:",population)

    parent1,parent2=population[0],population[1]
    child=(parent1+parent2)//2
    population[-1]=child
