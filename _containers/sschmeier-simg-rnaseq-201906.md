---
id: 9505
name: "sschmeier/simg-rnaseq"
branch: "master"
tag: "201906"
commit: "26f741e6a5ffe39f87b9bc9d993cca865afcd0dc"
version: "c8f8c9e3ed65033b0549ca99e0f3d295"
build_date: "2020-11-19T09:58:18.257Z"
size_mb: 3831
size: 1313349663
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201906/2020-11-19-26f741e6-c8f8c9e3/c8f8c9e3ed65033b0549ca99e0f3d295.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-rnaseq/201906/2020-11-19-26f741e6-c8f8c9e3/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201906/2020-11-19-26f741e6-c8f8c9e3/Singularity
collection: sschmeier/simg-rnaseq
---

# sschmeier/simg-rnaseq:201906

```bash
$ singularity pull shub://sschmeier/simg-rnaseq:201906
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
   conda update --yes -q conda 
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   echo "We install tools."
   conda install --yes r-samr bioconductor-deseq2 bioconductor-edger r-readr bioconductor-limma bioconductor-ihw bioconductor-tximport bioconductor-biocparallel bioconductor-clusterprofiler bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-gseabase colorama pandas numpy star=2.7.1a multiqc=1.7 bbmap=38.51 samtools=1.9 rseqc=3.0.0 salmon=0.14.0 gffutils=0.9 sambamba=0.7.0 seqtk=1.3 fastp=0.20.0 fastqc=0.11.8
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rnaseq](https://github.com/sschmeier/simg-rnaseq)
 - License: None

