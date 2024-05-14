from matplotlib import cm
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
N=50
c1=0.001
x = np.linspace(0, N, 100)
y = np.linspace(0, N, 100)
x_, y_ = np.meshgrid(x, y, indexing='ij')
z_ = abs(x_-y_)**-0.3 *abs(x_+y_-N)**2*c1 # 画图所要表现出来的主函数


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.view_init(elev=30,azim=60)

surf = ax.plot_surface(x_, y_, z_, cmap=cm.coolwarm, linewidth=0, antialiased=False)

#fig.colorbar(surf, shrink=0.8, aspect=16)
ax.set_xlabel('i')
ax.set_ylabel('j')
ax.set_zlabel('J_ij')
plt.show()
