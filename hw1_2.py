import numpy as np
import matplotlib.pyplot as plt
 
n = 1000
m = 1000
 
plt.figure(figsize=(15, 4))
 
s = np.random.choice([-1, 1], size=n)
x = np.zeros(n)
curr = 0
for i in range(n):
    curr += s[i]
    x[i] = curr
 
plt.subplot(1, 3, 1)
plt.plot(x)
plt.xlabel('N')
plt.ylabel('x')
plt.title('Траектория x(N)')
plt.grid()
 
p = np.random.choice([-1, 1], size=(m, n))
w = np.zeros((m, n))
 
for i in range(m):
    curr = 0
    for j in range(n):
        curr += p[i, j]
        w[i, j] = curr
 
f = w[:, -1]
 
plt.subplot(1, 3, 2)
plt.hist(f, bins=30)
plt.xlabel('x')
plt.ylabel('Count')
plt.title('Гистограмма (N=1000)')
plt.grid()
 
r = np.sqrt(np.mean(w**2, axis=0))
t = np.arange(1, n + 1)
 
plt.subplot(1, 3, 3)
plt.plot(t, r)
plt.plot(t, np.sqrt(t))
plt.xlabel('N')
plt.ylabel('RMSD')
plt.title('RMSD от N')
plt.grid()
 
plt.tight_layout()
plt.show()