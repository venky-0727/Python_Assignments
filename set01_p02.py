# array surgery
import array as a 
n = 6
arr = a.array('i', map(int, input().split()))
print(arr) # 10 20 30 40 50
arr.append(60)# 10 20 30 40 50 60
print(f"{'After append' :<14}: {arr}")
arr.insert(1,15) # 1 indicates index and 15 is the value
print(f"{'After insert' :<14}: {arr}")
arr.remove(30) # val 30 will be removed ([10 15 20 40 50 60])
print(f"{'After remove' :<14}: {arr}")
arr.pop(0)# here 0 is the index value ([15 20 40 50 60])
print(f"{'After pop' :<14}: {arr}")
arr.reverse() # ([60 50 40 20 15])
print(f"{'After reverse' :<14}: {arr}")
