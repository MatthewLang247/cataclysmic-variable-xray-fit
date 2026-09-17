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


obs1 = '2735\n'                   # can choose any obs
obs1_5 = '3384\n'
obs2 = '2736\n'
obs2_5 = '3385\n'
obs3 = '2737\n'
obs3_5 = '3386\n'
obs4 = '2738\n'
obs4_5 = '3387\n'
obs5 = '5542\n'       
obs6 = '5543\n'       
obs7 = '5544\n'
obs8 = '5545\n'
obs9 = '6237\n'
obs10 = '6238\n'

time1,counts1,net_rate1,net_error1 = data_extractor(obs1,data)
time1_5,counts1_5,net_rate1_5,net_error1_5 = data_extractor(obs1_5,data)
time2,counts2,net_rate2,net_error2 = data_extractor(obs2,data)
time2_5,counts2_5,net_rate2_5,net_error2_5 = data_extractor(obs2_5,data)
time3,counts3,net_rate3,net_error3 = data_extractor(obs3,data)
time3_5,counts3_5,net_rate3_5,net_error3_5 = data_extractor(obs3_5,data)
time4,counts4,net_rate4,net_error4 = data_extractor(obs4,data)
time4_5,counts4_5,net_rate4_5,net_error4_5 = data_extractor(obs4_5,data)
time5,counts5,net_rate5,net_error5 = data_extractor(obs5,data)
time6,counts6,net_rate6,net_error6 = data_extractor(obs6,data)
time7,counts7,net_rate7,net_error7 = data_extractor(obs7,data)
time8,counts8,net_rate8,net_error8 = data_extractor(obs8,data)
time9,counts9,net_rate9,net_error9 = data_extractor(obs9,data)
time10,counts10,net_rate10,net_error10 = data_extractor(obs10,data)

def data_merger(set1,set2):
    set1 = list(set1)
    set2 = list(set2)
    for i in range(len(set2)):
        set1.append(set2[i])
    set_tot = np.array(set1)
    return set_tot

# time_tot = data_merger(time1,time1_5)
# counts_tot = data_merger(counts1,counts1_5)
# net_rate_tot = data_merger(net_rate1,net_rate1_5)
# net_error_tot = data_merger(net_error1,net_error1_5)

# time_tot = data_merger(time_tot,time2)
# counts_tot = data_merger(counts_tot,counts2)
# net_rate_tot = data_merger(net_rate_tot,net_rate2)
# net_error_tot = data_merger(net_error_tot,net_error2)

# time_tot = data_merger(time_tot,time2_5)
# counts_tot = data_merger(counts_tot,counts2_5)
# net_rate_tot = data_merger(net_rate_tot,net_rate2_5)
# net_error_tot = data_merger(net_error_tot,net_error2_5)

# time_tot = data_merger(time_tot,time3)
# counts_tot = data_merger(counts_tot,counts3)
# net_rate_tot = data_merger(net_rate_tot,net_rate3)
# net_error_tot = data_merger(net_error_tot,net_error3)

# time_tot = data_merger(time_tot,time3_5)
# counts_tot = data_merger(counts_tot,counts3_5)
# net_rate_tot = data_merger(net_rate_tot,net_rate3_5)
# net_error_tot = data_merger(net_error_tot,net_error3_5)

# time_tot = data_merger(time_tot,time4)
# counts_tot = data_merger(counts_tot,counts4)
# net_rate_tot = data_merger(net_rate_tot,net_rate4)
# net_error_tot = data_merger(net_error_tot,net_error4)

# time_tot = data_merger(time_tot,time4_5)
# counts_tot = data_merger(counts_tot,counts4_5)
# net_rate_tot = data_merger(net_rate_tot,net_rate4_5)
# net_error_tot = data_merger(net_error_tot,net_error4_5)

# 2004

# time_tot = data_merger(time_tot,time5)
# counts_tot = data_merger(counts_tot,counts5)
# net_rate_tot = data_merger(net_rate_tot,net_rate5)
# net_error_tot = data_merger(net_error_tot,net_error5)

time_tot = data_merger(time5,time6)
counts_tot = data_merger(counts5,counts6)
net_rate_tot = data_merger(net_rate5,net_rate6)
net_error_tot = data_merger(net_error5,net_error6)

