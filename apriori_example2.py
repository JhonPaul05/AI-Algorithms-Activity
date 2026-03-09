transactions = [
['Laptop','Mouse','Keyboard'],
['Laptop','Mouse'],
['Mouse','Keyboard'],
['Laptop','Keyboard']
]

min_support=2

from collections import Counter

count=Counter()

for t in transactions:
    for item in t:
        count[item]+=1

print(count)
