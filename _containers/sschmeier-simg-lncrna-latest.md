---
id: 5639
name: "sschmeier/simg-lncrna"
branch: "master"
tag: "latest"
commit: "e6527574bc30edd8cb953a23131c29d8cc9a3b18"
version: "dccfbe86a9a565c035bbc0c5eeed147a"
build_date: "2018-12-20T11:05:47.372Z"
size_mb: 3147
size: 988446751
sif: "https://datasets.datalad.org/shub/sschmeier/simg-lncrna/latest/2018-12-20-e6527574-dccfbe86/dccfbe86a9a565c035bbc0c5eeed147a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-lncrna/latest/2018-12-20-e6527574-dccfbe86/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-lncrna/latest/2018-12-20-e6527574-dccfbe86/Singularity
collection: sschmeier/simg-lncrna
---

# sschmeier/simg-lncrna:latest

```bash
$ singularity pull shub://sschmeier/simg-lncrna:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.11

%labels
   AUTHOR schmeier@tuta.io

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels conda-forge
   conda config --add channels bioconda
   echo "We install tools."
   conda install --yes kallisto=0.45.0 salmon=0.12.0 star=2.6.1b samtools=1.9 stringtie=1.3.4 gffcompare=0.10.1 gffread=0.9.9  bioawk=1.0  ucsc-gtftogenepred=366 circexplorer2=2.3.3 bedtools=2.27.1 pandas=0.23.3  colorama=0.3.9 rseqc=2.6.4 cpat=1.2.3  r-readr=1.1.1  r-samr=2.0  bioconductor-tximport=1.8.0  bioconductor-deseq2=1.20.0 bioconductor-limma=3.36.5 bioconductor-edger=3.22.5 bioconductor-ihw=1.8.0  multiqc=1.6a0 
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-lncrna](https://github.com/sschmeier/simg-lncrna)
 - License: None

