"""
Created on Fri Jan 20 11:21:02 2023

@author: mflan
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def data_matrix():
    data = []
    obs = 0
    with open('X10_1ks_Lightcurves_ascii') as file:
        for line in file:
            if line.__contains__('Obs'):
                obs = line.replace('Obs ','')
            if obs != 0 and line.__contains__('Obs') != True:
                values = ' '.join(line.split())
                values.split()
                values = values.split()
                row = [obs]
                for i in range(len(values)):
                    row.append(values[i])
                data.append(row)
        return data

data = data_matrix()
# columns are (starting from column 0)

# obs number
# row number for obs
# time in modified julian date
# counts (x-ray photons, though some will be noise) how would I use this???
# exposure time (seconds?) if zero delete row
# net count rate (counts - background)/exposure
# error in net count rate (will be zero for zero exposure) need to recalculate this


def data_extractor(obs,data):
    time = []
    counts = []
    exposure = []
    net_rate = []

    for item in data:    
        if item[0] == obs:
            if item[4] != 0: 
                time.append(float(item[2]))
                counts.append(float(item[3]))
                exposure.append(float(item[4]))
                net_rate.append(float(item[5]))
    counts = np.array((counts))
    time = np.array((time))
    net_rate = np.array((net_rate))
    exposure = np.array((exposure))
    
    net_error = []
    for i in range(len(net_rate)):
        if counts[i] == 0:
            err = (1+np.sqrt(3/4)) / exposure[i]
        else:
            err = net_rate[i] * (np.sqrt(counts[i] + 3/4) + 1)/counts[i]
        net_error.append(err)
    net_error = np.array((net_error))
    
    return time,counts,net_rate,net_error


obs = '2737\n'          # can choose any obs
obs2 = '2736\n'

time,counts,net_rate,net_error = data_extractor(obs,data)
time2,counts2,net_rate2,net_error2 = data_extractor(obs2,data)

def data_merger(set1,set2):
    set1 = list(set1)
    set2 = list(set2)
    for i in range(len(set2)):
        set1.append(set2[i])
    set_tot = np.array(set1)
    return set_tot

time_tot = data_merger(time2,time)
counts_tot = data_merger(counts2,counts)
net_rate_tot = data_merger(net_rate2,net_rate)
net_error_tot = data_merger(net_error2,net_error)

##############################################################################

def fit_func(x,A,B,C,D,E,F):
    y_fit = []
    for i in range(len(x)):
        if x[i] > 149847164:             # last time in obs 2736
            function = np.sin(B*x[i]+C)
            y = A*function + D
        else:
            function = np.sin(B*x[i]+(C+np.pi))
            y = (E*x[i] + F)*function + 0.002
            if function < 0:
                y = 0.002
        y_fit.append(y)
    return y_fit 


def fit(time,net_rate):
    est = [0.04, 4.0*10**(-4), -6000, 0.01,-8.4*10**(-8),125]
    parameters,covariance = curve_fit(fit_func,time,net_rate,p0=est)
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    fit_E = parameters[4]
    fit_F = parameters[5]
    
    print(fit_A,fit_B,fit_C,fit_D,fit_E,fit_F)
    
    y_fit = np.array((fit_func(time,fit_A,fit_B,fit_C,fit_D,fit_E,fit_F)))
    
    return y_fit, fit_C


def residual(data,fit,error):
    resid = []
    for i in range(len(data)):
        value = (data[i] - fit[i]) / error[i]
        resid.append(value)
    resid = np.array((resid))
    return resid

##############################################################################

def chi_fit_func(x,A,B,D,E,F,B_2):
    y_fit = []
    for i in range(len(x)):
        if x[i] > 149847164:             # last time in obs 2736
            function = np.sin(B*x[i]+p)
            y = A*function + D
        else:
            function = np.sin(B_2*x[i]+(p+np.pi))
            y = (E*x[i] + F)*function + 0.002
            if function < 0:
                y = 0.002
        y_fit.append(y)
    return y_fit 


def chi_squared(time,data,phase,error):          # PI PHASE SHIFT
    p_range = np.pi/2
    #phase_array = np.linspace(phase - p_range, phase + p_range, num = 2000)
    phase_array = np.linspace(-1657.1994*np.pi, -1657.19936*np.pi, num = 6000)
    
    chi_square = []
    global p
    for p in phase_array:
        est = [0.04,4.0*10**(-4),0.01,-8.4*10**(-8),125,4.0*10**(-4)]
        parameters, covarience = curve_fit(chi_fit_func, time ,data,p0=est)
        A = parameters[0]
        B = parameters[1]
        D = parameters[2]
        E = parameters[3]
        F = parameters[4]
        B_2 = parameters[5]
        model_value = np.array((chi_fit_func( time ,A,B,D,E,F,B_2)))
        chi = 0
        for j in range(len(time)):
            chi = chi + (data[j] - model_value[j])**2 / error[j]**2
        chi_square.append(chi)
    chi_square = np.array((chi_square))
    return chi_square, phase_array

##############################################################################

y_fit, phase_fit = fit(time_tot,net_rate_tot)
resid = residual(net_rate_tot,y_fit,net_error_tot)


def chi_plot():
    chi_square, phase_array = chi_squared(time_tot,net_rate_tot,phase_fit,net_error_tot)
    plt.plot(phase_array/np.pi,chi_square)
    min_chi = min(chi_square)
    
    
    min_plot = np.zeros(6000)
    for i in range(6000):
        min_plot[i] = min_chi
    
    plt.plot(phase_array/np.pi,min_plot,label='Minimum')
    #plt.plot(phase_array/np.pi,min_plot+9,label='3 Sigma error')
    #plt.xticks([-1657.35,-1657.25,-1657.15,-1657.05,-1656.95])
    plt.ylim(194,196)
    
    plt.xlabel('pi multiples')
    plt.ylabel('Chi-squared')
    plt.legend()

def _plot_():
    fig,axs = plt.subplots(2,2,figsize=(8,6))
    fig.subplots_adjust(hspace=0,wspace=0.05)
    
    axs[0,0].spines['right'].set_visible(False)
    axs[0,1].spines['left'].set_visible(False)
    axs[0,1].set_yticks([])
    axs[0,1].tick_params(labelleft=False)
    axs[0,0].tick_params(labelbottom=False)
    axs[0,1].tick_params(labelbottom=False)
    
    axs[1,0].spines['right'].set_visible(False)
    axs[1,1].spines['left'].set_visible(False)
    axs[1,1].set_yticks([])
    axs[1,1].tick_params(labelleft=False)
    
    axs[0,0].set_xlim(time2[0]-4000,time2[-1]+4000)
    axs[0,1].set_xlim(time[0]-4000,time[-1]+4000)
    axs[1,0].set_xlim(time2[0]-4000,time2[-1]+4000)
    axs[1,1].set_xlim((time[0]-4000),(time[-1]+4000))
    
    axs[0,0].plot(time_tot,net_rate_tot,'o')
    axs[0,0].errorbar(time_tot,net_rate_tot,yerr = net_error_tot,ls='none')     #ecolor='dimgrey'
    axs[0,0].plot(time_tot,y_fit,color='r')
    axs[0,0].set(ylabel='Net Count Rate')
    
    axs[0,1].plot(time_tot,net_rate_tot,'o', label='Data')
    axs[0,1].errorbar(time_tot,net_rate_tot,yerr = net_error_tot,ls='none',label='Error')
    axs[0,1].plot(time_tot,y_fit,label='Fit',color='r')
    axs[0,1].legend(loc='upper right')
    
    axs[1,0].plot(time_tot,resid)
    axs[1,0].set(ylabel='Residuals',xlabel='Obs 2736 Time (s)')
    axs[1,1].plot(time_tot,resid,label = 'Residual')
    #axs[1,1].xaxis.set_ticks([1.4998e8,1.5000e8,1.5002e8,1.5004e8])
    axs[1,1].legend(loc='lower right')
    axs[1,1].set(xlabel='Obs 2737 Time (s)')

#_plot_()
chi_plot()