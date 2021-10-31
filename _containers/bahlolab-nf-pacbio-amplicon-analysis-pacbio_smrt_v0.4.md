---
id: 6523
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "pacbio_smrt_v0.4"
commit: "d5490960e30212c3292e4583b6a4d0aad5de4b48"
version: "9dba58f9fb2f954cd8612996e16e7596"
build_date: "2019-01-24T13:54:58.840Z"
size_mb: 1563
size: 545972255
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.4/2019-01-24-d5490960-9dba58f9/9dba58f9fb2f954cd8612996e16e7596.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.4/2019-01-24-d5490960-9dba58f9/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.4/2019-01-24-d5490960-9dba58f9/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.4

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.4
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: continuumio/miniconda3:latest

%labels
  AUTHOR Jacob Munro
  AUTHOR bahlolab

%post
    alias conda="/opt/conda/bin/conda"
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda install -y \
       genomicconsensus=2.3.2 \
       pbmm2=0.12.0 \
       blasr=5.3.2 \
       lima=1.8.0 \
       pbccs=3.3.0 \
       pblaa=2.4.2 \
       pbsv=2.1.1
    conda clean --tarballs --index-cache --source-cache
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

