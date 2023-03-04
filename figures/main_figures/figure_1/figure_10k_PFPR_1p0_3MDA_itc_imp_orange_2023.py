# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:03:19 2018

@author: NguyenTran
"""

#%%
import pandas as pd
import numpy as np
import datetime as dt


import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

import matplotlib.ticker as ticker

fs = 12
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : fs }

matplotlib.rc('font', **font)
plt.rc('text', usetex=False)

sns.set( font_scale=6)
sns.set_style("whitegrid", {'ytick.left': True })

dates = pd.date_range(start= "1 1 2008", end= "1 1 2042", freq="MS")

def make_plot(pfpr, pfpr_str, scenario, scenario_str, mda):     
    import matplotlib.dates as mdates
    
    main_lw = 6    
    dpi=72
    fig_w = 2*1080/dpi
    fig_h = fig_w*10.0/16.0
    
    fig, ax = plt.subplots( 1, 1,figsize=(fig_w,fig_h),tight_layout=True, sharex=True)  


    years = mdates.YearLocator()   # every year
    years_fmt = mdates.DateFormatter('%Y')
    # months = mdates.MonthLocator()  # every month

    data_positive= pd.read_csv('data\ONELOC_10k_%dRMDA_PFPR%s_OPPUNIFORM_FLAL%s_positive.csv'%(mda,pfpr_str,scenario ), sep=',', header=None)
    data_positive.index = dates
    
    quantile_positive = data_positive.quantile(np.round(np.arange(0.1,1,0.1),2), axis=1).T.reset_index(drop=True)
    
    for c in quantile_positive.columns:
        # first = next((x for x in quantile_positive[c] if x <=5), 0)
        found_id = np.where(quantile_positive[c]<=5)
        if len(found_id[0]) >0:
            ax.scatter(dates[found_id[0][0]],quantile_positive[c][found_id[0][0]],s=800, marker='s', color='k')
            quantile_positive[c][found_id[0][0]+1:] = None
      
    
    ax.plot(data_positive.index, quantile_positive, linewidth=main_lw, color='k')            
    
    ax.set_ylim(1, 500)
    ax.set_xlim(dt.date(2021, 1, 1), dt.date(2027, 1, 1))
    
    ax.set_yscale('log')
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(ticker.NullFormatter())
    
    
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_ticklabels(range(-1,6), rotation=0, ha="center")

    # plt.setp(ax2[i_mda].xaxis.get_majorticklabels(), rotation=60 , ha="center")
    plt.setp(ax.xaxis.get_ticklabels()[0], visible=False)
    
    # for label in ax2[i_mda].xaxis.get_ticklabels()[::2]:
    #     label.set_visible(False)
    
    
    ax.set_ylabel('Num Pos Indivs', fontsize=75)
    
    fig = plt.gcf()
    # fig.suptitle('10k Population - PfPR %0.2f%% - %s'%(pfpr,scenario_str))
    
    
    
    # ax.legend(np.round( np.arange(0.1,1,0.1), 2), loc='center left', bbox_to_anchor=(1, 0.5))     
    
    return fig

#%%
palette = sns.color_palette()
plt.close('all')

pfprs = {    
    0.5: '0p5'
    }

mdas = [3]
scenarios = {
    # "": "no importation",      
    # "_imp": "import 1 case per 100 days", 
   # "_itc": "itc 65%", 
    "_itc_imp": "import 1 case per 100 days - itc 65%", 
}

figs = []
for pfpr, pfpr_str in pfprs.items():
    for scenario, scenario_str in scenarios.items():
        for mda in mdas:
            figs.append(make_plot(pfpr,pfpr_str, scenario, scenario_str,mda))


fig = plt.gcf()
fig.savefig("orange.pdf")

#%%
# i=0
# for pfpr, pfpr_str in pfprs.items():
#     for scenario, scenario_str in scenarios.items():
#         for mda in mdas:
#             figs[i].savefig('pos_indivs_10k_PFPR%s_%dMDA%s.pdf'%(pfpr_str, mda,scenario))
#             i+=1
        
# plt.close('all')        