time_tot = data_merger(time_tot,time7)
counts_tot = data_merger(counts_tot,counts7)
net_rate_tot = data_merger(net_rate_tot,net_rate7)
net_error_tot = data_merger(net_error_tot,net_error7)

time_tot = data_merger(time_tot,time8)
counts_tot = data_merger(counts_tot,counts8)
net_rate_tot = data_merger(net_rate_tot,net_rate8)
net_error_tot = data_merger(net_error_tot,net_error8)

time_tot = data_merger(time_tot,time9)
counts_tot = data_merger(counts_tot,counts9)
net_rate_tot = data_merger(net_rate_tot,net_rate9)
net_error_tot = data_merger(net_error_tot,net_error9)

time_tot = data_merger(time_tot,time10)
counts_tot = data_merger(counts_tot,counts10)
net_rate_tot = data_merger(net_rate_tot,net_rate10)
net_error_tot = data_merger(net_error_tot,net_error10)


global test_period
test_period = 0.0004091863857352128  

global choose
choose = 6


##############################################################################

def fit_func(x,A,B,C,D,E,A2,D2,E2,A3,D3,E3,A4,D4,E4,A5,D5,E5,A6,D6,E6,A7,D7,E7,A8,D8,E8,A9,D9,E9,A10,D10,E10,A11,D11,E11,A12,E12,A13,E13,A14,E14,A15,D14,E15,A16,E16,A17,E17,A18,E18,A18_,E18_,A18_1,E18_1,A18_2,E18_2,A19,D19,E19,A20,D20,E20,A21,E21,A22,E22,A23,E23,A24,E24,A25,A26):
    y_fit = []
    for i in range(len(x)):
        func1 = np.sin(test_period*x[i] + C)
        func2 = np.sin(test_period*x[i] + C + np.pi)
        x1 = 0*B
        x2= 0
        
        # obs 5542
        if x[i] > 251363386 and x[i] < 251414390:   #############
            if func2 < 0:
                x1 = 0
        # obs 5543
        elif x[i] > 251478258 and x[i] < 251530260:   #############
            if func1 < 0:
                x1 = 0
            else:
                x1 = abs(A19*x[i] + D19)*func1 + E19
        # obs 5544
        elif x[i] > 251595112 and x[i] < 251646115:   # fit will make it out of phase but for period 0.00041 will be in phase
            if func2 < 0:
                x1 = 0
            else:
                x1 = (A20*x[i] + D20)*func1 + E20
        # obs 5545
        elif x[i] > 251701702 and x[i] < 251753705:
            if func1 < 0:
                x1 = 0
            elif x[i] > 251701702 and x[i] < 251714702: #1-14
                x1 = A21*func1 + E21
            elif x[i] > 251714702 and x[i] < 251730702: #14-30
                x1 = A22*func1 + E22
        # obs 6237
        elif x[i] > 251820842 and x[i] < 251871845:
            if func2 < 0:
                x1 = 0
        # obs 6237
        elif x[i] > 251933702 and x[i] < 251981705:
            if func2 < 0:
                x1 = 0
            else:
                x1 = A26*func2
        
        else:
            x1 = 0.06
        
        ########################
        
        # obs 5542
        if x[i] > 251363386 and x[i] < 251414390:   #############
            if func1 < 0:
                x2 = 0
            elif x[i] > 251363386 and x[i] < 251392386:
                x2 = A18*func1 + E18
            elif x[i] > 251392386 and x[i] < 251376386:
                x2 = A18_*func1 + E18_
            elif x[i] > 251376386 and x[i] < 251408386:
                x2 = A18_1*func1 + E18_1*0
            else:
                x2 = A18_2*func1 + E18_2
        # obs 5543
        elif x[i] > 251478258 and x[i] < 251530260:   #############
            if func2 < 0:
                x2 = 0

        # obs 5544
        elif x[i] > 251595112 and x[i] < 251646115:   
            x2 = 0
        # obs 5545
        elif x[i] > 251701702 and x[i] < 251753705:
            if func2 < 0:
                x2 = 0
            elif x[i] > 251723702 and x[i] < 251738702: # 23-38
                x2 = A23*func2 + E23
            elif x[i] > 251738702 and x[i] < 251753705: # 23-53
                x2 = abs(A24)*func2 + E24
        # obs 6237
        elif x[i] > 251820842 and x[i] < 251871845:
            if func1 < 0:
                x2 = 0
            else:
                x2 = A25*func1
        # obs 6237
        elif x[i] > 251933702 and x[i] < 251981705:
            if func1 < 0:
                x2 = 0
            
        
        
        else:
            x2 = 0.06
        
        
        y = x1 + x2
        y_fit.append(y)
    return y_fit 


