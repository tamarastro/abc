#!/usr/bin/env python

from matplotlib import rc
from daft import PGM, Node, Plate
rc("font", family="serif", size=10)
rc("text", usetex=True)


pgm = PGM([10.5, 7.5], origin=[0., 0.2], observed_style='inner')

pgm.add_node(Node('G',r"$G$", 3,1))
pgm.add_node(Node('Coords',r"${RA}_i$/${Dec}_i$", 2,2,fixed=True))
pgm.add_node(Node('G_i',r"$g_i$", 3,2))

pgm.add_node(Node('mu',r"$\theta_\mu$", 1,4))
pgm.add_node(Node('HD',r"$\mu_i$", 4,4,fixed=True))
pgm.add_node(Node('theta_T',r"$\theta_T^{Ia}$, $\theta_T^{non-Ia}$", 2,7,scale=1.5,aspect=1.5))
pgm.add_node(Node('theta_Ti',r"$\theta_{Ti}^{Ia}$, $\theta_{Ti}^{non-Ia}$", 2,6,scale=1.5,aspect=1.5))


#pgm.add_node(Node('theta_G',r"$\theta_G$", 2,1))



#pgm.add_node(Node('theta_Gi',r"$\theta_{Gi}$", 3,4))


pgm.add_node(Node('Host',r"$\theta_{gi}$", 2, 3))
pgm.add_node(Node('z',r"$z_i$", 3, 3))


pgm.add_node(Node('Type',r"$T_i$", 2, 5))
pgm.add_node(Node('Luminosity',r"$L_i(t,\lambda)$", 4, 6, scale=1.2,fixed=True))
pgm.add_node(Node('Flux',r"$n_i(t,\lambda)$", 5, 5, scale=1.2,fixed=True,offset=(15,0)))
pgm.add_node(Node('Flux_g',r"$n_{gi}(\lambda)$", 5, 2,fixed=True,offset=(0,-20)))
pgm.add_node(Node('Transmission',r"$\phi(\lambda)$", 7, 7))
pgm.add_node(Node('Counts',r"$\overline{\mathit{ADU}}_i$", 8, 5,scale=1.2,fixed=True,offset=(15,0)))
pgm.add_node(Node('Counts_g',r"$\overline{\mathit{ADU}}_{gi}$", 8, 4,scale=1.2,fixed=True,offset=(10,-25)))
pgm.add_node(Node('Zeropoints',r"${Z}$", 9, 7, observed=True))
pgm.add_node(Node('^Counts',r"${\mathit{ADU}_i}$", 9, 4, observed=True,scale=1.2,aspect=1.2))

pgm.add_node(Node('Spars',r"${T}_{Si}$, ${z}_{Si},{\theta}_{Si}$", 6, 4, scale=1.8,aspect=1.2, observed=True))
#pgm.add_node(Node('^Host',r"${z}_{Hi},{\theta}_{Hi}$", 7, 2, scale=1.5,observed=True))
pgm.add_node(Node('Galaxies',r"${\mathit{GC}}$", 5, 1, fixed=True))

pgm.add_node(Node('Detected',r"Detected", 8, 3, fixed=True,offset=(-10,-20)))
pgm.add_node(Node('^Type',r"Selected", 8, 2, fixed=True,offset=(-10,-20)))

pgm.add_edge("mu","HD")
#pgm.add_edge("^Host","^Type")
pgm.add_edge("^Type","^Counts")

pgm.add_edge("Host","Luminosity")


pgm.add_edge("z","HD")


pgm.add_edge("Coords","G_i")
pgm.add_edge("G_i","Host")

pgm.add_edge("G_i","z")
pgm.add_edge("HD","Flux")
pgm.add_edge("z","Flux")
pgm.add_edge("HD","Flux_g")
pgm.add_edge("z","Flux_g")
#pgm.add_edge("HD","^Host")


pgm.add_edge("Host","Type")

pgm.add_edge("Type","Luminosity")
pgm.add_edge("Luminosity","Flux")
pgm.add_edge("G","G_i")


pgm.add_edge("theta_T","Luminosity")
#pgm.add_edge("theta_G","Flux_g")
pgm.add_edge("Galaxies","G")

pgm.add_edge("theta_Ti","Luminosity")
pgm.add_edge("Host","Flux_g")


pgm.add_edge("Flux","Counts")
pgm.add_edge("Flux_g","Counts_g")

pgm.add_edge("Counts","^Counts")
pgm.add_edge("Counts_g","^Counts")


pgm.add_edge("Transmission","Counts")
pgm.add_edge("Transmission","Counts_g")
pgm.add_edge("Transmission","Zeropoints")

pgm.add_edge("Flux","Spars")

#pgm.add_edge("Galaxies","^Host")

pgm.add_edge("Counts_g","^Counts")


pgm.add_edge("Detected","^Counts")




# pgm.add_edge("Galaxies", "gal_zi")


# Per-Galaxy parameters: third line in the plate


# Observed photometry

# pgm.add_edge("gal_ni","^gal_zi")
# pgm.add_edge("gal_ni","^gal_thetai")
# pgm.add_edge("gal_ni","^gal_ni")


# pgm.add_edge("gal_D","^gal_zi")
# pgm.add_edge("gal_D","^gal_thetai")
# pgm.add_edge("gal_D","^gal_ni")

# pgm.add_edge("^ni","^Type")


# pgm.add_edge("Standard","Z")


#pgm.add_node(Node("t0true", r"$t_0^{\mathrm{true}}$", 7, 1))


# Big Plate: Galaxy
pgm.add_plate(Plate([1.5, 1.5, 8, 5.],
                    label=r"SNe $\i = 1, \cdots, N_{SN}$",
                    shift=-0.1))

# # Big Plate: SNe
# pgm.add_plate(Plate([5.5, 0.5, 4, 6.],
#                     label=r"SNe $i = 1, \cdots, N_{SN}$",
#                     shift=-0.1))


# pgm.add_plate(Plate([2.6, 1.6, 1.8, 3.8],
#                     label=r"Photo-$z$",
#                     shift=-0.1))

# pgm.add_plate(Plate([3.6, 5.6, 2.8, 1.8],
#                     label=r"Host match",
#                     shift=-0.1))

# pgm.add_plate(Plate([5.6, 1.6, 1.8, 3.8],
#                     label=r"LC Fit",
#                     shift=-0.1))

# pgm.add_plate(Plate([5.6, 2.6, 2.8, 0.8],
#                     label=r"Efficiency",
#                     shift=-0.1))


# Render and save.
pgm.render()
# pgm.figure.text(0.2,0.98,r'\underline{UNIVERSE}',size='large')
# pgm.figure.text(0.45,0.98,r'\underline{OBSERVATORY}',size='large')
# pgm.figure.text(0.72,0.98,r'\underline{DATA}',size='large')

pgm.figure.savefig("../results/hdpgm.eps")
