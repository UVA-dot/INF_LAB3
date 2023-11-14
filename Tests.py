import itertools
lists = []
for i in itertools.permutations([1, 2, 3, 4, 5]):
    lists.append(i)
lists.sort()
print(lists[92])
var a = 2