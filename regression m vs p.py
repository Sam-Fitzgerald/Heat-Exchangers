import numpy as np
import matplotlib.pyplot as plt

def cold():
    cold_flowrate = [0.7083,0.6417,0.5750,0.5083,0.4250,0.3583,0.3083,0.2417,0.1917,0.1583]
    cold_pressure_rise =[0.1310,0.2017,0.2750,0.3417,0.4038,0.4503,0.4856,0.5352,0.5717,0.5876]
    fit = np.polyfit(cold_flowrate, cold_pressure_rise, 2, rcond=None, full=False, w=None, cov=False)
    print(fit)
    x = np.linspace(0, 1, 100)
    y = fit[2] +fit[1]*x +fit[0]*x**2#+fit[3]*x**3 +fit[4]*x**4 +fit[5]*x**5
    plt.plot(x,y)
    return fit


def hot():
    hot_flowrate= [0.4722,0.4340, 0.3924, 0.3507, 0.3021, 0.2535, 0.1979, 0.1493, 0.1111, 0.0694] 
    hot_pressure_rise =[0.0538,0.1192,0.1727,0.2270,0.2814,0.3366,0.3907,0.4456,0.4791,0.5115]
    fit = np.polyfit(hot_flowrate, hot_pressure_rise, 2, rcond=None, full=False, w=None, cov=False)
    print(fit)
    x = np.linspace(0, 1, 100)
    y = fit[2] +fit[1]*x +fit[0]*x**2#+fit[3]*x**3 #+fit[4]*x**4 +fit[5]*x**5
    plt.plot(x,y)
    plt.show()
    return fit

   
def mass_flow(p_loss_shell,p_loss_tube,saftey factor):

