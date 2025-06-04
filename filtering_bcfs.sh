# script for filtering bcf files from the switchgrass diversity panel
# these genotype files were initially processed by Paulo 

# setting directory where bcfs are stored & where the filtered genotype files will go
bcfDir="/path/to/bcfs"
outDir="path/to/filtered/bcfs"

mkdir outDir

cd outDir

# filter by quality

# filter by depth

# filter by missingness 

# delete intermediate files 

# convert to .012 format (simple genotype matrix for mapping eQTLs)