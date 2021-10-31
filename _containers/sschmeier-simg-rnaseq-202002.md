---
id: 12292
name: "sschmeier/simg-rnaseq"
branch: "master"
tag: "202002"
commit: "eacea90cc60a66282a9efc85079617b9114fa17f"
version: "009c72805d33cbcd3961d14564ef1aac68cfa0d94d99921cf3c49ddfece34a81"
build_date: "2020-05-28T12:23:10.888Z"
size_mb: 1375.71875
size: 1442545664
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202002/2020-05-28-eacea90c-009c7280/009c72805d33cbcd3961d14564ef1aac68cfa0d94d99921cf3c49ddfece34a81.sif"
url: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202002/2020-05-28-eacea90c-009c7280/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202002/2020-05-28-eacea90c-009c7280/Singularity
collection: sschmeier/simg-rnaseq
---

# sschmeier/simg-rnaseq:202002

```bash
$ singularity pull shub://sschmeier/simg-rnaseq:202002
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
   AUTHOR s.schmeier@protonmail.com

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This sets global environment variables for anything run within the container
  export PATH="/opt/conda/bin:$PATH"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   #conda update --yes -q conda 
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   echo "We install tools."
   conda install --yes salmon=1.1.0 star=2.7.3a bbmap=38.76 fastp=0.20.0 r-samr bioconductor-deseq2 bioconductor-edger r-readr bioconductor-limma bioconductor-ihw bioconductor-tximport bioconductor-biocparallel bioconductor-clusterprofiler bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-gseabase colorama pandas numpy multiqc samtools rseqc gffutils sambamba seqtk fastqc htseq
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rnaseq](https://github.com/sschmeier/simg-rnaseq)
 - License: None