def fit(time,net_rate):
    est = [0, 4.0*10**(-4), -6000, -100, 0, 0, -250, 0, 0, -80, 0, 0, 0.04, 0, 0, 0.02, 0, 0, 0.07, 0, 0, 0.06, 0, 0, -3600, -0.1, -8.4*10**(-8), 125, 0.002, 9e-7, -140, 0.01, 0, 0, 0, 0.0015, 0.01, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.03, 0, 0.005, 0, 0.02, 0, 0.03, 0, 6e-7, -150, 0.001, 8e-7, -200, 0.003, 0.02, 0, 0.008, 0, 0.002, 0, 0.002, 0, 0.0018, 0.0018]
    parameters,covariance = curve_fit(fit_func,time,net_rate,p0=est)
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    fit_E = parameters[4]
    fit_A2 = parameters[5]
    fit_D2 = parameters[6]
    fit_E2 = parameters[7]
    fit_A3 = parameters[8]
    fit_D3 = parameters[9]
    fit_E3 = parameters[10]
    fit_A4 = parameters[11]
    fit_D4 = parameters[12]
    fit_E4 = parameters[13]
    fit_A5 = parameters[14]
    fit_D5 = parameters[15]
    fit_E5 = parameters[16]
    fit_A6 = parameters[17]
    fit_D6 = parameters[18]
    fit_E6 = parameters[19]
    fit_A7 = parameters[20]
    fit_D7 = parameters[21]
    fit_E7 = parameters[22]
    fit_A8 = parameters[23]
    fit_D8 = parameters[24]
    fit_E8 = parameters[25]
    fit_A9 = parameters[26]
    fit_D9 = parameters[27]
    fit_E9 = parameters[28]
    fit_A10 = parameters[29]
    fit_D10 = parameters[30]
    fit_E10 = parameters[31]
    fit_A11 = parameters[32]
    fit_D11 = parameters[33]
    fit_E11 = parameters[34]
    
    fit_A12 = parameters[35]
    fit_E12 = parameters[36]
    fit_A13 = parameters[37]
    fit_E13 = parameters[38]
    
    fit_A14 = parameters[39]
    fit_D14 = parameters[40]
    fit_E14 = parameters[41]
    fit_A15 = parameters[42]
    fit_E15 = parameters[43]
    fit_A16 = parameters[44]
    fit_E16 = parameters[45]
    fit_A17 = parameters[46]
    fit_E17 = parameters[47]
    
    
    fit_A18 = parameters[48]
    fit_E18 = parameters[49]
    fit_A18_ = parameters[50]
    fit_E18_ = parameters[51]
    fit_A18_1 = parameters[52]
    fit_E18_1 = parameters[53]
    fit_A18_2 = parameters[54]
    fit_E18_2 = parameters[55]
    
    fit_A19 = parameters[56]
    fit_D19 = parameters[57]
    fit_E19 = parameters[58]
    
    fit_A20 = parameters[59]
    fit_D20 = parameters[60]
    fit_E20 = parameters[61]
    
    fit_A21 = parameters[62]
    fit_E21 = parameters[63]
    fit_A22 = parameters[64]
    fit_E22 = parameters[65]
    fit_A23 = parameters[66]
    fit_E23 = parameters[67]
    fit_A24 = parameters[68]
    fit_E24 = parameters[69]
    
    fit_A25 = parameters[70]
    
    fit_A26 = parameters[71]
    
    print(fit_A,fit_B,fit_C,fit_D,fit_E,fit_A2,fit_D2,fit_E2,fit_A3,fit_D3,fit_E3,fit_A4,fit_D4,fit_E4,fit_A5,fit_D5,fit_E5,fit_A6,fit_D6,fit_E6,fit_A7,fit_D7,fit_E7,fit_A8,fit_D8,fit_E8,fit_A9,fit_D9,fit_E9,fit_A10,fit_D10,fit_E10,fit_A11,fit_D11,fit_E11,fit_A12,fit_E12,fit_A13,fit_E13,fit_A14,fit_D14,fit_E14,fit_A15,fit_E15,fit_A16,fit_E16,fit_A17,fit_E17,fit_A18,fit_E18,fit_A18_,fit_E18_,fit_A18_1,fit_E18_1,fit_A18_2,fit_E18_2,fit_A19,fit_D19,fit_E19,fit_A20,fit_D20,fit_E20,fit_A21,fit_E21,fit_A22,fit_E22,fit_A23,fit_E23,fit_A24,fit_E24,fit_A25,fit_A26)
    
    y_fit = np.array((fit_func(time,fit_A,fit_B,fit_C,fit_D,fit_E,fit_A2,fit_D2,fit_E2,fit_A3,fit_D3,fit_E3,fit_A4,fit_D4,fit_E4,fit_A5,fit_D5,fit_E5,fit_A6,fit_D6,fit_E6,fit_A7,fit_D7,fit_E7,fit_A8,fit_D8,fit_E8,fit_A9,fit_D9,fit_E9,fit_A10,fit_D10,fit_E10,fit_A11,fit_D11,fit_E11,fit_A12,fit_E12,fit_A13,fit_E13,fit_A14,fit_D14,fit_E14,fit_A15,fit_E15,fit_A16,fit_E16,fit_A17,fit_A18,fit_E18,fit_A18_,fit_E18_,fit_A18_1,fit_E18_1,fit_A18_2,fit_E18_2,fit_E17,fit_A19,fit_D19,fit_E19,fit_A20,fit_D20,fit_E20,fit_A21,fit_E21,fit_A22,fit_E22,fit_A23,fit_E23,fit_A24,fit_E24,fit_A25,fit_A26)))
    
    return y_fit, fit_B


