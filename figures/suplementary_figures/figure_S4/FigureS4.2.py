# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:14:15 2019

@author: nguyentd
"""

import pandas as pd
import datetime as dt
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

fs = 12
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : fs }

matplotlib.rc('font', **font)
plt.rc('text', usetex=False)


scenarios = [
    "",      
    "_imp", 
    "_itc", 
    "_itc_imp", 
        ]

y_labels = [
    "   ",      
    "   \nIMPORTATION", 
    "ITC\n   ", 
    "ITC\nIMPORTATION", 
        ]
mdas = [0,1,2,3,4]
pfpr = 5

figure_index = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']

dates = pd.date_range(start= "1 1 2008", end= "1 1 2042", freq="MS")

def myLogFormat(y,pos):
    # Find the number of decimal places required
    decimalplaces = int(np.maximum(-np.log10(y),0))     # =0 for numbers >=1
    # Insert that number into a format string
    formatstring = '{{:.{:1d}f}}'.format(decimalplaces)
    # Return the formatted tick label
    return formatstring.format(y)


#%%
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D


main_lw = 1.5
sub_lw = 0.8

infected_plot_color = '#b1b1b1'
palette = sns.color_palette()[0:5]

sns.set( font_scale=2.2)
sns.set_style("whitegrid", {'ytick.left': True })
matplotlib.rc('font', **font)
matplotlib.rc('text', usetex = False)
plt.rc('text', usetex=False)


plt.close('all')

dpi=72
fig_w = 3240/dpi
fig_h = fig_w*30/40

plt.close('all')
fig, ax = plt.subplots(4,4, figsize=(fig_w, fig_h),tight_layout=True)

locmaj = matplotlib.ticker.LogLocator(base=10,numticks=12) 
locmin = matplotlib.ticker.LogLocator(base=10.0,subs=np.arange(0,1,0.1),numticks=12)

#ax22.set_ylabel('NUMBER OF POSITIVE INIDIVIDUALS\nANY LEVEL OF PARASITEAMIA')

for idx, scenario in enumerate(scenarios):
    print(idx, scenario)   
#    
#    ax21 = ax[idx,1].twinx()
#    ax22 = ax[idx,2].twinx()
#    
    for i_mda, mda in enumerate(mdas):  
        freq_580Y_plas2 =  pd.read_csv('data_300k\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_580Y_plas2.csv'%(mda,pfpr,scenario), sep=',', header=None)
        freq_580Y= pd.read_csv('data_300k\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_C580Y.csv'%(mda,pfpr,scenario), sep=',', header=None)
        freq_plas2= pd.read_csv('data_300k\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_plas.csv'%(mda,pfpr,scenario), sep=',', header=None)
        freq_plas2 = freq_plas2.fillna(0)
        freq_580Y = freq_580Y.fillna(0)
        freq_580Y_plas2 = freq_580Y_plas2.fillna(0)
        
    
#        ax[idx].fill_between(r.index, r[.25], r[.75], alpha=.2)
#        ax[idx].plot(r.index, r[0.5], linewidth=main_lw)
        
        r = freq_580Y.quantile([0.25,0.5,0.75], axis=1).T+0.00001
        r.index = dates
        ax[idx,0].fill_between(r.index, r[.25], r[.75], alpha=.2)
        ax[idx,0].plot(r.index, r[0.5], linewidth=main_lw)
        ax[idx,0].set_yscale('log')
        
        ax[idx,0].yaxis.set_major_formatter(ticker.FuncFormatter(myLogFormat))
        # ax[idx,0].yaxis.set_major_formatter(ticker.ScalarFormatter())
        ax[idx,0].yaxis.set_minor_formatter(ticker.NullFormatter())

        ax[idx,0].yaxis.set_major_locator(locmaj)
        ax[idx,0].yaxis.set_minor_locator(locmin)
        ax[idx,0].set_ylim(0.00001, 1)
        ax[idx,0].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))  
         
        r = freq_plas2.quantile([0.25,0.5,0.75], axis=1).T+0.00001
        r.index = dates
        ax[idx,1].fill_between(r.index, r[.25], r[.75], alpha=.2)
        ax[idx,1].plot(r.index, r[0.5], linewidth=main_lw)
        ax[idx,1].set_yscale('log')
        
        ax[idx,1].yaxis.set_major_formatter(ticker.NullFormatter())
        ax[idx,1].yaxis.set_minor_formatter(ticker.NullFormatter())
        ax[idx,1].yaxis.set_major_locator(locmaj)
        ax[idx,1].yaxis.set_minor_locator(locmin)
        
        ax[idx,1].set_ylim(0.00001, 1)
        ax[idx,1].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))  
        
        r = freq_580Y_plas2.quantile([0.25,0.5,0.75], axis=1).T+0.00001
        r.index = dates
        ax[idx,2].fill_between(r.index, r[.25], r[.75], alpha=.2)
        ax[idx,2].plot(r.index, r[0.5], linewidth=main_lw)
        ax[idx,2].set_yscale('log')

        ax[idx,2].yaxis.set_major_formatter(ticker.NullFormatter())
        ax[idx,2].yaxis.set_minor_formatter(ticker.NullFormatter())
        ax[idx,2].yaxis.set_major_locator(locmaj)
        ax[idx,2].yaxis.set_minor_locator(locmin)
        
        ax[idx,2].set_ylim(0.00001, 1)
        ax[idx,2].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))  
        
        LD=  freq_580Y_plas2 - freq_580Y * freq_plas2
        
        r = LD / np.sqrt(  freq_580Y * freq_plas2 * (1-freq_580Y) * (1-freq_plas2) )     
        r = r.fillna(0)
        r = r.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T        
        r.index = dates
        ax[idx,3].fill_between(r.index, r[.25], r[.75], alpha=.2)
        ax[idx,3].plot(r.index, r[0.5], linewidth=main_lw)
        ax[idx,3].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))  
        

    if(idx>=3):
        ax[idx,0].set_xlabel('YEAR')
        ax[idx,1].set_xlabel('YEAR')
        ax[idx,2].set_xlabel('YEAR')
        ax[idx,3].set_xlabel('YEAR')
    else:
        ax[idx,0].set_xticklabels('')
        ax[idx,1].set_xticklabels('')
        ax[idx,2].set_xticklabels('')
        ax[idx,3].set_xticklabels('')


    if (idx ==0):
        ax[idx,0].set_title('ALLELE FREQUENCY OF 580Y')
#        ax[idx,0].set_title('PfPR_2-10')
        ax[idx,1].set_title('GENOTYPE FREQUENCY OF\n DOUBLE-COPY PLASMEPSIN')        
        ax[idx,2].set_title('GENOTYPE FREQUENCY OF\n DOUBLE-COPY PLASMEPSIN + 580Y')
        ax[idx,3].set_title('LINKAGE DISEQUILIBRIUM')
          
    #remove year 2042 tick label
    dr = pd.date_range(start= "1 1 2022", end= "1 1 2041", freq="5YS")
    ax[idx,0].set_xticks(dr)
    ax[idx,1].set_xticks(dr)
    ax[idx,2].set_xticks(dr)
    ax[idx,3].set_xticks(dr)

    if(idx==3):
        ax[idx,0].set_xticklabels(range(2022,2041,5))
        ax[idx,1].set_xticklabels(range(2022,2041,5))
        ax[idx,2].set_xticklabels(range(2022,2041,5))
        ax[idx,3].set_xticklabels(range(2022,2041,5))
        
    ax[idx,0].set_ylabel(y_labels[idx],linespacing=1.5)
    
    fig.canvas.draw()
        # remove ytick label 0 for frequency plot
    ytick_labels =  [item.get_text() for item in ax[idx,0].get_yticklabels()]
    # print(ytick_labels)
    ytick_labels[0] = ''
    ytick_labels[1] = ''
#    print(ytick_labels)
    ax[idx,0].set_yticklabels(ytick_labels)
    ax[idx,1].set_yticklabels([])
    ax[idx,2].set_yticklabels([])
    
    ax[idx,0].text(dt.date(2020, 6, 1), 0.3, figure_index[idx*3], fontsize=25, weight='bold')
    ax[idx,1].text(dt.date(2020, 6, 1), 0.3, figure_index[idx*3+1], fontsize=25, weight='bold')
    ax[idx,2].text(dt.date(2020, 6, 1), 0.3, figure_index[idx*3+2], fontsize=25, weight='bold')
    
    
custom_lines = [Line2D([0], [0], color=palette[0], lw=4),
                Line2D([0], [0], color=palette[1], lw=4),
                Line2D([0], [0], color=palette[2], lw=4),
                Line2D([0], [0], color=palette[3], lw=4),
                Line2D([0], [0], color=palette[4], lw=4),
                ]
# ax[0,3].legend(custom_lines, ['0', '1', '2','3','4'], title="# MDA ROUNDS")

#%%
ax[0,3].text(dt.date(2020, 6, 1), 0.11, figure_index[0*3+3], fontsize=25, weight='bold')
ax[1,3].text(dt.date(2020, 6, 1), 0.5, figure_index[1*3+3], fontsize=25, weight='bold')
ax[2,3].text(dt.date(2020, 6, 1), 0.1, figure_index[2*3+3], fontsize=25, weight='bold')
ax[3,3].text(dt.date(2020, 6, 1), 0.5, figure_index[3*3+3], fontsize=25, weight='bold')

