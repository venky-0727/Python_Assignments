#Predict, Then Run
def mystery(a, b=[], *c, **d):
    b.append(a)
    return a, b, c, d

print(mystery(1)) #1, [1], (), {}
print(mystery(2, [9])) # 2, [1,9,2], (), {}
print(mystery(3)) # 3, [1,9,2,3], (), {}
print(mystery(4, [7], 8, 9, x=10)) # 4, [1,9,2,3,7,4], (8,9), {'x': 10}

# When we pass a list, a new list is used for that function call.
# When we don't pass a list, It uses the same default list,
# so previous values are still there.