def residual(data,fit,error):
    resid = []
    for i in range(len(data)):
        value = (data[i] - fit[i]) / error[i]
        resid.append(value)
    resid = np.array((resid))
    return resid

##############################################################################

def chi_fit_func(x,A,C,D,E,A2,D2,E2,A3,D3,E3,A4,D4,E4,A5,D5,E5,A6,D6,E6,A7,D7,E7,A8,D8,E8,A9,D9,E9,A10,D10,E10):
    y_fit = []
    for i in range(len(x)):
        func1 = np.sin(p*x[i] + C)
        func2 = np.sin(p*x[i] + C + np.pi)
        x1 = 0
        x2= 0
        if func1 < 0:      # either zero out the A's or the D's
            x1 = 0
        elif x[i] > 149706573 and x[i] < 149721573.7: # 1 - 16
            x1 = abs(A*x[i] + D)*func1 + E
        elif x[i] > 149721573.7 and x[i] < 149735573.7: # 16 - 30
            x1 = abs(A2*x[i] + D2)*func1 + E2
        elif x[i] > 149735573.7 and x[i] < 149750573.7: # 30 - 45
            x1 = abs(A3*x[i] + D3)*func1 + E3*0
        elif x[i]  >149750573.7 and x[i] < 149770573.7: # 45 - 65
            x1 = abs(A4*x[i] + D4)*func1 + E4
        elif x[i] > 149770573.7 and x[i] < 149785163.3: # 65 - 6
            x1 = abs(A5*x[i] + D5)*func1 + E5
        elif x[i] > 149785163.3 and x[i] < 149847165:
            x1 = 0
        
        if func2 < 0:
            x2 = 0
        elif x[i] > 149713573.7 and x[i] < 149729573.7: # 7 - 24
            x2 = abs(A6*x[i] + D6)*func2 + E6*0
        elif x[i] > 149729573.7 and x[i] < 149742573.7: # 24 - 37
            x2 = abs(A7*x[i] + D7)*func2 + E7
        elif x[i] > 149742573.7 and x[i] < 149760573.7: # 37 - 55
            x2 = abs(A8*x[i] + D8)*func2 + E8
        elif x[i] > 149760573.7 and x[i] < 149779733.2: # 55 - 7 (obs 3)
            x2 = abs(A9*x[i] + D9)*func2 + E9
        elif x[i] > 149779733.2 and x[i] < 149847165: 
            x2 = abs(A10*x[i] + D10)*func2 + E10
        y = x1 + x2
        y_fit.append(y)
    return y_fit 


