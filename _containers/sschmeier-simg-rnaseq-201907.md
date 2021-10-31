---
id: 10149
name: "sschmeier/simg-rnaseq"
branch: "master"
tag: "201907"
commit: "1cbf4e73e46193968a1e697bdd884430dedd3d15"
version: "285705544107256549191175558aa555942a4ed713b117814b5da99abaf7873c"
build_date: "2020-12-03T11:53:56.263Z"
size_mb: 1180.0390625
size: 1237360640
sif: "https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201907/2020-12-03-1cbf4e73-28570554/285705544107256549191175558aa555942a4ed713b117814b5da99abaf7873c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sschmeier/simg-rnaseq/201907/2020-12-03-1cbf4e73-28570554/
recipe: https://datasets.datalad.org/shub/sschmeier/simg-rnaseq/201907/2020-12-03-1cbf4e73-28570554/Singularity
collection: sschmeier/simg-rnaseq
---

# sschmeier/simg-rnaseq:201907

```bash
$ singularity pull shub://sschmeier/simg-rnaseq:201907
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
   conda install --yes r-samr bioconductor-deseq2 bioconductor-edger r-readr bioconductor-limma bioconductor-ihw bioconductor-tximport bioconductor-biocparallel bioconductor-clusterprofiler bioconductor-org.hs.eg.db bioconductor-org.mm.eg.db bioconductor-gseabase colorama pandas numpy star=2.7.1a multiqc=1.7 bbmap=38.51 samtools=1.9 rseqc=3.0.0 salmon=0.14.1 gffutils=0.9 sambamba=0.7.0 seqtk=1.3 fastp=0.20.0 fastqc=0.11.8 htseq
   conda clean --index-cache --tarballs --packages --yes
```

## Collection

 - Name: [sschmeier/simg-rnaseq](https://github.com/sschmeier/simg-rnaseq)
 - License: None

