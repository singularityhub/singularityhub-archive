---
id: 9877
name: "rpolicastro/RNAseq"
branch: "dev"
tag: "latest"
commit: "274655bac181b9ee23c92848ed0b80f948d23003"
version: "277ba535bebda2188b8c66ae3b95191d"
build_date: "2020-01-30T16:16:27.238Z"
size_mb: 5541
size: 1742438431
sif: "https://datasets.datalad.org/shub/rpolicastro/RNAseq/latest/2020-01-30-274655ba-277ba535/277ba535bebda2188b8c66ae3b95191d.simg"
url: https://datasets.datalad.org/shub/rpolicastro/RNAseq/latest/2020-01-30-274655ba-277ba535/
recipe: https://datasets.datalad.org/shub/rpolicastro/RNAseq/latest/2020-01-30-274655ba-277ba535/Singularity
collection: rpolicastro/RNAseq
---

# rpolicastro/RNAseq:latest

```bash
$ singularity pull shub://rpolicastro/RNAseq:latest
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

## Install RNA-seq analysis software
conda create -n rnaseq-automation -y -c conda-forge -c bioconda \
pandas fastqc star samtools subread \
r-tidyverse bioconductor-rtracklayer bioconductor-genomicranges bioconductor-genomicfeatures \
bioconductor-edger bioconductor-deseq2 bioconductor-clusterprofiler bioconductor-reactomepa

## Update rnaseq-automation environment
#conda update -n chip-downsampling -y --strict-channel-priority -c conda-forge -c bioconda --all

## Clean up extra files
conda clean -y --all
```

## Collection

 - Name: [rpolicastro/RNAseq](https://github.com/rpolicastro/RNAseq)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

