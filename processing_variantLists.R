# loading required libraries

library(dplyr)
library(ggplot2)

# reading in data 

filt90 <- read.csv("~/scripts/lowryLab/positions_90_filt.txt", sep = "\t", header = FALSE)
filt95 <- read.csv("~/scripts/lowryLab/positions_95_filt.txt", sep = "\t", header = FALSE)
filt97.5 <- read.csv("~/scripts/lowryLab/positions_97.5_filt.txt", sep = "\t", header = FALSE)
filt99 <- read.csv("~/scripts/lowryLab/positions_99_filt.txt", sep = "\t", header = FALSE)
filt100 <- read.csv("~/scripts/lowryLab/positions_100_filt.txt", sep = "\t", header = FALSE)

# give the colnames
colnames(filt90) <- c("chrom", "pos")
colnames(filt95) <- c("chrom", "pos")
colnames(filt97.5) <- c("chrom", "pos")
colnames(filt99) <- c("chrom", "pos")
colnames(filt100) <- c("chrom", "pos")