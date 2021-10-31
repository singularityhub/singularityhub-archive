---
id: 5189
name: "bahlolab/nf-wgs-multiqc"
branch: "master"
tag: "v0.1"
commit: "df3871590d45edc35ced12cf4bd0394424ac4cc8"
version: "2a8fae66d98f76485a38ac5874558327"
build_date: "2018-10-10T10:52:37.748Z"
size_mb: 2595
size: 1014231071
sif: "https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.1/2018-10-10-df387159-2a8fae66/2a8fae66d98f76485a38ac5874558327.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.1/2018-10-10-df387159-2a8fae66/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-wgs-multiqc/v0.1/2018-10-10-df387159-2a8fae66/Singularity
collection: bahlolab/nf-wgs-multiqc
---

# bahlolab/nf-wgs-multiqc:v0.1

```bash
$ singularity pull shub://bahlolab/nf-wgs-multiqc:v0.1
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: continuumio/miniconda3:latest

%labels
  AUTHOR Jacob Munro
  AUTHOR bahlolab

%post
    alias conda="/opt/conda/bin/conda"
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels r
    conda install -y \
        gatk4=4.0.10.0 \
        samtools=1.9 \
        bcftools=1.9 \
        multiqc=1.6 \
        fastp=0.19.4
    conda clean --all -y
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-wgs-multiqc](https://github.com/bahlolab/nf-wgs-multiqc)
 - License: None