def chi_squared(time,data,period,error):
    p_range = 0.0003
    period_array = np.linspace(period - p_range/2, period + p_range*4, num = 2000)
    #period_array = np.linspace((2*np.pi)/(4.4*3600), (2*np.pi)/(4.1*3600), num = 2000)
    
    chi_square = []
    global p
    for p in period_array:
        est = [0, -6000, -100, 0, 0, -250, 0, 0, -80, 0, 0, 0.04, 0, 0, 0.02, 0, 0, 0.07, 0, 0, 0.06, 0, 0, -3600, -0.1, -8.4*10**(-8), 125, 0.002, 0, 0, 0]
        #est = []
        parameters, covarience = curve_fit(chi_fit_func, time ,data,p0=est)
        fit_A = parameters[0]
        fit_C = parameters[1]
        fit_D = parameters[2]
        fit_E = parameters[3]
        fit_A2 = parameters[4]
        fit_D2 = parameters[5]
        fit_E2 = parameters[6]
        fit_A3 = parameters[7]
        fit_D3 = parameters[8]
        fit_E3 = parameters[9]
        fit_A4 = parameters[10]
        fit_D4 = parameters[11]
        fit_E4 = parameters[12]
        fit_A5 = parameters[13]
        fit_D5 = parameters[14]
        fit_E5 = parameters[15]
        fit_A6 = parameters[16]
        fit_D6 = parameters[17]
        fit_E6 = parameters[18]
        fit_A7 = parameters[19]
        fit_D7 = parameters[20]
        fit_E7 = parameters[21]
        fit_A8 = parameters[22]
        fit_D8 = parameters[23]
        fit_E8 = parameters[24]
        fit_A9 = parameters[25]
        fit_D9 = parameters[26]
        fit_E9 = parameters[27]
        fit_A10 = parameters[28]
        fit_D10 = parameters[29]
        fit_E10 = parameters[30]
        model_value = np.array((chi_fit_func( time ,fit_A,fit_C,fit_D,fit_E,fit_A2,fit_D2,fit_E2,fit_A3,fit_D3,fit_E3,fit_A4,fit_D4,fit_E4,fit_A5,fit_D5,fit_E5,fit_A6,fit_D6,fit_E6,fit_A7,fit_D7,fit_E7,fit_A8,fit_D8,fit_E8,fit_A9,fit_D9,fit_E9,fit_A10,fit_D10,fit_E10)))
        chi = 0
        for j in range(len(time)):
            chi = chi + (data[j] - model_value[j])**2 / error[j]**2
        chi_square.append(chi)
    chi_square = np.array((chi_square))
    return chi_square, period_array

##############################################################################

y_fit, period_fit = fit(time_tot,net_rate_tot)
resid = residual(net_rate_tot,y_fit,net_error_tot)


def chi_plot():
    chi_square, period_array = chi_squared(time_tot,net_rate_tot,period_fit,net_error_tot)
    plt.plot(2*np.pi/(period_array*3600),chi_square)
    min_chi = min(chi_square)
    
    
    min_plot = np.zeros(2000)
    for i in range(2000):
        min_plot[i] = min_chi
    
    plt.plot(2*np.pi/(period_array*3600),min_plot,label='Minimum')
    plt.plot(2*np.pi/(period_array*3600),min_plot+9,label='3 Sigma error')
    plt.ylim(200,400)
    
    plt.xlabel('Period (hours)')
    plt.ylabel('Chi-squared')
    plt.legend()

