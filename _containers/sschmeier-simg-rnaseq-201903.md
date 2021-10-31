---
id: 7762
name: "sschmeier/simg-rnaseq"
branch: "master"
tag: "201903"
commit: "75760802b770c9920004739bc30bfe1ea90678e5"
version: "da9ae84f0e511618173dd8137a02862c"
build_date: "2019-12-16T01:41:21.662Z"
size_mb: 3060
size: 1024339999
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201903/2019-12-16-75760802-da9ae84f/da9ae84f0e511618173dd8137a02862c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-rnaseq/201903/2019-12-16-75760802-da9ae84f/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201903/2019-12-16-75760802-da9ae84f/Singularity
collection: sschmeier/simg-rnaseq
---

# sschmeier/simg-rnaseq:201903

```bash
$ singularity pull shub://sschmeier/simg-rnaseq:201903
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%labels
   AUTHOR schmeier@tuta.io

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
   conda config --add channels conda-forge
   conda config --add channels bioconda
   echo "We install tools."
   conda install --yes r-samr bioconductor-deseq2=1.18.1 bioconductor-edger r-readr bioconductor-limma bioconductor-ihw bioconductor-tximport bioconductor-biocparallel bioconductor-clusterprofiler bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-gseabase pandas numpy star=2.6.1d multiqc=1.7 bbmap=38.22 samtools=1.9 colorama rseqc=3.0.0 salmon=0.13.1 gffutils=0.9
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rnaseq](https://github.com/sschmeier/simg-rnaseq)
 - License: None

