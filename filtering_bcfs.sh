# script for filtering bcf files from the switchgrass diversity panel
# these genotype files were initially processed by Paulo 

# setting directory where bcfs are stored & where the filtered genotype files will go
bcfDir="/mnt/research/glbrc_group/lowry_lab/WGS/genotyping_pi/population_L/chr_level/"
outDir="/mnt/scratch/bergcole/filtered_switchgrass_genotypes"

mkdir outDir

cd outDir

# filter to only keep indvs with Texas RNASeq data

bcftools view -Ou -S TX_keep.txt ${bcfDir}/Chr01K_pop.vcf.gz > ${outDir}/Chr01K_TX_keep.bcf 

# filter to only keep indvs with Michigan RNASeq data 

bcftools view -Ou -S MI_keep.txt ${bcfDir}/Chr01K_pop.vcf.gz > ${outDir}/Chr01K_TX_keep.bcf 



# filter to only keep indvs with Michigan RNASeq data 

# filter by quality

bcftools view -i 'QUAL>=29' ${bcfDir}/Chr01K_pop.vcf.gz > ${outDir}/Chr01K_biallelic_snps_qualFilt.bcf

# filter by depth

bcftools view  -i  'MIN(FMT/DP>8) & MIN(FMT/DP<500)' ${outDir}/Chr01K_biallelic_snps_qualFilt.bcf > ${outDir}/Chr01K_biallelic_snps_depthFilt.bcf

# filter by missingness 

bcftools view -i 'F_MISSING<0.1'  ${outDir}/Chr01K_biallelic_snps_depthFilt.bcf > ${outDir}/Chr01K_biallelic_snps_missingFilt.bcf

# filter by minor allele frequency 

bcftools view -q 0.005:minor ${outDir}/Chr01K_biallelic_snps_missingFilt.bcf > ${outDir}/Chr01K_biallelic_snps_filtered.bcf

# delete intermediate files 
rm ${outDir}/Chr01K_biallelic_snps_qualFilt.bcf
rm ${outDir}/Chr01K_biallelic_snps_depthFilt.bcf
rm ${outDir}/Chr01K_biallelic_snps_missingFilt.bcf

# convert to .012 format (simple genotype matrix for mapping eQTLs)