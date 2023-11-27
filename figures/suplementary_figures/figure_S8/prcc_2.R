# read data ---------------------------------------------------------------
result =  data.frame()
for (mda in 0:4) {
  print(mda)
  
  paramspace =  read.csv(
    file = sprintf('SA3_paramspace_%d.csv', mda))
  
  paramspace$mda = mda
  paramspace = head(paramspace, 10000)
  output = read.csv(sprintf('%d\\data\\time_580Y_reach_x.csv',mda), header = FALSE)
  
  temp = cbind(paramspace, output['V5']
  )
  result = rbind(result, temp)
}



# prcc --------------------------------------------------------------------

library(epiR)
r1 = result

# r1 = result[ result$mda_coverage > 0.8, ]

# r1 = r1[-7]

# plot(r1$mda_coverage, r1$V6)


prcc_res = epi.prcc(r1, sided.test = 2, conf.level = 0.95)
c_names = c ("Population Size", "PfPR", "Importation Rate of\nDrug Resistance", "Level of Improved\nTreatment Coverage", 
             "Cost of Drug Resistance", "MDA Coverage", "Number of MDA Rounds" )
prcc_res = cbind(prcc_res, varname = c_names)
prcc_res = prcc_res[order(-abs(prcc_res$est)),]

# plot --------------------------------------------------------------------
# Increase margin size
# par(mar=c(10,10,0,0))
# par(mar = c(0, 0, 0, 0))
par(mar = c(6.5, 10.5, 4.5, 1.5), mgp = c(5, 1, 0))

x<-barplot(prcc_res$est,
           horiz=TRUE,
           names.arg=prcc_res$varname,
           # axes = FALSE,  
           # space = 0,         
           # col = c("darkgreen", "red"),
           xlim = c(-0.6, 0.6),
           ylim = c(7, 0),
           axes=FALSE, 
           las = 1,
           xlab = expression('Partial Rank Correlation Coefficient with T'[.25])
)

tx_offset = 0.045
prcc_res$x_pos = with(prcc_res, ifelse(est < 0, est - tx_offset, est + tx_offset))
text(prcc_res$x_pos, x , sprintf("%.2f",prcc_res$est) ,cex=1)
axis(3)

