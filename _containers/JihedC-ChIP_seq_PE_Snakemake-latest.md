---
id: 14293
name: "JihedC/ChIP_seq_PE_Snakemake"
branch: "master"
tag: "latest"
commit: "cd7ddb2681d3fa7b2734a16fc6d30878a169a78a"
version: "505b41f1af0945f31fd29e670588f2cd"
build_date: "2020-09-25T15:43:43.949Z"
size_mb: 2132.0
size: 734535711
sif: "https://datasets.datalad.org/shub/JihedC/ChIP_seq_PE_Snakemake/latest/2020-09-25-cd7ddb26-505b41f1/505b41f1af0945f31fd29e670588f2cd.sif"
url: https://datasets.datalad.org/shub/JihedC/ChIP_seq_PE_Snakemake/latest/2020-09-25-cd7ddb26-505b41f1/
recipe: https://datasets.datalad.org/shub/JihedC/ChIP_seq_PE_Snakemake/latest/2020-09-25-cd7ddb26-505b41f1/Singularity
collection: JihedC/ChIP_seq_PE_Snakemake
---

# JihedC/ChIP_seq_PE_Snakemake:latest

```bash
$ singularity pull shub://JihedC/ChIP_seq_PE_Snakemake:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.7.12
%labels
AUTHOR jihed.chouaref@gmail.com

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container export
PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
unset CONDA_DEFAULT_ENV
export ANACONDA_HOME=/opt/conda

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This is going to be executed after the base container has been downloaded export
PATH=/opt/conda/bin:$PATH
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
#conda install --yes centrifuge=1.0.3
#conda install --yes krona=2.7.1
conda install --yes deeptools=3.5.0
#conda install --yes fastqc=0.11.9
#conda install --yes macs2=2.2.7.1
conda install --yes multiqc=1.9
conda install --yes picard=2.23.4
#conda install --yes r-base=3.6.1
conda install --yes cutadapt=2.10
conda install --yes trim-galore=0.6.6
conda install --yes bowtie2=2.4.1
conda install --yes samtools=1.10
conda install --yes snakemake=5.24.2
conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [JihedC/ChIP_seq_PE_Snakemake](https://github.com/JihedC/ChIP_seq_PE_Snakemake)
 - License: [MIT License](https://api.github.com/licenses/mit)

