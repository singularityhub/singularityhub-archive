---
id: 9745
name: "rpolicastro/ChIPseq"
branch: "dev"
tag: "latest"
commit: "86e52075e7209b291c55f375e65bfb4ee0ea9fe4"
version: "5be1b8e5e21b7db569407b1822d3f83c"
build_date: "2019-11-16T20:17:05.827Z"
size_mb: 3584
size: 1312874527
sif: "https://datasets.datalad.org/shub/rpolicastro/ChIPseq/latest/2019-11-16-86e52075-5be1b8e5/5be1b8e5e21b7db569407b1822d3f83c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rpolicastro/ChIPseq/latest/2019-11-16-86e52075-5be1b8e5/
recipe: https://datasets.datalad.org/shub/rpolicastro/ChIPseq/latest/2019-11-16-86e52075-5be1b8e5/Singularity
collection: rpolicastro/ChIPseq
---

# rpolicastro/ChIPseq:latest

```bash
$ singularity pull shub://rpolicastro/ChIPseq:latest
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

## Install chipseq-automation environment
conda create -n chipseq-automation -y -c conda-forge -c bioconda \
fastqc bowtie2 samtools macs2 deeptools bedtools sra-tools r-tidyverse r-getopt \
bioconductor-chipseeker bioconductor-rtracklayer bioconductor-genomicranges \
bioconductor-genomicfeatures

## Update chipseq-automation environment
conda update -n chipseq-automation -y -c conda-forge -c bioconda --all

## Clean up extra files
conda clean --all
```

## Collection

 - Name: [rpolicastro/ChIPseq](https://github.com/rpolicastro/ChIPseq)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

