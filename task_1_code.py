import matplotlib.pyplot as plt
import numpy as np
import os
import json

def f(x,A):
    return -1 * np.sin(x) * np.sin ((x**2)/(np.pi))**2*A
#параметры
A=10
x= np.linspace(0, np.pi, 100)

#расчёт
y = f(x, A)
data = [{"x": x, "y": y} for x, y in zip(x, y)]

#cоздание директории
if not os.path.exists('results'):
    os.makedirs('results')

#сохранение в JSON
with open('results/function.json', 'w') as file:
    json.dump({"data": data}, file)

#построение графика функции
plt.plot(x, y)
#названи графика
plt.title('Задание №1')
#ось x
plt.xlabel('x')
#ось y
plt.ylabel('y')
#plt.xscale('symlog')
#сетка
plt.grid()
#показ графика
plt.show()
