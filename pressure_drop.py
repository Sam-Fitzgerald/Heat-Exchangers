import numpy as np

def p_end_approx(Re, sigma,mass_flow_tube,A_tube):
    Kc =  0.41 +0.12*np.exp(-0.000026*(Re-3000)) - 0.4*sigma
    Ke = (1-sigma)**2 # for Re is infinate case (worst case) could be up to 0.1 smaller   
    print(Kc,Ke)  
    rho = 990.1   
    v = mass_flow_tube/(A_tube*rho)
    print(v) 
    p_end = 0.5*rho*(Kc+Ke)*v**2
    return p_end

kc = p_end_approx(15000,0.114, 0.034615,2.8274e-5)
