# quick script to convert AP13 gff3 file to gtf, for runnign STAR

module purge
module load gffread/0.12.7-GCCcore-12.3.0

gffread /mnt/scratch/bergcole/referenceGenome/Pvirgatum_AP13.gff3 -T -o /mnt/scratch/bergcole/referenceGenome/AP13.gtf
