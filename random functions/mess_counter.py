from collections import Counter
with open('mess.txt') as f:
    text = f.read()
print(Counter(text))