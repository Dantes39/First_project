import matplotlib.pyplot as plt
import numpy as np

#ввод заряда
E = magnit_pole(0.0000003)

#ввод максимального расстояния от точки заряда,которое делиться на 5 часть
R = 20 

edge = 5

fig, ax = plt.subplots()

def magnit_pole(q):
    """ Функция определяет напряженности электрического поля,
        создаваемого зарядом q.
        На вход функции подается заряд и расстояние R на котором 
        определятся напряженность
    """
    k = 9*10**9 #кулоновская постоянная
    circles_number = 5 #количество радиусов
    
    circle = np.linspace(1, R, circles_number) 
    E = np.zeros(circles_number)
    for i in range(circles_number):
        E[i] = k*q/(circle[i])**2
    return E


#Грнаица области заряда
x = np.arange(-edge, edge, 0.1)
y = np.arange(-edge, edge, 0.1)

#Параметрическое задание окружности
X,Y = np.meshgrid(x,y) 
fxy = X**2 + Y**2

circle = np.linspace(1, R, 5) 

elpole = ax.contour(X, Y, fxy, levels=circle, 
                    colors=((1, 0.1, 0.4), 
                            (0.9, 0, 0),
                            (0.8, 0, 0),
                            (0.7, 0, 0),
                            (0.6, 0, 0),
                            (0.5, 0, 0)))



#Построение графика
fmt = {}
strs = []


print(E)
#Вывод показаний на окружности
for i in range(5):
    strs.append('{}, Тл'.format(int(E[i])))
    
for l, s in zip(elpole.levels, strs):
    fmt[l] = s


ax.clabel(elpole, inline=1, fontsize=10, fmt=fmt)

ax.set_title('Электрическое поле')
ax.clabel(elpole, inline=1, fontsize=10)

plt.plot([0], [0], marker='o', ms=10, color=((1,0.2,0))) #точка заряда
plt.xlim(-edge, edge)
plt.ylim(-edge, edge)

plt.axis('equal')

plt.show() #вызываем график
