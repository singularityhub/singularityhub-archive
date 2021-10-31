---
id: 10070
name: "sschmeier/simg-txid"
branch: "master"
tag: "201906-2"
commit: "fd247723a347a141780af7940d4dad68adc3c7f9"
version: "8588c4cefe6d731897e578d4ce922363"
build_date: "2019-06-28T07:13:42.841Z"
size_mb: 3060
size: 1072205855
sif: "https://datasets.datalad.org/shub/sschmeier/simg-txid/201906-2/2019-06-28-fd247723-8588c4ce/8588c4cefe6d731897e578d4ce922363.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-txid/201906-2/2019-06-28-fd247723-8588c4ce/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-txid/201906-2/2019-06-28-fd247723-8588c4ce/Singularity
collection: sschmeier/simg-txid
---

# sschmeier/simg-txid:201906-2

```bash
$ singularity pull shub://sschmeier/simg-txid:201906-2
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
   conda install --yes pybedtools pysam sambamba salmon=0.14.0 star=2.7.1a samtools=1.9 gffread=0.11.4  bioawk=1.0 ucsc-gtftogenepred=377 circexplorer2=2.3.6 bedtools=2.28.0 pandas colorama rseqc=2.6.4 cpat=1.2.4 picard r-readr r-samr bioconductor-tximport bioconductor-deseq2 bioconductor-limma bioconductor-edger bioconductor-ihw multiqc=1.7
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-txid](https://github.com/sschmeier/simg-txid)
 - License: None

