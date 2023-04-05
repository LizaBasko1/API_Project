import copy
l = [0, 1, [2, 3]]
l_assign = l

l_copy = l.copy()
l_deepcopy = copy.deepcopy(l)

l[1] = 100
l[2][0] = 200

print(l)
print(l_assign)
print(l_copy)
print(l_deepcopy)
