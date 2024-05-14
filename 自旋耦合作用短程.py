from matplotlib import cm
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
N=100

x=[1]*20+[2]*20+[3]*20+[4]*20+[5]*20
y=1

first_term = 0  # 首项
common_difference = 5  # 公差
number_of_terms = 20  # 项数

# 使用列表推导式创建等差数列
y = [first_term + common_difference * i for i in range(number_of_terms)]*5

#z = -abs(x)**-1*abs(y+x*0.5-N*0.5)**2*0.001 # 画图所要表现出来的主函数

z = [a**-3 * (b+a*0.5-N*0.5)**2*0.001 for a, b in zip(x, y)]

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.view_init(elev=30,azim=60)

surf = ax.scatter(x, y, z, c=z, cmap='coolwarm', linewidth=0, antialiased=False)

ax.set_xlabel('j')
ax.set_ylabel('i')
plt.legend()
plt.show()