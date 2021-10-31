---
id: 12991
name: "sschmeier/simg-rnaseq"
branch: "master"
tag: "202005"
commit: "61589847eb89da8b6080a54dfa38620998e861e7"
version: "4a824a68180a0dd08f310ebddd3cc296fbf9d340e5c061c783108cbf8695974b"
build_date: "2020-08-18T06:42:22.068Z"
size_mb: 1220.88671875
size: 1280192512
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202005/2020-08-18-61589847-4a824a68/4a824a68180a0dd08f310ebddd3cc296fbf9d340e5c061c783108cbf8695974b.sif"
url: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202005/2020-08-18-61589847-4a824a68/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/202005/2020-08-18-61589847-4a824a68/Singularity
collection: sschmeier/simg-rnaseq
---

# sschmeier/simg-rnaseq:202005

```bash
$ singularity pull shub://sschmeier/simg-rnaseq:202005
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
   AUTHOR s.schmeier@pm.me

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
   conda install --yes salmon=1.1.0 star=2.7.3a bbmap=38.76 fastp=0.20.0 r-samr bioconductor-deseq2 bioconductor-edger r-readr bioconductor-limma bioconductor-ihw bioconductor-tximport bioconductor-biocparallel bioconductor-clusterprofiler bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-gseabase colorama pandas numpy multiqc samtools rseqc gffutils sambamba seqtk fastqc htseq subread
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rnaseq](https://github.com/sschmeier/simg-rnaseq)
 - License: None

