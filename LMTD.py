import numpy as np
def H(hi,Ai,ro,ri,k_tube,L,ho,Ao):
    H = (1/hi + Ai*np.log(ro/ri)/(2*np.pi*k_tube*L) + (1/ho)*(Ai/Ao))**-1
    return H

def Nu_i(Re_tube,Pr):
    Nu_i = 0.023 * Re_tube**0.8 * Pr**0.3
    return Nu_i

def Nu_o(c,Re_sh,Pr):
    Nu_o = 0.023 * Re_sh**0.8 * Pr**0.3
    return Nu_o

def hi(Nu_i,kw,di):
    hi = Nu_i*kw/di
    return hi

def ho(Nu_o,kw,do):
    ho = Nu_o*kw/do
    return ho
def A(N,di,L):
    A = N * np.pi *di *L
    return A

def LMTD_counter(mass_flow_tube,mass_flow_sh,Th_in,Tc_in,H,error, Th, Tc, F, Cp,N,di,L):
    
    Th_prev = 0
    Tc_prev = 0
    A = N * np.pi *di *L
    while abs(Th-Th_prev) > error or abs(Tc-Tc_prev) > error:
        Th_prev = Th
        Tc_prev = Tc
        #print(Th,Tc)
        LMTD = abs(((Th_in-Tc) - (Th-Tc_in))/(np.log((Th_in-Tc)/(Th-Tc_in))))
        #print(LMTD)
        Tc = (H * A * LMTD * F)/(mass_flow_sh * Cp) + Tc_in
        Th = -1* (H * A * LMTD * F)/(mass_flow_tube * Cp)  + Th_in
    R = (Th_in-Th)/(Tc-Tc_in)
    P = (Tc-Tc_in)/(Th_in-Tc_in)
    kappa = ((R**2+1)**0.5)/(R-1)
    F = (kappa*(np.log((1-P)/(1-P*R))))/np.log(((2/P)-1-R+((R**2+1)**0.5))/((2/P)-1-R-((R**2+1)**0.5)))
    Q = H * A * LMTD * F
    mass = [mass_flow_sh,mass_flow_tube]
    min_flow = min(mass)
    e = Q/(min_flow*Cp*(Th_in-Tc_in))
    print(Q,e)
    return Q,e

LMTD_counter(0.5,0.47,60,20,9878.692,0.01, 55, 27, 1, 4179,13,0.006,0.35)

def NTU(mass_flow_tube,mass_flow_sh,Th_in,Tc_in,H,error, Th, Tc, F, Cp,N,di,L,no_pass):
    A = N * np.pi *di *L
    
    NTU = (H *A)/Cp
    #print(NTU)
    Rc = 1

    e_co = (1-np.exp(-NTU*(1+Rc)))/(1+Rc)
    e_counter = (1-np.exp(-NTU*(1-Rc)))/(1-Rc*np.exp(-NTU*(1-Rc)))

    e = 2* (1 +Rc + (1+Rc**2)**0.5 * (1+np.exp(-1*NTU*(1+Rc**2)**0.5))/(1-np.exp(-1*NTU*(1+Rc**2)**0.5)))**-1
    #print(e)
    Q_max = Cp*(Th_in-Tc_in)
    Q = e*Q_max
    print(Q,e)

NTU(0.5,0.47,60,20,9878.692,0.01, 55, 27, 1, 4179,13,0.006,0.35,1)