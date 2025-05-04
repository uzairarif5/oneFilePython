# The Euler phi function is multiplicative 
# (m, n) = 1 implies phi(mn) = phi(m) * phi(n)

from math import gcd 

m = 4
n = 5
mn=m*n

assert(m<n)

counterM = 0
counterN = 0
counterMN = 0
for i in range(1,mn+1):
  print(i,end="")
  if (gcd(i,m) == 1):
    print("|",end="")
    if i<m:
      counterM += 1
  if (gcd(i,n) == 1):
    print("^",end="")
    if i<n:
      counterN += 1
  if (gcd(i,mn) == 1):
    print(".",end="")
    counterMN += 1
  print("\t",end="")
  if(i%m==0):
    print("\n",end="")

print(counterM,counterN,counterMN)