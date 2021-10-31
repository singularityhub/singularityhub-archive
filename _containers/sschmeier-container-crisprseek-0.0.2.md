---
id: 11905
name: "sschmeier/container-crisprseek"
branch: "master"
tag: "0.0.2"
commit: "faa9d138377685c16a9b290613190b6853f128df"
version: "362f8cd394d407e0574dc3abcae526a94362693ff6f03489471a8fe6162be86c"
build_date: "2020-04-21T20:57:56.226Z"
size_mb: 3306.765625
size: 3467395072
sif: "https://datasets.datalad.org/shub/sschmeier/container-crisprseek/0.0.2/2020-04-21-faa9d138-362f8cd3/362f8cd394d407e0574dc3abcae526a94362693ff6f03489471a8fe6162be86c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/container-crisprseek/0.0.2/2020-04-21-faa9d138-362f8cd3/
recipe: https://datasets.datalad.org/shub/sschmeier/container-crisprseek/0.0.2/2020-04-21-faa9d138-362f8cd3/Singularity
collection: sschmeier/container-crisprseek
---

# sschmeier/container-crisprseek:0.0.2

```bash
$ singularity pull shub://sschmeier/container-crisprseek:0.0.2
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
  export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
  unset CONDA_DEFAULT_ENV
  export ANACONDA_HOME=/opt/conda

%post
   export PATH=/opt/conda/bin:$PATH
   echo "We add conda channels."
   # should be added in this order for bioconda to function as intended
   conda config --add channels defaults
   conda config --add channels bioconda
   conda config --add channels conda-forge
   conda update -c defaults conda
   echo "We install tools."
   conda install --yes biopython=1.74 pandas=0.25.3 bedtools=2.29.2 gffcompare=0.11.2 gffread=0.11.6 gffutils=0.9
   conda install --yes r-base=3.6.2 bioconductor-crisprseek bioconductor-bsgenome.hsapiens.ucsc.hg19 bioconductor-bsgenome.hsapiens.ucsc.hg38 bioconductor-org.hs.eg.db bioconductor-txdb.hsapiens.ucsc.hg19.knowngene bioconductor-txdb.hsapiens.ucsc.hg38.knowngene bioconductor-txdb.mmusculus.ucsc.mm9.knowngene bioconductor-txdb.mmusculus.ucsc.mm10.knowngene bioconductor-bsgenome.mmusculus.ucsc.mm9 bioconductor-bsgenome.mmusculus.ucsc.mm10 bioconductor-org.mmu.eg.db
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/container-crisprseek](https://github.com/sschmeier/container-crisprseek)
 - License: None

