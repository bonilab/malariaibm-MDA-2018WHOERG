# -*- coding: utf-8 -*-


#%%
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.lines import Line2D


fs = 10
font = {'weight' : 'normal',
        'size'   : fs }

matplotlib.rc('font', **font)
#matplotlib.rcParams['axes.unicode_minus'] = False
sns.set(font_scale=0.8)
sns.set_style("whitegrid", {'ytick.left': True })

palette = sns.color_palette()[0:5]

#%%
#plot 40k
import matplotlib.ticker as ticker
from matplotlib.collections import PathCollection


sns.set(font_scale=3.2)
sns.set_style("whitegrid", {'ytick.left': True })
matplotlib.rc('font', **font)
matplotlib.rc('text', usetex = False)
plt.rc('text', usetex=False)

dpi=72
fig_w = 3240/dpi
fig_h = fig_w*8/12

plt.close('all')
fig, ax = plt.subplots(2,1, figsize=(fig_w, fig_h),tight_layout=True)  

mdas = [0,1,2,3,4]
pfprs = [1]
itcs = [0, 0.65, 0.7, 0.75, 0.8]
itcs_value = ['','0p65', '0p7', '0p75', '0p8']

list_ = []

dot_size = 12
annotation_text_size = 36

for pfpr in pfprs:
    for itc_i, itc in enumerate(itcs):
        for mda in mdas:
            if(itc_i ==0):
                data_raw= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_pfpr.csv'%(mda,pfpr), sep=',', header=None)    
                data_positive= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_positive.csv'%(mda,pfpr), sep=',', header=None)    
            else:
                data_raw= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_itc_%s_pfpr.csv'%(mda,pfpr,itcs_value[itc_i]), sep=',', header=None)
                data_positive= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_itc_%s_positive.csv'%(mda,pfpr,itcs_value[itc_i]), sep=',', header=None)    

            data = pd.DataFrame()
            data['pfpr2025']=data_raw.iloc[229,:]            
            data['positive']=data_positive.T.iloc[229,:]
            data['mda'] = mda
            data['itc'] = itc
            list_.append(data)

all_pfpr2025 = pd.concat(list_)
all_pfpr2025['log_pfpr2025'] = np.log10(all_pfpr2025['pfpr2025']+0.0001);



#sns.violinplot(x="itc", y="log_pfpr2025",hue="mda" , data=all_pfpr2025, palette="muted",inner=None, ax=ax[0])
ax1 = sns.boxplot(x="itc", y="pfpr2025",hue="mda" , 
                  data=all_pfpr2025, showfliers=False,
                  boxprops={ "zorder":10},
                  whis=0,ax = ax[0])

# Add transparency to colors
for patch in ax1.patches:
    fc = patch.get_facecolor()
    patch.set_facecolor(matplotlib.colors.to_rgba(fc, 0.3))

ax1.set_yscale('log')
ax1.tick_params(axis='both', which='both')
ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:0.3f}%"))
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())

ax1.set_ylim([0.0005, 1.0])

ax2=sns.stripplot(x="itc", y="pfpr2025", hue="mda", 
                  data=all_pfpr2025, jitter=True, dodge= True, 
                  size=dot_size, alpha=0.75, ax = ax[0])
for artist in ax2.findobj(PathCollection):
    artist.set_zorder(1)

#yposlist = (all_pfpr2025.groupby(['itc','mda'])['pfpr2025'].max()+0.001).tolist()
#xposlist = [ -0.34,-0.17, 0 ,0.17, 0.34 ] + np.linspace(1-0.34,1.36,5).tolist() + np.linspace(2-0.34,2.36,5).tolist() + np.linspace(3-0.34,3.36,5).tolist()+ np.linspace(4-0.34,4.36,5).tolist()

labels = [item.get_text() for item in ax[0].get_xticklabels()]
labels[0] = 'NO ITC'

ax1.set
ax[0].set_xticklabels(labels)
#custom_lines = [Line2D([0], [0], color=palette[0], lw=4),
#                Line2D([0], [0], color=palette[1], lw=4),
#                Line2D([0], [0], color=palette[2], lw=4),
#                Line2D([0], [0], color=palette[3], lw=4),
#                Line2D([0], [0], color=palette[4], lw=4),
#                ]
#ax[0].legend(custom_lines, ['0', '1', '2','3','4'], title="# of MDA rounds", loc="upper right", ncol=2)
ax[0].legend_.remove()
ax[0].set_xlabel('')
ax[0].set_ylabel('40k\n'+'$\mathit{PfPR}_{2\u221210}}$ at year 5', multialignment='center')

count_cases_lt_100_40k = all_pfpr2025.groupby(['itc','mda'])[['positive']].apply(lambda x: x[x <100].count())


quantile = all_pfpr2025.groupby(['itc','mda'])[['pfpr2025']].quantile(0.25)
quantile.reset_index(level=[0,1], inplace=True)
for tick in range(len(ax1.get_xticklabels())):
    # print(tick)
    for ind in range(0,5):
        # print(ind)
        if count_cases_lt_100_40k.iloc[tick*5+ind][0] > 0:
            ax2.text(tick+0.16*(ind-2), 0.007,
                     count_cases_lt_100_40k.iloc[tick*5+ind][0] , horizontalalignment='center',  
                     color='k', fontsize=annotation_text_size)


  #%%
