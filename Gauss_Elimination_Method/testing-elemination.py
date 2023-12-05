import numpy as np
import sys

n = int(input("enter numenr of unknown: "))
a = np.zeros((n, n+1))
x = np.zeros(n)


print("print matrix ")
for i in range(n):
    for j in range(n+1):
        a[i][j] = input("a["+str(i)+"]["+str(j)+"]== ")

for i in range(n):
    for j in range(i+1, n):
        ratio = a[i][i] / a[j][i]
        for k in range(n+1):
            a[j][k] = a[j][k] * ratio - a[i][k]

x[n-1] = a[n-1][n] / a[n-1][n-1]
for i in range(n-2, -1, -1):
    x[i] = a[i][n]
    for j in range(i+1, n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i] / a[i][i]

print(end="\n")
for i in range(n):
    print(x[i] , end="  ")
