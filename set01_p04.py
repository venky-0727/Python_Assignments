#Left Rotate by k 
import array as arr 
a = arr.array('i', map(int, input().split()))
k = int(input())
k = k % len(a)
a1 = a[k:]
a1.reverse()
result = a1 + a[:k]
print(result)