#plot 300k

mdas = [0,1,2,3,4]
pfprs = [1]
itcs = [0, 0.65, 0.7, 0.75, 0.8]
itcs_value = ['','0p65', '0p7', '0p75', '0p8']

list_ = []

for pfpr in pfprs:
    for itc_i, itc in enumerate(itcs):
        for mda in mdas:
            if(itc_i ==0):
                data_raw= pd.read_csv('data\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_pfpr.csv'%(mda,pfpr), sep=',', header=None)    
                data_positive= pd.read_csv('data\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_positive.csv'%(mda,pfpr), sep=',', header=None)    
            else:
                data_raw= pd.read_csv('data\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_itc_%s_pfpr.csv'%(mda,pfpr,itcs_value[itc_i]), sep=',', header=None)
                data_positive= pd.read_csv('data\ONELOC_300k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL_itc_%s_positive.csv'%(mda,pfpr,itcs_value[itc_i]), sep=',', header=None)    

            data = pd.DataFrame()
            data['pfpr2025']=data_raw.iloc[229,:]      
            data['positive']=data_positive.T.iloc[229,:]

            data['mda'] = mda
            data['itc'] = itc
            list_.append(data)

all_pfpr2025 = pd.concat(list_)
all_pfpr2025['log_pfpr2025'] = np.log10(all_pfpr2025['pfpr2025']+0.0001);

#sns.violinplot(x="itc", y="log_pfpr2025",hue="mda" , data=all_pfpr2025, palette="muted",inner=None, ax=ax[0])
ax1 = sns.boxplot(x="itc", y="pfpr2025",hue="mda" , data=all_pfpr2025,showfliers=False,boxprops={ "zorder":10}, whis=0,ax = ax[1])

# Add transparency to colors
for patch in ax1.patches:
    r, g, b, a = patch.get_facecolor()
    patch.set_facecolor((r, g, b,0.2))

ax1.set_yscale('log')
ax1.tick_params(axis='both', which='both')
ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:0.3f}%"))
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())
ax1.set_ylim([0.0005, 1.0])

ax2=sns.stripplot(x="itc", y="pfpr2025", hue="mda", data=all_pfpr2025, jitter=True, dodge= True, size=dot_size, alpha=0.75, ax = ax[1])
for artist in ax2.findobj(PathCollection):
    artist.set_zorder(1)
    
#    
#sns.violinplot(x="itc", y="log_pfpr2025",hue="mda" , data=all_pfpr2025, palette="muted",inner=None, ax = ax[1])
#sns.stripplot(x="itc", y="log_pfpr2025", hue="mda", data=all_pfpr2025, jitter=0.2, dodge= True, color='black', alpha=.3, ax = ax[1])
#
#
#yposlist = (all_pfpr2025.groupby(['itc','mda'])['pfpr2025'].max()+0.001).tolist()
#xposlist = [ -0.34,-0.17, 0 ,0.17, 0.34 ] + np.linspace(1-0.34,1.36,5).tolist() + np.linspace(2-0.34,2.36,5).tolist() + np.linspace(3-0.34,3.36,5).tolist()+ np.linspace(4-0.34,4.36,5).tolist()
#
#ax[1].set_ylabel('Log10 PFPR 2030 (%)')

labels = [item.get_text() for item in ax[1].get_xticklabels()]
labels[0] = 'NO ITC'

ax[1].set_xticklabels(labels)


custom_lines = [Line2D([0], [0], color=palette[0], lw=4),
                Line2D([0], [0], color=palette[1], lw=4),
                Line2D([0], [0], color=palette[2], lw=4),
                Line2D([0], [0], color=palette[3], lw=4),
                Line2D([0], [0], color=palette[4], lw=4),
                ]


ax[1].legend(custom_lines, ['0', '1', '2','3','4'], title="# of MDA rounds", ncol=2)
ax[1].set_ylabel('300k\n'+'$\mathit{PfPR}_{2\u221210}}$ at year 5', multialignment='center')
ax[1].set_xlabel('TREATMENT COVERAGE POST-MDA')

count_cases_lt_100_300k = all_pfpr2025.groupby(['itc','mda'])[['positive']].apply(lambda x: x[x <100].count())


quantile = all_pfpr2025.groupby(['itc','mda'])[['pfpr2025']].quantile(0.25)
quantile.reset_index(level=[0,1], inplace=True)
for tick in range(len(ax1.get_xticklabels())):
    # print(tick)
    for ind in range(0,5):
        # print(ind)
        if count_cases_lt_100_300k.iloc[tick*5+ind][0] > 0:
            ax2.text(tick+0.16*(ind-2), 0.00085,
                     count_cases_lt_100_300k.iloc[tick*5+ind][0] , horizontalalignment='center',  
                     color='k', fontsize=annotation_text_size)



