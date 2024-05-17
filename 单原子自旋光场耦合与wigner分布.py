from matplotlib import cm
from qutip import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#args
Nstates=15
tg=30
omegac=2*np.pi
omegaa=2*np.pi


#operators
a = tensor(destroy(Nstates), qeye(2))
sm = tensor(qeye(Nstates), destroy(2))

resultsm=sm.dag()*sm
resulta=a.dag()*a

g_vec = np.linspace(0, 2.0, 101) * 2 * np.pi

psi_list = []
#hamiltonian
H0=H0 = omegac * a.dag() * a + omegaa * sm.dag() * sm
H1 = (a.dag() + a) * (sm + sm.dag())

#output
for g in g_vec:
    H=H0+g*H1
    gnd_energy,gnd_state=H.groundstate()
    psi_list.append(gnd_state)

smexpt=expect(resultsm,psi_list)
aexpt=expect(resulta,psi_list)

#plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

ax.plot(g_vec / (2 * np.pi), aexpt, "r", linewidth=2, label="cavity")
ax.plot(g_vec / (2 * np.pi), smexpt, "b", linewidth=2, label="atom")
ax.set_ylabel("Occupation probability", fontsize=16)
ax.set_xlabel("coupling strength", fontsize=16)
ax.legend(loc=0)

plt.show()


g_idx = np.where([g_vec == 2 * np.pi * g for
                  g in [0.0, 0.5, 1.0, 1.5, 2.0]])[1]
psi_sublist = []
for idx in g_idx:
    psi_sublist.append(psi_list[idx])

xvec = np.linspace(-5, 5, 200)

fig_grid = (2, len(psi_sublist) * 2)
fig = plt.figure(figsize=(3 * len(psi_sublist), 6))

for idx, psi in enumerate(psi_sublist):
    rho_cavity = ptrace(psi, 0)
    W = wigner(rho_cavity, xvec, xvec)
    ax = plt.subplot2grid(fig_grid, (0, 2 * idx), colspan=2)
    ax.contourf(
        xvec,
        xvec,
        W,
        100,
        norm=mpl.colors.Normalize(-0.125, 0.125),
        cmap=plt.get_cmap("RdBu"),
    )
    ax.set_title(r"$g = %.1f$" % (g_vec[g_idx][idx] / (2 * np.pi)),
                 fontsize=16)
    ax.set_xlabel(r"$Re( \alpha )$")
    ax.set_ylabel(r"$Im(\alpha)$");

# plot the cavity occupation probability in the ground state
ax = plt.subplot2grid(fig_grid, (1, 1), colspan=(fig_grid[1] - 2))
ax.plot(g_vec / (2 * np.pi), aexpt, label="Cavity")
ax.plot(g_vec / (2 * np.pi), smexpt, label="Atom excited state")
ax.legend(loc=0)
ax.set_xlabel("coupling strength")
ax.set_ylabel("Occupation probability");
plt.show()
