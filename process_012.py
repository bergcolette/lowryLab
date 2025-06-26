# import relevant packages 
import numpy as np 
import pandas as pd

from pandas.api.types import is_string_dtype
from pandas.api.types import is_numeric_dtype

# set genotype directory
genDir="/mnt/scratch/bergcole/filtered_switchgrass_genotypes/filt_99"

# reading in indvs -- only need to do this once bc all chroms have the same individuals
indv = pd.read_csv(genDir+"/Chr01K_maf05.012.indv", sep="\t", header=None)

# Chr01K
gen = pd.read_csv(genDir+"/Chr01K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr01K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr01K_maf05.csv", index = None, sep = "\t")

# Chr01N
gen = pd.read_csv(genDir+"/Chr01N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr01N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr01N_maf05.csv", index = None, sep = "\t")

# Chr02K
gen = pd.read_csv(genDir+"/Chr02K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr02K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr02K_maf05.csv", index = None, sep = "\t")

# Chr02N
gen = pd.read_csv(genDir+"/Chr02N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr02N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr02N_maf05.csv", index = None, sep = "\t")

# Chr03K
gen = pd.read_csv(genDir+"/Chr03K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr03K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr03K_maf05.csv", index = None, sep = "\t")

# Chr03N
gen = pd.read_csv(genDir+"/Chr03N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr03N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr03N_maf05.csv", index = None, sep = "\t")

# Chr04K
gen = pd.read_csv(genDir+"/Chr04K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr04K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr04K_maf05.csv", index = None, sep = "\t")

# Chr04N
gen = pd.read_csv(genDir+"/Chr04N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr04N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr04N_maf05.csv", index = None, sep = "\t")

# Chr05K
gen = pd.read_csv(genDir+"/Chr05K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr05K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr05K_maf05.csv", index = None, sep = "\t")

# Chr05N
gen = pd.read_csv(genDir+"/Chr05N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr05N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr05N_maf05.csv", index = None, sep = "\t")

# Chr06K
gen = pd.read_csv(genDir+"/Chr06K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr06K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr06K_maf05.csv", index = None, sep = "\t")

# Chr06N
gen = pd.read_csv(genDir+"/Chr06N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr06N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr06N_maf05.csv", index = None, sep = "\t")

# Chr07K
gen = pd.read_csv(genDir+"/Chr07K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr07K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr07K_maf05.csv", index = None, sep = "\t")

# Chr07N
gen = pd.read_csv(genDir+"/Chr07N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr07N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr07N_maf05.csv", index = None, sep = "\t")

# Chr08K
gen = pd.read_csv(genDir+"/Chr08K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr08K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr08K_maf05.csv", index = None, sep = "\t")

# Chr08N
gen = pd.read_csv(genDir+"/Chr08N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr08N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr08N_maf05.csv", index = None, sep = "\t")

# Chr09K
gen = pd.read_csv(genDir+"/Chr09K_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr09K_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr09K_maf05.csv", index = None, sep = "\t")

# Chr09N
gen = pd.read_csv(genDir+"/Chr09N_maf05.012", sep="\t", header=None)
pos = pd.read_csv(genDir+"/Chr09N_maf05.012.pos", sep="\t", header=None)
pos.columns = ["Chrom", "Pos"]
pos['id'] = pos['Chrom'].astype(str) + ['_'] + pos['Pos'].astype(str)
gen_T = gen.T[1:].reset_index().iloc[:,1:]
gen_T.columns=indv[0]
pd.concat([pos.drop(columns=["Chrom", "Pos"]), gen_T], axis=1).to_csv(genDir+"/Chr09N_maf05.csv", index = None, sep = "\t")