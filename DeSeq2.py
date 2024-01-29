
import pandas as pd
import scanpy as sc
import numpy as np
from pydeseq2.default_inference import DefaultInference
from sanbomics.plots import volcano
import seaborn as sns
import matplotlib.pyplot as plt  # Import matplotlib for plotting
# from sanbomics.tools import id_map
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

# Load counts data from an Excel file (update the filename)
counts = pd.read_excel("BEZELYECOUNT.xlsx")

# Set geneid as the index and filter out rows with zero counts
counts = counts.set_index("geneid")
counts = counts[counts.sum(axis=1) > 0]

# Transpose the counts data for DESeq2 analysis
tcounts = counts.T

# Create metadata based on sample names and conditions
metadata = pd.DataFrame(zip(tcounts.index, ["C", "C", "T", "T"]), columns=["Sample", "Condition"])
metadata = metadata.set_index("Sample")

# Initialize DESeq2 dataset
inference = DefaultInference(n_cpus=4)
dds = DeseqDataSet(
    counts=tcounts,
    metadata=metadata,
    design_factors="Condition",  # compare samples based on the "condition"
    refit_cooks=True,
    inference=inference,
)

# Fit DESeq2 model and perform differential expression analysis
dds.fit_size_factors()
dds.fit_genewise_dispersions()
dds.fit_dispersion_trend()
dds.fit_dispersion_prior()
print(f"logres_prior={dds.uns['_squared_logres']}, sigma_prior={dds.uns['prior_disp_var']}")
dds.fit_MAP_dispersions()
dds.fit_LFC()
dds.calculate_cooks()

# Refit model if needed
if dds.refit_cooks:
    dds.refit()

# Summarize DESeq2 analysis results
stat_res = DeseqStats(dds, alpha=0.05, cooks_filter=True, independent_filter=True)
stat_res.summary()
res = stat_res.results_df
table = stat_res.results_df
table.to_csv('deseq.csv')

# Perform additional analysis and visualization
dds.layers["log1p"] = np.log1p(dds.layers["normed_counts"])
sigs = res[(res.padj < 0.05) & (abs(res.log2FoldChange) > 0.5)]
dds_sigs = dds[:, sigs.index]
grapher = pd.DataFrame(dds_sigs.layers['log1p'].T, index=dds_sigs.var_names, columns=dds_sigs.obs_names)

# Generate a clustermap of the selected genes
sns.clustermap(grapher, z_score=18, cmap='RdYlBu_r')

# Perform PCA and visualize the results
sc.tl.pca(dds)
stat_res.lfc_shrink(coeff="Condition_T_vs_C")
sc.pl.pca(dds, color="Condition", size=200)

# Create and display a volcano plot
volcano(res, symbol='Condition_T_vs_C', log2fc='log2FoldChange')
plt.show()
