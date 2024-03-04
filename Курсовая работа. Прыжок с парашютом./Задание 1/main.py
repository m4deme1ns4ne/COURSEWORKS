from matplotlib import pyplot as plt
import numpy as np
# Исходные параметры модели
g = 9.8
m0 = 70
mp = 15
m = m0+mp
r = 0.3
S0 = np.pi*r**2
R = 5
S1 = np.pi*R**2
ro = 1.3
Cx0 = 0.5
Cx1 = 1.28
k0 = Cx0*ro*S0/2
k1 = Cx1*ro*S1/2
H = 1000
tr = 5
v0 = 0
# Расчёт математической (теоретической) модели
T = 500
N = 20000
dt = T/N
y = np.zeros(N)
v = np.zeros(N)
t = np.zeros(N)
y[0] = H
v[0] = v0
t[0] = 0
k = k0
for i in range(N-1):
    if t[i]>=tr:
        k = k1
    y[i+1] = y[i]+v[i]*dt
    v[i+1] = v[i]-(g+k/m*abs(v[i])*v[i])*dt
    if y[i+1]<0:
        break
    t[i+1] = t[i]+dt
# Вывод полученного графика
plt.subplot(3, 1, 1)
plt.title("y = y(t)")
plt.xlabel('t,c', fontsize=14)
plt.ylabel('y,м', fontsize=14)
plt.plot(t[:i], y[:i])
plt.grid()
plt.ylim(0)
plt.subplot(3, 1, 2)
plt.title("v = v(t)")
plt.xlabel('t,c', fontsize=14)
plt.ylabel('v, м/с', fontsize=14)
plt.plot(t[:i], v[:i])
plt.grid()
plt.subplot(3, 1, 3)
plt.title("v = v(y)")
plt.xlabel('y, м', fontsize=14)
plt.ylabel('v, м/с', fontsize=14)
plt.plot(y[:i], v[:i])
plt.grid()
plt.tight_layout()
plt.show()
