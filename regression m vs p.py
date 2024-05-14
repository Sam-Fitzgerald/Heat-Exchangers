import numpy as np
import matplotlib.pyplot as plt

def cold():
    cold_flowrate = [0.5776, 0.5597, 0.5152, 0.4626, 0.4203, 0.3568, 0.2717, 0.1870, 0.1444, 0.1024]
    cold_pressure_rise =[0.1583, 0.1917, 0.2417, 0.3083, 0.3583, 0.4250, 0.5083, 0.5750, 0.6083, 0.6333]

    fit = np.polyfit(cold_flowrate, cold_pressure_rise, 2, rcond=None, full=False, w=None, cov=False)
    print(fit)
    x = np.linspace(0, 1, 100)
    y = fit[2] +fit[1]*x +fit[0]*x**2#+fit[3]*x**3 +fit[4]*x**4 +fit[5]*x**5
    plt.plot(x,y)
    return fit


def hot():
    hot_flowrate= [0.4826, 0.4340, 0.3924, 0.3507, 0.3021, 0.2535, 0.1979, 0.1493, 0.1111, 0.0694] 
    hot_pressure_rise =[0.0944, 0.1662, 0.2297, 0.2820, 0.3294, 0.3856, 0.4447, 0.5006, 0.5311, 0.5615]
    fit = np.polyfit(hot_flowrate, hot_pressure_rise, 2, rcond=None, full=False, w=None, cov=False)
    print(fit)
    x = np.linspace(0, 1, 100)
    y = fit[2] +fit[1]*x +fit[0]*x**2#+fit[3]*x**3 #+fit[4]*x**4 +fit[5]*x**5
    plt.plot(x,y)
    plt.show()
    return fit

print(hot())
print(cold())



