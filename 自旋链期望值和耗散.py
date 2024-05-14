from matplotlib import cm
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
#args
Nstates=5
tg=30

h_coeff=1
j_coeff=1

#operators
state_list=[basis(2,1)]+[basis(2,0)]*(Nstates-1)
psi0=tensor(state_list)
t=np.linspace(0,tg,100)
h=np.ones(Nstates)*h_coeff
jx=np.ones(Nstates)*j_coeff
jy=np.ones(Nstates)*j_coeff
jz=np.ones(Nstates)*j_coeff

sx_list,sy_list,sz_list=[],[],[]
for i in range(Nstates):
    op_list=[qeye(2)]*Nstates
    op_list[i]=sigmax()
    sx_list.append(tensor(op_list))

    op_list[i]=sigmay()
    sy_list.append(tensor(op_list))

    op_list[i] = sigmaz()
    sz_list.append(tensor(op_list))

#hamiltonian
H=0
for i in range(Nstates):
    H+=-0.5*h[i]*sz_list[i]

for n in range(Nstates-1):
    H+=-0.5*jx[n]*sx_list[n]*sx_list[n+1]
    H+=-0.5*jy[n]*sy_list[n]*sy_list[n+1]
    H+=-0.5*jz[n]*sz_list[n]*sz_list[n+1]

#output
output=mesolve(H,psi0,t,[],[])

states=[s*s.dag() for s in output.states]
exp_sz=np.array(expect(states,sz_list))

#plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)


plt.plot(t, exp_sz[:, 0], label=r"$\langle \sigma_z^{0} \rangle$")
plt.plot(t, exp_sz[:, -1], label=r"$\langle \sigma_z^{-1} \rangle$")
plt.legend(loc="lower right")
plt.xlabel("t"), plt.ylabel(r"$\langle \sigma_z \rangle$")
plt.title("Dynamics of spin chain");

plt.show()


#args
gamma = 0.02 * np.ones(Nstates)

#operator
c_ops = [np.sqrt(gamma[i]) * sz_list[i] for i in range(Nstates)]

#hamiltonian

#output
result = output= mesolve(H, psi0, t, c_ops, [])
exp_sz_dephase = expect(sz_list, result.states)

#plot
plt.plot(t, exp_sz_dephase[0], label=r"$\langle \sigma_z^{0} \rangle$")
plt.plot(t, exp_sz_dephase[-1], label=r"$\langle \sigma_z^{-1} \rangle$")
plt.legend()
plt.xlabel("Time"), plt.ylabel(r"$\langle \sigma_z \rangle$")
plt.title("Dynamics of spin chain with qubit dephasing")
plt.show()