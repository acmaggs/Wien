# Non-monotonic conductivity of aqueous electrolytes: beyond the first Wien effect
### Hélène Berthoumieux, Vincent Démery, A. C. Maggs
arXiv preprint [arXiv:2405.05882](https://arxiv.org/abs/2405.05882)

## Abstract 
The conductivity of strong electrolytes increases under high electric fields, a nonlinear response known as the first Wien effect. Here, using molecular dynamics simulations we show that this nonlinear response is non-monotonic for moderately concentrated aqueous electrolytes. We attribute this unanticipated behavior to the fact that, under high electric fields, the permittivity of water decreases and becomes anisotropic. The permittivity tensor measured in the simulations can be reproduced by a model of water molecules as dipoles. We incorporate the resulting anisotropic interactions between the ions into a generalised Stochastic Density Field Theory and calculate ionic correlations as well as corrections to the Nernst-Einstein conductivity which are in good agreement with the numerical simulations.

## Gromacs files
`npt.gro` is the input file for a concentration $c=0.075$ M of NaCl obtained after the energy minimisation, followed by  nvt and npt equilibration for 200 ps.

`topol.top` and `topol.tpr` are the two associated topology files.

`grommpp.mdp` is the file controlling the production run for an electrostatic field $E=0.01$ V.nm applied to the whole system .

`grommpp_ion.mdp` is the file controlling the production run for an electrostatic field $E=0.01$ V.nm applied to the ions only.

`index.ndx` is an index of the atoms in the system, necessary to run `grommpp_ion.mdp`.


## Python file
`Conductivity.py` is used to calculate the conductivity of the sytem. It computes the mean and stadard deviation of v_na-vcl.
It uses the package MDAnalysis.

## Gromacs commands
1. To apply $E$ on the whole system:  
`gmx grompp -f grompp.mdp -c npt.gro -maxwarn 2`
`gmx mdrun -v`
  
2. To apply $E$ on the ions only:   
`gmx grompp -f grompp_ion.mdp -n index.ndx -c npt.gro`
`gmx mdrun -v`
 
