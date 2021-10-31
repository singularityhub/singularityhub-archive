---
id: 7412
name: "sschmeier/simg-txid"
branch: "master"
tag: "201902"
commit: "36604631b8642239c621ac904501654ef2539c6a"
version: "fa5f7b2493d26280494935ae4b7cb6cf"
build_date: "2019-02-24T08:38:40.274Z"
size_mb: 3807
size: 1326727199
sif: "https://datasets.datalad.org/shub/sschmeier/simg-txid/201902/2019-02-24-36604631-fa5f7b24/fa5f7b2493d26280494935ae4b7cb6cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-txid/201902/2019-02-24-36604631-fa5f7b24/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-txid/201902/2019-02-24-36604631-fa5f7b24/Singularity
collection: sschmeier/simg-txid
---

# sschmeier/simg-txid:201902

```bash
$ singularity pull shub://sschmeier/simg-txid:201902
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
   conda install --yes pybedtools pysam sambamba=0.6.8 salmon=0.12.0 star=2.7.0d samtools=1.9 gffread=0.9.9  bioawk=1.0 ucsc-gtftogenepred=377 circexplorer2=2.3.5 bedtools=2.27.1 pandas=0.23.3 colorama=0.3.9 rseqc=2.6.4 cpat=1.2.3 picard=2.18.26 r-readr=1.3.1 r-samr=2.0 bioconductor-tximport=1.10.0 bioconductor-deseq2=1.22.1 bioconductor-limma=3.38.3 bioconductor-edger=3.24.1 bioconductor-ihw=1.10.0 multiqc=1.7
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-txid](https://github.com/sschmeier/simg-txid)
 - License: None

