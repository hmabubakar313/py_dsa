from collections import Counter
mylist = [ 2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
print(Counter(mylist))
print(Counter(mylist).items())
print(Counter(mylist).keys())
print(Counter(mylist).values())

for k, v in Counter(mylist).items():
    v +=v

print(sum(Counter(mylist).values()))
   