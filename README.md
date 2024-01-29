# DESeq2 Analysis and Visualization

## Overview

This repository contains Python code for performing DESeq2 analysis and visualization using scanpy, seaborn, and pydeseq2. The analysis includes loading count data from an Excel file, differential expression analysis, generating a clustermap, performing principal component analysis (PCA), and creating a volcano plot.

## Requirements

Make sure you have the following dependencies installed:

- pandas
- scanpy
- numpy
- pydeseq2
- sanbomics
- seaborn
- matplotlib

You can install these dependencies using the following:

```bash
pip install pandas scanpy numpy pydeseq2 sanbomics seaborn matplotlib
```
## Usage
- Clone this repository:
```bash
  git clone https://github.com/RNA-Seq/RNA-Seq.git
  cd RNA-Seq
```
- Install the dependencies:
```bash
pip install -r requirements.txt
```
- Run the provided Python script:
```bash
python PyDeSeq2.py
```
This script performs DESeq2 analysis on the provided count data, generates visualizations, and saves results in a CSV file.

## Results
deseq.csv: CSV file containing the results of the DESeq2 analysis.
## Visualizations
- Clustermap: A heatmap of gene expression data, generated using seaborn.
- PCA Plot: A principal component analysis (PCA) plot, visualizing sample relationships.
- Volcano Plot: A volcano plot showing differentially expressed genes.
## Screenshots 
- ![Screenshot 2024-01-29 105833](https://github.com/gitdevutku/RNA-Seq/assets/144778146/7c86e450-eef1-44e3-b90b-65b10fa83b92)
-![Screenshot 2024-01-29 105810](https://github.com/gitdevutku/RNA-Seq/assets/144778146/dfb51d85-1522-41ae-9598-b6ad1e371255)
-![image](https://github.com/gitdevutku/RNA-Seq/assets/144778146/a843a048-0dc6-4051-a576-7f2fc0383169)
## Contributors
- [Utku Berki Baysal](https://github.com/gitdevutku)
- [Ömür Baysal](https://www.researchgate.net/profile/Oemuer-Baysal)
- Contributions are welcome! If you find any issues or have suggestions, please open an issue or create a pull request.
## License
This project is open-source and is provided under the MIT License. Feel free to contribute and use the code for educational or personal purposes.
