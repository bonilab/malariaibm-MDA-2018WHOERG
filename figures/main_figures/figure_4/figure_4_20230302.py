# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 16:25:31 2018

@author: NguyenTran
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

fs = 22
font = {
        'weight' : 'normal',
        'size'   : fs }

matplotlib.rc('font', **font)

sns.set(style="whitegrid")
palette = sns.color_palette()[0:5]
sns.set(font_scale=1.5)

# dates = pd.date_range(start= "1 1 2006", end= "1 1 2040", freq="MS")

t = pd.read_csv('monthly_data_0.txt',delimiter='\t',header=None)[0]
#%%

import matplotlib.ticker as ticker
from matplotlib.collections import PathCollection

from matplotlib.lines import Line2D
flierprops = dict(markerfacecolor='0.75', markersize=5, linestyle='none')

plt.close('all')


fs = 12
font = {
        'weight' : 'normal',
        'size'   : fs }

matplotlib.rc('font', **font)
sns.set(font_scale=1)
sns.set_style("whitegrid", {'ytick.left': True })



plt.close('all')
fig, ax = plt.subplots( 2, 1,figsize=(12, 8), dpi=150,tight_layout=True) 

#figure(num=None, figsize=(12, 4), dpi=150, facecolor='w', edgecolor='k', tight_layout=True)

mdas = [0,1,2,3,4]
pfprs = [2]
importations = [0, 0.001, 0.01, 0.1, 0.2]
importations_value = ['0p0', '0p001', '0p01', '0p1', '0p2']

list_ = []
threshold = 0.25
for pfpr in pfprs:
    for importation_i, importation in enumerate(importations):
        for mda in mdas:
            data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_importation_%s_C580Y.csv'%(mda,pfpr,importations_value[importation_i]), sep=',', header=None)
            data = data.fillna(0)
            time_t=[]
            for i in range(100):
                time_C580Y_reach_25 = (t.iloc[next((i for i,x in enumerate(data[i]) if x>=threshold),408)] - 5113)/365
                time_t.append(time_C580Y_reach_25)
            
            
            data = pd.DataFrame({'t25':time_t})
            data['mda'] = mda
            data['importation'] = importation
            
#            print(data.count())
            
            list_.append(data)

all_data = pd.concat(list_)


#ax = sns.boxplot(x="importation", y="t25",hue="mda" , data=all_data, palette="muted",fliersize=4,flierprops=flierprops)


ax1 = sns.boxplot(x="importation", y="t25",hue="mda" , data=all_data,showfliers=False,boxprops={ "zorder":10},ax = ax[0])

# Add transparency to colors
for patch in ax1.patches:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b,0.2))
#
#for artist in ax.lines:
#    artist.set_zorder(10)
#for artist in ax.findobj(PathCollection):
#    artist.set_zorder(11)

ax2= sns.stripplot(x="importation", y="t25", hue="mda", data=all_data, jitter=True, dodge= True, size=3, alpha=0.75,ax = ax[0])
for artist in ax2.findobj(PathCollection):
    artist.set_zorder(1)

#plt.yscale('log')
ax1.tick_params(axis='both', which='both')
ax1.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())

#ax.set_ylim(0.001, 25)

#custom_lines = [Line2D([0], [0], color=palette[0], lw=4),
#                Line2D([0], [0], color=palette[1], lw=4),
#                Line2D([0], [0], color=palette[2], lw=4),
#                Line2D([0], [0], color=palette[3], lw=4),
#                Line2D([0], [0], color=palette[4], lw=4),
#                ]
#ax1.legend(custom_lines, ['0', '1', '2','3','4'], title="# of MDA rounds", loc="lower left", ncol=2)
ax1.legend_.remove()

ax1.set_ylabel('40K\n'+'YEARS UNTIL\n25% ARTEMISININ RESISTANCE', linespacing=1.5)

ax1.set_xlabel('')


#%%
list_ = []

for pfpr in pfprs:
    for importation_i, importation in enumerate(importations):
        for mda in mdas:
            data= pd.read_csv('data\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_importation_%s_C580Y.csv'%(mda,pfpr,importations_value[importation_i]), sep=',', header=None)
            data = data.fillna(0)
            time_t=[]
            for i in range(100):
                time_C580Y_reach_25 = (t.iloc[next((i for i,x in enumerate(data[i]) if x>=threshold),408)] - 5113)/365
                time_t.append(time_C580Y_reach_25)
            
            
            data = pd.DataFrame({'t25':time_t})
            data['mda'] = mda
            data['importation'] = importation
            
            
            list_.append(data)

all_data = pd.concat(list_)


#ax = sns.boxplot(x="importation", y="t25",hue="mda" , data=all_data, palette="muted",fliersize=4,flierprops=flierprops)


ax1 = sns.boxplot(x="importation", y="t25",hue="mda" , data=all_data,showfliers=False,boxprops={ "zorder":10},ax = ax[1])

# Add transparency to colors
for patch in ax1.patches:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b,0.2))
#
#for artist in ax.lines:
#    artist.set_zorder(10)
#for artist in ax.findobj(PathCollection):
#    artist.set_zorder(11)

ax2= sns.stripplot(x="importation", y="t25", hue="mda", data=all_data, jitter=True, dodge= True, size=3, alpha=0.75,ax = ax[1])
for artist in ax2.findobj(PathCollection):
    artist.set_zorder(1)

#plt.yscale('log')
ax1.tick_params(axis='both', which='both')
ax1.yaxis.set_major_formatter(ticker.ScalarFormatter(useMathText=True))
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())

# ax.set_ylim(0.001, 25)

custom_lines = [Line2D([0], [0], color=palette[0], lw=4),
                Line2D([0], [0], color=palette[1], lw=4),
                Line2D([0], [0], color=palette[2], lw=4),
                Line2D([0], [0], color=palette[3], lw=4),
                Line2D([0], [0], color=palette[4], lw=4),
                ]
ax1.legend(custom_lines, ['0', '1', '2','3','4'], title="# MDA ROUNDS", loc="lower left", ncol=2)

ax1.set_ylabel('300K\n'+'YEARS UNTIL\n25% ARTEMISININ RESISTANCE', linespacing=1.5)

ax1.set_xlabel('IMPORTATION RATE (CASES PER DAY)')
