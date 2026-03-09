from itertools import combinations

transactions = [
    ['Milk','Bread','Butter'],
    ['Bread','Butter'],
    ['Milk','Bread'],
    ['Milk','Butter'],
]

min_support = 2

items = set(item for t in transactions for item in t)

freq = {}

for i in range(1,3):
    for combo in combinations(items,i):
        count = sum(1 for t in transactions if set(combo).issubset(t))
        if count >= min_support:
            freq[combo]=count

print(freq)
