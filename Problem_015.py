#Lattice paths
import math

# Print Pascal's Triangle in Java 
from math import factorial 
  
# input n
nums = [] 
n = 21
for i in range(n): 
    for j in range(i+1): 
        if i == 20:
            nums.append(factorial(i)//(factorial(j)*factorial(i-j)))
print(nums) 
tot = 0
for i in nums:
    tot = tot + i**2
print(tot)

# Lee solution
#from math import comb
#
#SIZE = 20
#print(comb(SIZE+SIZE, SIZE))