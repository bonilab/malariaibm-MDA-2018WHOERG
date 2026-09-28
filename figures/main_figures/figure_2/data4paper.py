# -*- coding: utf-8 -*-

#%%
# one round MDA\
import pandas as pd
import matplotlib.pyplot as plt

scenarios = [
    "",      
    "_imp", 
    "_itc", 
    "_itc_imp", 
        ]

pfpr = 2
mda =1
pfpr_all= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_pfpr.csv'%(mda,pfpr,scenarios[0] ), sep=',', header=None)




dates = pd.date_range(start= "1 1 2006", end= "1 1 2040", freq="MS")

pfpr_quantile = pfpr_all.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T                        
pfpr_quantile.index = dates

#plt.plot(pfpr_quantile[0.5])



#%%

# 4 round MDA\
import pandas as pd
import matplotlib.pyplot as plt

scenarios = [
    "",      
    "_imp", 
    "_itc", 
    "_itc_imp", 
        ]

pfpr = 2
mda =4
pfpr_all= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_pfpr.csv'%(mda,pfpr,scenarios[0] ), sep=',', header=None)




dates = pd.date_range(start= "1 1 2006", end= "1 1 2040", freq="MS")

pfpr_quantile = pfpr_all.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T                        
pfpr_quantile.index = dates

data= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_positive.csv'%(mda,pfpr,scenarios[0]), sep=',', header=None)
infected_quantile = data.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T        
infected_quantile.index = dates

#%%

pfpr = 2
mda= 2
pfpr_all= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_pfpr.csv'%(mda,pfpr,scenarios[0] ), sep=',', header=None)

pfpr_end = pfpr_all.tail(1)
print( pfpr_end.T[pfpr_end.T==0].count())

#%%
### Row 2


# 4 round MDA\
import pandas as pd
import matplotlib.pyplot as plt

scenarios = [
    "",      
    "_imp", 
    "_itc", 
    "_itc_imp", 
        ]

pfpr = 2
mda = 4
C580Y_all= pd.read_csv('data\ONELOC_40k_%dRMDA_PFPR%d_OPPUNIFORM_FLAL%s_C580Y.csv'%(mda,pfpr,scenarios[1] ), sep=',', header=None)
C580Y_all = C580Y_all.fillna(0)
dates = pd.date_range(start= "1 1 2006", end= "1 1 2040", freq="MS")

C580Y_quantile = C580Y_all.quantile([0.05, 0.25, 0.5, 0.75, 0.95], axis=1).T                        
C580Y_quantile.index = dates

print(C580Y_quantile[0.5][dates[216]])


