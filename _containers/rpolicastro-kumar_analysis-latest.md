---
id: 10205
name: "rpolicastro/kumar_analysis"
branch: "master"
tag: "latest"
commit: "15d06bff485c3406d75c4086b54f2cc043b09711"
version: "7f7866c52ea98ab647f33af697a84599"
build_date: "2019-07-04T14:23:00.807Z"
size_mb: None
size: 1341095967
sif: "https://datasets.datalad.org/shub/rpolicastro/kumar_analysis/latest/2019-07-04-15d06bff-7f7866c5/7f7866c52ea98ab647f33af697a84599.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rpolicastro/kumar_analysis/latest/2019-07-04-15d06bff-7f7866c5/
recipe: https://datasets.datalad.org/shub/rpolicastro/kumar_analysis/latest/2019-07-04-15d06bff-7f7866c5/Singularity
collection: rpolicastro/kumar_analysis
---

# rpolicastro/kumar_analysis:latest

```bash
$ singularity pull shub://rpolicastro/kumar_analysis:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%post

## Add conda to path
export PATH=$PATH:/opt/conda/bin

## Update conda
conda update -n base -y -c defaults conda

## Install Drop-seq analysis software
conda create -n dropseq-analysis -y -c conda-forge -c bioconda \
dropseq_tools star picard fastqc sra-tools \
r-tidyverse r-seurat umap-learn

## Update Drop-seq analysis environment
conda update -n dropseq-analysis -y -c conda-forge -c bioconda --all

## Clean up extra files
conda clean -y --all
```

## Collection

 - Name: [rpolicastro/kumar_analysis](https://github.com/rpolicastro/kumar_analysis)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

