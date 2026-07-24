# 1.1 Cricket Over Analyser
import array as ar
n = int(input())
runs = ar.array('i',map(int, input().split()))
print(f"{'Total runs' :<20}:{sum(runs)}")
print(f"{ 'Highest over':<20}:{max(runs)}")
print(f"{'Lowest over' : <20}:{min(runs)}")
print(f"{'Average per over' :<20}:{(sum(runs)/n)}")
print(f"{'Madien overs' :<20}:{ runs.count(0)}")
print(f"{'Bytes used' :<20}:{ n * 4}")