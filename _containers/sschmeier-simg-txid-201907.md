---
id: 10146
name: "sschmeier/simg-txid"
branch: "master"
tag: "201907"
commit: "170bc75da222bbe753a1e181efa7408322eb723b"
version: "739a1f40081f8098dcc9797264b9cfda"
build_date: "2020-11-01T08:55:01.612Z"
size_mb: 3457
size: 1195069471
sif: "https://datasets.datalad.org/shub/sschmeier/simg-txid/201907/2020-11-01-170bc75d-739a1f40/739a1f40081f8098dcc9797264b9cfda.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-txid/201907/2020-11-01-170bc75d-739a1f40/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-txid/201907/2020-11-01-170bc75d-739a1f40/Singularity
collection: sschmeier/simg-txid
---

# sschmeier/simg-txid:201907

```bash
$ singularity pull shub://sschmeier/simg-txid:201907
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
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda


%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   #conda update -n base -c defaults conda
   #conda update --yes --all
   echo "We install tools."     
   conda install --yes pybedtools pysam sambamba salmon=0.14.1 star=2.7.1a samtools=1.9 gffread=0.11.4  bioawk=1.0 ucsc-gtftogenepred=377 circexplorer2=2.3.6 bedtools=2.28.0 pandas colorama rseqc=2.6.4 cpat=1.2.4 picard r-readr r-samr bioconductor-tximport bioconductor-deseq2 bioconductor-limma bioconductor-edger bioconductor-ihw multiqc gffcompare=0.11.2 julia
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-txid](https://github.com/sschmeier/simg-txid)
 - License: None

