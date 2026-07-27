# Merge Two sorted arrays 
import array as ar
a = ar.array('i', map(int, input().split()))
b = ar.array('i',map(int, input().split()))
i=0
j=0 
merged_array = []
while i<len(a) and j < len(b):
    if a[i] <= b[j]:
        merged_array.append(a[i])
        i +=1
    # print(merged_array)
    else :
        merged_array.append(b[j])
        j +=1
    # print(merged_array)
    
while i < len(a):
    merged_array.append(a[i])
    i += 1
# print(merged_array)

while j < len(b):
    merged_array.append(b[j])
    j += 1
print(merged_array)