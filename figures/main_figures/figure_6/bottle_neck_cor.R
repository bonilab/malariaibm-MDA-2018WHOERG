# read data ---------------------------------------------------------------
result =  data.frame()
for (mda in 0:4) {
  print(mda)
  # 
  # paramspace =  read.csv(
  #   file = sprintf('SA3_paramspace_%d.csv', mda))
  # 
  # paramspace$mda = mda
  # paramspace = head(paramspace, 10000)
  output = read.csv(sprintf('%d\\data\\bottle_neck_data.csv',mda), header = FALSE)
  
  # temp = cbind(paramspace, output['V6'])
  result = rbind(result, output)
}

result[is.na(result)] = 0


# extract 2030 data
c_names = c ("2023", "2024", "2025", "2026", "2027", "2028", "bottle neck sizes" )

library(plyr)
result = rename(result , c ("V1"="y2023","V2"= "y2024", "V3" = "y2025", 
                            "V4" = "y2026","V5" = "y2027", "V6" = "y2028", 
                            "V7" = "y2029","V8" = "y2030", 
                            "V9" = "bottle neck sizes" ))
result$`log bottle neck sizes` = log10(result$`bottle neck sizes` + 0.001)

cor(result[1:6], result[7],  use="complete.obs", method="pearson")

cor.test(result$`bottle neck sizes`, result$y2027)

library(Hmisc)
# rcorr(result, type="pearson")

library("ggpubr")
library(grid)

year = "y2024"

d1 = result[(result['bottle neck sizes'] <= 100) & (result[year] > 0.5), ]
d2 = result[(result['bottle neck sizes'] > 100) & (result[year] >  0.5), ]
d3 = result[(result['bottle neck sizes'] <= 100) & (result[year] <= 0.5), ]
d4 = result[(result['bottle neck sizes'] > 100) & (result[year] <= 0.5), ]

grob1 <- grobTree(textGrob(nrow(d1), x=0.1,  y=0.95, hjust=0,
                          gp=gpar(col="red", fontsize=16)))

grob2 <- grobTree(textGrob(nrow(d2), x=0.75,  y=0.95, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob3 <- grobTree(textGrob(nrow(d3), x=0.1,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob4 <- grobTree(textGrob(nrow(d4), x=0.75,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))


p1 = ggscatter(result, x = "bottle neck sizes", y = "y2024",
          color = "black", shape = 20, size = 2,
          add = "none", 
          # conf.int = TRUE, cor.coef = FALSE, cor.method = "pearson",
          xlab = "Bottleneck Size", ylab = "580Y Freq at 2024", log="bottle neck sizes") + 
  xscale("log10") + 
  geom_vline(xintercept = 100, color="red", size = 1.5) + 
  geom_hline(yintercept = 0.5, color="red", size = 1.5) + 
  annotation_custom(grob1) +
  annotation_custom(grob2) +
  annotation_custom(grob3) +
  annotation_custom(grob4) 

###############
year = "y2027"

d1 = result[(result['bottle neck sizes'] <= 100) & (result[year] > 0.5), ]
d2 = result[(result['bottle neck sizes'] > 100) & (result[year] >  0.5), ]
d3 = result[(result['bottle neck sizes'] <= 100) & (result[year] <= 0.5), ]
d4 = result[(result['bottle neck sizes'] > 100) & (result[year] <= 0.5), ]

grob1 <- grobTree(textGrob(nrow(d1), x=0.1,  y=0.95, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob2 <- grobTree(textGrob(nrow(d2), x=0.75,  y=0.95, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob3 <- grobTree(textGrob(nrow(d3), x=0.1,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob4 <- grobTree(textGrob(nrow(d4), x=0.75,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))


p2 = ggscatter(result, x = "bottle neck sizes", y = "y2027",
               color = "black", shape = 20, size = 2,
               add = "none", 
               # conf.int = TRUE, cor.coef = FALSE, cor.method = "pearson",
               xlab = "Bottleneck Size", ylab = "580Y Freq at 2027", log="bottle neck sizes") + 
  xscale("log10") + 
  geom_vline(xintercept = 100, color="red", size = 1.5) + 
  geom_hline(yintercept = 0.5, color="red", size = 1.5) + 
  annotation_custom(grob1) +
  annotation_custom(grob2) +
  annotation_custom(grob3) +
  annotation_custom(grob4) 

########
year = "y2030"

d1 = result[(result['bottle neck sizes'] <= 100) & (result[year] > 0.5), ]
d2 = result[(result['bottle neck sizes'] > 100) & (result[year] >  0.5), ]
d3 = result[(result['bottle neck sizes'] <= 100) & (result[year] <= 0.5), ]
d4 = result[(result['bottle neck sizes'] > 100) & (result[year] <= 0.5), ]

grob1 <- grobTree(textGrob(nrow(d1), x=0.1,  y=0.95, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob2 <- grobTree(textGrob(nrow(d2), x=0.75,  y=0.95, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob3 <- grobTree(textGrob(nrow(d3), x=0.1,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))

grob4 <- grobTree(textGrob(nrow(d4), x=0.75,  y=0.1, hjust=0,
                           gp=gpar(col="red", fontsize=16)))


p3 = ggscatter(result, x = "bottle neck sizes", y = "y2030",
               color = "black", shape = 20, size = 2,
               add = "none", 
               # conf.int = TRUE, cor.coef = FALSE, cor.method = "pearson",
               xlab = "Bottleneck Size", ylab = "580Y Freq at 2030", log="bottle neck sizes") + 
  xscale("log10") + 
  geom_vline(xintercept = 100, color="red", size = 1.5) + 
  geom_hline(yintercept = 0.5, color="red", size = 1.5) + 
  annotation_custom(grob1) +
  annotation_custom(grob2) +
  annotation_custom(grob3) +
  annotation_custom(grob4) 

ggarrange(p1+ rremove("xlab"), p2+ rremove("xlab"), p3, ncol = 1, nrow = 3,
          common.legend = TRUE, legend = "bottom")
# ggpar(p,ylim= c(0,1) )




# 
# p1 = ggscatter(d1, x = "bottle neck sizes", y = year, 
#           add = "reg.line", conf.int = TRUE, 
#           cor.coef = TRUE, cor.method = "pearson",
#           xlab = "Bottleneck Size", ylab = "580Y Freq at 2027") + xscale("log10")
# 
# p2 = ggscatter(d2, x = "bottle neck sizes", y = year, 
#                add = "reg.line", conf.int = TRUE, 
#                cor.coef = TRUE, cor.method = "pearson",
#                xlab = "", ylab = "580Y Freq at 2027") + xscale("log10")
# p3 = ggscatter(d3, x = "bottle neck sizes", y = year, 
#                add = "reg.line", conf.int = TRUE, 
#                cor.coef = TRUE, cor.method = "pearson", cor.coef.coord = c(3.5, 0.48),
#                xlab = "Bottleneck Size", ylab = "580Y Freq at 2027",xlim=c(100,20000)) + xscale("log10") 
# p4 = ggscatter(d4, x = "bottle neck sizes", y = year, 
#                add = "reg.line", conf.int = TRUE, 
#                cor.coef = TRUE, cor.method = "pearson", cor.coef.coord = c(3.0, 0.95),
#                xlab = "", ylab = "", xlim= c(100,20000)) + xscale("log10")
# # + rremove("y.text") + rremove("x.text") 
# 
# ggarrange(p2, p4, p1, p3, ncol = 2, nrow = 2)


# plot(result$`bottle neck sizes`, result$`2023`, pch=19)
