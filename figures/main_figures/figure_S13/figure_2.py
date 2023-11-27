# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:03:19 2018

@author: NguyenTran
"""

#%%
import pandas as pd
import datetime as dt

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
pfpr = 2

figure_index = ['A','B','C','D','E','F','G','H','I','J','K','L']

dates = pd.date_range(start= "1 1 2008", end= "1 1 2042", freq="MS")
#%%

import matplotlib.ticker as ticker

main_lw = 1.5
sub_lw = 0.8

infected_plot_color = '#b1b1b1'

sns.set( font_scale=2.2)
sns.set_style("whitegrid", {'ytick.left': True })
matplotlib.rc('font', **font)
matplotlib.rc('text', usetex = False)
plt.rc('text', usetex=False)

palette = sns.color_palette()[0:5]

plt.close('all')

dpi=72
fig_w = 3240/dpi
fig_h = fig_w*3/4

plt.close('all')
fig, ax = plt.subplots(4,3, figsize=(fig_w, fig_h),tight_layout=True)  
# fig, ax = plt.subplots( 4, 3,figsize=(30,10),tight_layout=True)  

#ax22.set_ylabel('NUMBER OF POSITIVE INIDIVIDUALS\nANY LEVEL OF PARASITEAMIA')


for idx, scenario in enumerate(scenarios):
    print(idx, scenario)   
    
    ax21 = ax[idx,1].twinx()
    ax22 = ax[idx,2].twinx()
    
    for i_mda, mda in enumerate(mdas):        
        data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_pfpr.csv'%(mda,pfpr,scenario ), sep=',', header=None)
        data = data.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T                        
        data.index = dates
        
        ax[idx,0].fill_between(data.index, data[.25], data[.75], alpha=.2)
        ax[idx, 0].plot(data.index, data[.5], linewidth=main_lw)
   
        data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_positive.csv'%(mda,pfpr,scenario), sep=',', header=None)
        data = data.fillna(0)
        data = data.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T        
        data.index = dates
#        ax[idx,1].fill_between(data.index, data[.25], data[.75], alpha=.2)
        
        ## plot number of infected individuals
        ax21.plot(data.index, data[.5], color=infected_plot_color,  linewidth=sub_lw)
        ax21.tick_params(axis='y', colors=infected_plot_color, which='both')

        ax22.plot(data.index, data[.5], color=infected_plot_color,  linewidth=sub_lw)
        ax22.tick_params(axis='y', colors=infected_plot_color,which='both')
        
        ax21.set_yscale('log')
        ax21.yaxis.set_major_formatter(ticker.ScalarFormatter())
        ax21.yaxis.set_minor_formatter(ticker.NullFormatter())
        ax22.set_yscale('log')
        ax22.yaxis.set_major_formatter(ticker.ScalarFormatter())
        ax22.yaxis.set_minor_formatter(ticker.NullFormatter())
        
        
    
        data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_C580Y.csv'%(mda,pfpr,scenario), sep=',', header=None)
        data = data.fillna(0)
        data = data.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T        
        data.index = dates
#        ax[idx,1].fill_between(data.index, data[.25], data[.75], alpha=.2)
        ax[idx,1].plot(data.index, data[.5], linewidth=main_lw)
        
        
        
#        else:
#            ax2.plot(data.index, data[.5],'--')
    
        data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_plas.csv'%(mda,pfpr,scenario), sep=',', header=None)
        data = data.fillna(0)
        data = data.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T
        data.index = dates
        #        ax[idx,1].fill_between(data.index, data[.25], data[.75], alpha=.2)
        ax[idx,2].plot(data.index, data[.5], linewidth=main_lw)
    
    ax[idx,0].text(dt.date(2020, 6, 1), 2.25, figure_index[idx*3], fontsize=25, weight='bold')
    ax[idx,1].text(dt.date(2020, 6, 1), 0.45, figure_index[idx*3+1],fontsize=25, weight='bold')
    ax[idx,2].text(dt.date(2020, 6, 1), 0.45, figure_index[idx*3+2], fontsize=25, weight='bold')
    
    
    
    ax[idx,0].set_ylim(0, 2.5)
    ax[idx,0].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))
#    ax[idx,0].grid(True)
    ax[idx,0].tick_params(axis='both', which='both')
    ax[idx,0].yaxis.set_major_locator(plt.MaxNLocator(3))
    ax[idx,0].yaxis.set_major_formatter(ticker.PercentFormatter(decimals= 0))
#    ax[idx,0].set_ylabel(r'$PFPR_{2-10}$',fontsize= fs)
 
    ax[idx,1].set_ylim(0.0001, 1)
    ax[idx,1].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))  
    ax[idx,1].set_yscale('log')
    ax[idx,1].tick_params(axis='y', which='both')
    ax[idx,1].yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax[idx,1].yaxis.set_minor_formatter(ticker.NullFormatter())
#    ax[idx,1].set_ylabel('580Y Frequency',fontsize= fs)
 
    ax[idx,2].set_ylim(0.0001, 1)
    ax[idx,2].set_xlim(dt.date(2020, 1, 1), dt.date(2042, 1, 1))    
    ax[idx,2].set_yscale('log')
    ax[idx,2].tick_params(axis='y', which='both')
    ax[idx,2].yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax[idx,2].yaxis.set_minor_formatter(ticker.NullFormatter())    
    
    ax21.grid(False)
    ax22.grid(False)
    ax21.set_ylim(1, 10000)
#        ax21.yaxis.set_ticks(np.arange(0, 4000, 1000))
    ax22.set_ylim(1, 10000)
    ax21.yaxis.set_ticks([1, 10, 100, 1000, 10000])
    ax22.yaxis.set_ticks([1, 10, 100, 1000, 10000])
    
    
    
    
    if(idx>=3):
        ax[idx,0].set_xlabel('YEAR')
        ax[idx,1].set_xlabel('YEAR')
        ax[idx,2].set_xlabel('YEAR')
    else:
        ax[idx,0].set_xticklabels('')
        ax[idx,1].set_xticklabels('')
        ax[idx,2].set_xticklabels('')

    if (idx ==0):
        ax[idx,0].set_title(r'$PfPR_{2-10}$')
#        ax[idx,0].set_title('PfPR_2-10')
        ax[idx,1].set_title('ALLELE FREQUENCY OF 580Y')        
        ax[idx,2].set_title('GENOTYPE FREQUENCY OF\n DOUBLE-COPY PLASMEPSIN')
        
    ax[idx,0].set_ylabel(y_labels[idx],linespacing=1.5)
    
        
    ### This part modify default axis tick label and others
    # IMPORTANT: We need to draw the canvas, otherwise the labels won't be positioned and 
    # won't have values yet.
    fig.canvas.draw()
    
    # remove ytick label 0 for infected individuals plot
#    labels = [item.get_text() for item in ax21.get_yticklabels()]
#    labels[0] = ''
#
#    ax21.set_yticklabels(labels)
#    ax22.set_yticklabels(labels)
    
    #remove year 2040 tick label
    dr = pd.date_range(start= "1 1 2022", end= "1 1 2041", freq="5YS")
    ax[idx,0].set_xticks(dr)
    ax[idx,1].set_xticks(dr)
    ax[idx,2].set_xticks(dr)
    if(idx==3):
        ax[idx,0].set_xticklabels(range(2022,2041,5))
        ax[idx,1].set_xticklabels(range(2022,2041,5))
        ax[idx,2].set_xticklabels(range(2022,2041,5))

#         xtick_labels = [item.get_text() for item in ax[idx,0].get_xticklabels()]
#         xtick_labels[6] = ''
# #        print(xtick_labels)
#         ax[idx,0].set_xticklabels(xtick_labels)
#         ax[idx,1].set_xticklabels(xtick_labels)
#         ax[idx,2].set_xticklabels(xtick_labels)
        
    # remove ytick label 0 for PFPR plot
    ytick_labels =  [item.get_text() for item in ax[idx,0].get_yticklabels()]
    ytick_labels[0] = ''
#    print(ytick_labels)
    ax[idx,0].set_yticklabels(ytick_labels)
    
    # remove ytick label 0 for frequency plot
    ytick_labels =  [item.get_text() for item in ax[idx,1].get_yticklabels()]
    ytick_labels[1] = ''
#    print(ytick_labels)
    ax[idx,1].set_yticklabels(ytick_labels)
    ax[idx,2].set_yticklabels(ytick_labels)

sns.set_style("white", {'axes.spines.bottom': False,
 'axes.spines.left': False,
 'axes.spines.right': False,
 'axes.spines.top': False })
axx= fig.add_subplot(111, frameon=False)
axx.get_xaxis().set_visible(False)
axx.get_yaxis().set_ticks([])

plt.grid(False)
axx.set_ylabel('NUMBER OF POSITIVE INIDIVIDUALS\nANY LEVEL OF PARASITEAMIA',labelpad=100, 
               color=infected_plot_color,linespacing=1.5)
axx.yaxis.set_label_position("right")
