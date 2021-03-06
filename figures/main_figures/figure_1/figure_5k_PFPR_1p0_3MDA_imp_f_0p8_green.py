# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:03:19 2018

@author: NguyenTran
"""

#%%
import pandas as pd
import numpy as np

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
    fig_h = fig_w*16/9
    
    fig, ax = plt.subplots( 1, 1,figsize=(fig_w,fig_h),tight_layout=True, sharex=True)  
    
    year_from = 2021
    year_to = 2027
    
    x_from = '%s-01-01'%year_from
    x_to = '%s-01-01'%year_to


    years = mdates.YearLocator()   # every year
    years_fmt = mdates.DateFormatter('%Y')
    # months = mdates.MonthLocator()  # every month

         

    data_positive= pd.read_csv('data\ONELOC_5k_%dRMDA_PFPR%s_OPPUNIFORM_FLAL%s_positive_f_0p8.csv'%(mda,pfpr_str,scenario ), sep=',', header=None)
        
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
    ax.set_xlim(x_from, x_to)
    ax.set_yscale('log')
    ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
    ax.yaxis.set_minor_formatter(ticker.NullFormatter())
    
    
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)

    # plt.setp(ax2[i_mda].xaxis.get_majorticklabels(), rotation=60 , ha="center")
    plt.setp(ax.xaxis.get_ticklabels()[0], visible=False)
    
    # for label in ax2[i_mda].xaxis.get_ticklabels()[::2]:
    #     label.set_visible(False)
    
    
    ax.set_ylabel('Num Pos Indivs', fontsize=75)
    
    fig = plt.gcf()
    # fig.suptitle('5k Population - PfPR %0.2f%% - %s'%(pfpr,scenario_str))
    fig.autofmt_xdate()
    
    
    # ax.legend(np.round( np.arange(0.1,1,0.1), 2), loc='center left', bbox_to_anchor=(1, 0.5))     
    
    return fig

#%%
palette = sns.color_palette()
plt.close('all')

pfprs = {    
    1.0: '1p0'
    }

mdas = [3]
scenarios = {
    # "": "no importation",      
    "_imp": "import 1 case per 100 days", 
   # "_itc": "itc 65%", 
   # "_itc_imp": "import 1 case per 100 days - itc 65%", 
}



# make_plot(0.5,"0p5", "", "no importation", 3)

# make_plot(0.5,"0p5", "_imp", "import 1 case per 100 days", 3)


figs = []
for pfpr, pfpr_str in pfprs.items():
    for scenario, scenario_str in scenarios.items():
        for mda in mdas:
            fig = make_plot(pfpr,pfpr_str, scenario, scenario_str,mda)            
            figs.append(fig)
    

#%%
# i=0
# for pfpr, pfpr_str in pfprs.items():
#     for scenario, scenario_str in scenarios.items():
#         for mda in mdas:
#             figs[i].savefig('pos_indivs_5k_PFPR%s_%dMDA%s_f_0p8.pdf'%(pfpr_str, mda,scenario))
#             i+=1
        
# plt.close('all')