def _plot_():
    ### close data
    
    fig,axs = plt.subplots(2,1,figsize=(8,6))
    fig.subplots_adjust(hspace=0,wspace=0.05)
    axs[0].plot(time_tot,net_rate_tot,'o',label='Data')
    axs[0].errorbar(time_tot,net_rate_tot,yerr = net_error_tot,ls='none',label='Error')     #ecolor='dimgrey'
    axs[0].plot(time_tot,y_fit,color='r',label='Fit')
    axs[0].set(ylabel='Net Count Rate')
    
    axs[1].plot(time_tot,resid)
    axs[1].set(ylabel='Residuals')
    axs[1].set(xlabel='Time (s)')
    
    if choose == 1:
        axs[0].set_xlim(time5[0]-1000,time5[-1]+1000)
        axs[0].set_ylim(-0.069,0.06)
        axs[1].set_xlim(time5[0]-1000,time5[-1]+1000)
        axs[0].legend(loc='lower right')
    elif choose == 2:
        axs[0].set_xlim(time6[0]-1000,time6[-1]+1000)
        axs[0].set_ylim(-0.05,0.05)
        axs[1].set_xlim(time6[0]-1000,time6[-1]+1000)
        axs[0].legend(loc='lower right')
    elif choose == 3:
        axs[0].set_xlim(time7[0]-1000,time7[-1]+1000)
        axs[0].set_ylim(-0.12,0.12)
        axs[1].set_xlim(time7[0]-1000,time7[-1]+1000)
        axs[0].legend(loc='lower right')
    elif choose == 4:
        axs[0].set_xlim(time8[0]-1000,time8[-1]+1000)
        axs[0].set_ylim(-0.045,0.04)
        axs[1].set_xlim(time8[0]-1000,time8[-1]+1000)
        axs[0].legend(loc='lower right')
    elif choose == 5:
        axs[0].set_xlim(time9[0]-1000,time9[-1]+1000)
        axs[0].set_ylim(-0.005,0.01)
        axs[1].set_xlim(time9[0]-1000,time9[-1]+1000)
        axs[0].legend(loc='upper right')
    elif choose == 6:
        axs[0].set_xlim(time10[0]-1000,time10[-1]+1000)
        axs[0].set_ylim(-0.0028,0.008)
        axs[1].set_xlim(time10[0]-1000,time10[-1]+1000)
        axs[0].legend(loc='upper left')
    
    axs[0].tick_params(labelbottom=False)
    
    ### far data
    
    # fig,axs = plt.subplots(2,2,figsize=(8,6))
    # fig.subplots_adjust(hspace=0,wspace=0.05)
    
    # axs[0,0].spines['right'].set_visible(False)
    # axs[0,1].spines['left'].set_visible(False)
    # axs[0,1].set_yticks([])
    # axs[0,1].tick_params(labelleft=False)
    # axs[0,0].tick_params(labelbottom=False)
    # axs[0,1].tick_params(labelbottom=False)
    
    # axs[1,0].spines['right'].set_visible(False)
    # axs[1,1].spines['left'].set_visible(False)
    # axs[1,1].set_yticks([])
    # axs[1,1].tick_params(labelleft=False)
    
    # axs[0,0].set_xlim(time3[0]-4000,time3[-1]+4000)
    # axs[0,1].set_xlim(time3_5[0]-4000,time3_5[-1]+4000)
    # axs[1,0].set_xlim(time3[0]-4000,time3[-1]+4000)
    # axs[1,1].set_xlim((time3_5[0]-4000),(time3_5[-1]+4000))
    
    # axs[0,0].plot(time_tot,net_rate_tot,'o')
    # axs[0,0].errorbar(time_tot,net_rate_tot,yerr = net_error_tot,ls='none')     #ecolor='dimgrey'
    # axs[0,0].plot(time_tot,y_fit,color='r')
    # axs[0,0].set(ylabel='Net Count Rate')
    
    # axs[0,1].plot(time_tot,net_rate_tot,'o', label='Data')
    # axs[0,1].errorbar(time_tot,net_rate_tot,yerr = net_error_tot,ls='none',label='Error')
    # axs[0,1].plot(time_tot,y_fit,label='Fit',color='r')
    # axs[0,1].legend(loc='upper right')
    
    # axs[1,0].plot(time_tot,resid)
    # axs[1,0].set(ylabel='Residuals',xlabel='Obs 2736 Time (s)')
    # axs[1,1].plot(time_tot,resid,label = 'Residual')
    # #axs[1,1].xaxis.set_ticks([1.4998e8,1.5000e8,1.5002e8,1.5004e8])
    # axs[1,1].legend(loc='lower right')
    # axs[1,1].set(xlabel='Obs 2737 Time (s)')

_plot_()
#chi_plot()


# Things to look at:
    
# obs 2738 and 3387 has slight spike (??????) time 4-4.5
# obs 5544 will appear to be completely out of phase for initial fit but chi^2 min period makes it in phase, time 7
# obs 5543 ? (maybe a small pulse), time 6
# obs 5542 acting strange, time 5