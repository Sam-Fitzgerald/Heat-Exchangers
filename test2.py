import numpy as np


T_in_hot = 60
T_in_cold = 20
rho = 990.1
Cp = 4179
mu = 0.000651
Pr = 4.31
k = 0.632
k_tube = 386
ltot = 3.5
#Dimensions
di_shell = 0.064
d_noz = 0.02
di_tube = 0.006
do_tube = 0.008
l_shell = 0.27
Re_hot = 10
Re_cold = 9


#defs
def reynolds(v, di, mu = 0.000651, rho = 990.1):
    return(rho*di*v/mu)

def velocity(m_dot,diameter, rho = 990.1):
    a_temp = 3.1415926*0.25*(diameter**2)
    return(m_dot/(rho*a_temp))

def massflow_cold( dp ):
    cold=[-0.79464036, -0.45389983,  0.68890994]
    return(cold[2] +cold[1]*dp +cold[0]*dp**2)
    
def massflow_hot( dp ):
    hot=[-0.81172445, -0.67918997,  0.61450441]
    return (hot[2] +hot[1]*dp +hot[0]*dp**2)

def dp(v, l_pipe, di, f, rho = 990.1):
    dp_temp = 0.5*rho*(v**2)*f*l_pipe/di
    return(dp_temp)

def friction(Re):
    temp_re = 1.82*np.log10(Re)-1.64
    return (temp_re**(-2))

def kc_ke(Re, sigma):
    Kc =  0.41 +0.12*np.exp(-0.000026*(Re-3000)) - 0.4*sigma
    Ke = (1-sigma)**2 # for Re is infinate case (worst case) could be up to 0.1 smaller   
    return Kc, Ke


def hot_dp_mf(n, massflow_h, no_pass, l_per_pipe, di = 0.006, rho = 990.1):
    #hot stream analysis
    
    massflow_h_prev = 0

    while abs(massflow_h-massflow_h_prev) > 0.0001:
        massflow_per_tube = massflow_h / (n/no_pass)
        massflow_h_prev = massflow_h
        v_pipe = velocity(massflow_per_tube, di)
        v_noz2 = velocity(massflow_h, 0.02)
        Re_hot = reynolds (v_pipe, di)
        print(Re_hot)
        f = friction (Re_hot)
        #ends
        area_r = n*((di**2)/(0.064**2))
        kc, ke = kc_ke(Re_hot, area_r)

        #pdrop for hot stream
        dp_nozzle2 = rho*(v_noz2**2)

        dp_ends = 0.5*rho*(v_pipe**2)*(kc+ke)*(no_pass)

        dp_hot_pipe = no_pass * dp(v_pipe, l_per_pipe , di, f)

        dp_total_hot = dp_nozzle2 + dp_ends + dp_hot_pipe
        print(dp_total_hot)
        massflow_h = massflow_hot(dp_total_hot*0.00001)
        print(massflow_h)
    return(massflow_h, dp_total_hot, Re_hot)


n_pipe = 12 #use total pipes
n_baffle = 9 #use baffles per section for now
pitch = 0.014  #for a square, keeping const for now
massflow_h = 0.272
massflow_c = 0.7

l_shell_max = 0.28 - (0.28/(n_baffle+1))
l_shell = ltot/(n_pipe)
if l_shell > l_shell_max:
    l_shell = l_shell_max

a_value = {"triangle":0.2, "square":0.34}
No_pass = 2
No_sh =1

hot_dp_mf(n_pipe, massflow_h, No_pass, l_shell)