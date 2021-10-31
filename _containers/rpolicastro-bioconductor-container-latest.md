---
id: 9849
name: "rpolicastro/bioconductor-container"
branch: "master"
tag: "latest"
commit: "cb439515bcae1746527f70329b62828b6083a4fc"
version: "f390ddbbda069a55ef43e32c0ec02e8f"
build_date: "2020-08-18T18:41:49.945Z"
size_mb: 5006
size: 1496412191
sif: "https://datasets.datalad.org/shub/rpolicastro/bioconductor-container/latest/2020-08-18-cb439515-f390ddbb/f390ddbbda069a55ef43e32c0ec02e8f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rpolicastro/bioconductor-container/latest/2020-08-18-cb439515-f390ddbb/
recipe: https://datasets.datalad.org/shub/rpolicastro/bioconductor-container/latest/2020-08-18-cb439515-f390ddbb/Singularity
collection: rpolicastro/bioconductor-container
---

# rpolicastro/bioconductor-container:latest

```bash
$ singularity pull shub://rpolicastro/bioconductor-container:latest
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

## Create environment
conda create -n bioconductor -y -c conda-forge -c bioconda -y \
r-tidyverse \
r-getopt \
r-devtools \
r-roxygen2 \
bioconductor-tsrchitect \
bioconductor-genomicranges \
bioconductor-genomicfeatures \
bioconductor-rtracklayer \
bioconductor-chipseeker \
bioconductor-clusterprofiler \
bioconductor-gviz \
bioconductor-biomart \
bioconductor-edger \
bioconductor-deseq2 \
bioconductor-rsubread \
bioconductor-rsamtools \
bioconductor-annotationhub \
bioconductor-reactomepa \
bioconductor-dose \
bioconductor-diffbind

## Update environment
conda update -n bioconductor -y -c conda-forge -c bioconda --all

## Clean up extra files
conda clean --all
```

## Collection

 - Name: [rpolicastro/bioconductor-container](https://github.com/rpolicastro/bioconductor-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

