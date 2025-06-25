#!/bin/bash --login
# Job name:
#SBATCH --job-name=convert_bcfs
# Number of nodes
#SBATCH --nodes=1
#
# Number of tasks to run on each node
#SBATCH --ntasks-per-node=128
#
#
# Wall time (e.g. "minutes", "hours:minutes:seconds", "days-hours", "days-hours:minutes"):
#SBATCH --time=40:00:00
#
# Mail type:
#SBATCH --mail-type=ALL
#
# Mail user:
#SBATCH --mail-user=bergcole@msu.edu
#
# Standard out and error:
#SBATCH --output=%x-%j.SLURMout
#
# indicate that I'm using an array
#SBATCH --array=1-18

module purge
module load GCC/12.2.0 BCFtools/1.17

# call to the chromosome array
sampleID=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' chromosomes.array)

# setting the working directory
outDir="/mnt/scratch/bergcole/filtered_switchgrass_genotypes/99_filt"


bcftools convert -O v -o ${outDir}/${sampleID}_99_snps_stringent.bcf ${outDir}/${sampleID}Chr01K_99_snps.vcf 