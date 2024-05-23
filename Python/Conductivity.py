import pyblock
import numpy as np
import MDAnalysis as mda
from MDAnalysis.analysis.distances import distance_array
from numpy import random
import scipy.integrate as integrate
from scipy.integrate import quad
from scipy.optimize import minimize
import math
import itertools
import argparse
from numpy.linalg import norm
from numpy import random


def v_contruction():
    V=np.zeros((3,lt-500))
    D=np.zeros((3,lt-500))
    i=0
    for ts in range (500,lt):
        u.trajectory[ts]
        pos_na_t=na_group.positions
        pos_cl_t=cl_group.positions
        u.trajectory[ts-1]
        pos_na_tm1=na_group.positions
        pos_cl_tm1=cl_group.positions
        Dpos_na=pos_na_t-pos_na_tm1
        Dpos_cl=pos_cl_t-pos_cl_tm1
        Dpos_na[np.where(Dpos_na>Lbox/2)]-=Lbox
        Dpos_cl[np.where(Dpos_cl>Lbox/2)]-=Lbox
        Dpos_cl[np.where(Dpos_cl<-Lbox/2)]+=Lbox
        Dpos_na[np.where(Dpos_na<-Lbox/2)]+=Lbox
        Deltat=2*10**(-3)
        j=Dpos_na-Dpos_cl
        Vt=j/Deltat/10 # velocity in nm.ns^(-1)
        V[:,i]=np.mean(Vt,axis=0) #mean sur tous les ions
        D[:,i]=np.mean(Vt**2,axis=0)
        i=i+1
    return V,D

def Reblocking():
    V,D=v_contruction()	
    siz=np.shape(V)[1]
    reblock_data=pyblock.blocking.reblock(V[1,:])
    opt=pyblock.blocking.find_optimal_block(siz,reblock_data)
    optimalblock=reblock_data[opt[0]]
    s_i=opt[0]
    print('decorrelation',s_i)
    return s_i 
    
def Conductivity():
    t=Reblocking()
    V,D=v_contruction()
    siz=np.shape(V)
    x=siz[1]//t
    V_t=np.zeros((3,t))
    D_t=np.zeros((3,t))
    k=0
    for j in range(t):
        t_s=(j)*x+500
        t_f=(j+1)*x+500
        V_t[:,k]=np.mean(V[:,t_s:t_f],axis=1)
        k=k+1
    return V_t     

if __name__ == "__main__":
   
    cos=math.cos
    Pi=math.pi
    u = mda.Universe("topol.tpr", "traj_comp.xtc")
    
    Qe=1.6*10**(-19)
    o_group = u.select_atoms("name MW")
    h1_group = u.select_atoms("name HW1")
    h2_group = u.select_atoms("name HW2")
    na_group = u.select_atoms("name NA")
    cl_group = u.select_atoms("name CL")
    Lbox=u.dimensions[0]
    print('L=',Lbox)
    lt=(len(u.trajectory))    
    print('longueur traj=',lt)
    print('starting time=', 500*2*10**(-3))
    V_t=Conductivity()
    print('vitesse',np.mean(V_t,axis=1))
    print('std', np.std(V_t, axis=1))
