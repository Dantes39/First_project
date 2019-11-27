import matplotlib.pyplot as plt
import numpy as np

def magnit_pole(q,r):
              ***Функция закона Кулона***
    k = 9*10**9
    E = k*q/r**2
    return E
            

def ell_circl_plotter():
             ***Функция, рисующая график электрическкого поля
                В константу a подставлять значение, равное размеру окружности, который буде нужен***
    fig, ax = plt.subplots()
    a = 4
    x = np.arange(-a,a,0.01)
    y = np.arange(-a,a,0.01)
    X,Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    elpole = ax.contour(X,Y,fxy, levels = [1,2,5,7,9])
    manual_locations = [(1,4),(1,8),(3,6)]
    ax.clabel(elpole, inline=1, fontsize=10, manual=manual_locations)
    E = magnit_pole(10,1)
    plt.plot(1,1, color='y',label='{}'.format(E))
    plt.legend()
    
    plt.axis('equal')
    plt.show()
    plt.savefig('gfhj')
    
magnit_pole(3)
ell_circl_plotter()
    
