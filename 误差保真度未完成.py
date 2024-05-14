from matplotlib import cm
from qutip import *
import numpy as np
import matplotlib.pyplot as plt


first_term = 0  # 首项
common_difference = 0.005  # 公差
number_of_terms = 20  # 项数

#
meanpho_num = [first_term + common_difference * i for i in range(number_of_terms)]
k=1.1
y = [(a*2+1)*k**2 for a in meanpho_num]

fig = plt.figure(figsize=(5, 4))
ax = fig.add_subplot(1, 1, 1)

line = ax.plot(meanpho_num, y, c='red', linewidth=0.5, antialiased=False,label='wx=wy')
k=1.15
y = [(a*2+1)*k**2 for a in meanpho_num]
line = ax.plot(meanpho_num, y, c='black', linewidth=0.5, antialiased=False,label='wx=wy')

k=1.1
y = [1*k**2 for a in meanpho_num]
dots = ax.scatter(meanpho_num, y, c='red',s=5, linewidth=0, antialiased=False,label='wx=0.75wy')
k=1.15
y = [1*k**2 for a in meanpho_num]
dots = ax.scatter(meanpho_num, y, c='black',s=15, linewidth=0, antialiased=False,label='wx=0.75wy')
ax.set_xlabel('MeanPhononNum')
ax.set_ylabel('Error')
plt.legend()
plt.show()

first_term = 0  # 首项
common_difference = 0.05  # 公差
number_of_terms = 30  # 项数

#
k = [first_term + common_difference * i for i in range(number_of_terms)]
phonon_num=0.25
fig=plt.figure(figsize=(5,4))
ax=fig.add_subplot(1,1,1)
y=[a*phonon_num for a in k]

line=ax.plot(k,y,c='red',linewidth=0.5,label='wx=0.75wy')
ax.set_xlabel('$\eta$^2')
ax.set_ylabel('Error')
plt.legend()
plt.show()