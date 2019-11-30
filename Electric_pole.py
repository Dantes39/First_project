import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def magnit_pole(q):
    k = 9*10**9
    circle = [0.1,1,3,5,7,9]
    E = np.zeros(5)
    for i in range(5):
        E[i] = k*q/(circle[i])**2
    return E

plt.plot([0],[0])

x = np.arange(-a,a,0.1)
y = np.arange(-a,a,0.1)
X,Y = np.meshgrid(x,y)
fxy = X**2 + Y**2
elpole = ax.contour(X, Y, fxy, levels=circle, colors=((1, 0.1, 0.4), 
                                                      (0.9, 0, 0), 
                                                      (0.8, 0, 0), 
                                                      (0.7, 0, 0), 
                                                      (0.6, 0, 0), 
                                                      (0.5, 0, 0)))


fmt = {}
strs = []
E = magnit_pole(0.0000003)

for i in range(5):
    strs.append('{}, Тл'.format(int(E[i])))
    
for l, s in zip(elpole.levels, strs):
    fmt[l] = s


ax.clabel(elpole, inline=1, fontsize=10, fmt=fmt)

ax.set_title('Lines with colorbar')
ax.clabel(elpole, inline=1, fontsize=10)

plt.plot([0], [0], marker='o', ms=10, color=((1,0.2,0)))
magnit_pole(3)

print(E[0])


plt.axis('equal')
plt.show()

