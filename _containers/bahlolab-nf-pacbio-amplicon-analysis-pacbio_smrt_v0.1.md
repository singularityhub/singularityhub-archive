---
id: 6148
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "pacbio_smrt_v0.1"
commit: "6d85d8ba681f98bb7b532bc448e169bc6a1b9a61"
version: "16e2431e6514bb07b62953a881fe0153"
build_date: "2019-01-08T15:14:12.080Z"
size_mb: 1707
size: 596238367
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.1/2019-01-08-6d85d8ba-16e2431e/16e2431e6514bb07b62953a881fe0153.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.1/2019-01-08-6d85d8ba-16e2431e/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.1/2019-01-08-6d85d8ba-16e2431e/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.1

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.1
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
       pbmm2=0.8.1 \
       blasr=5.3.2 \
       lima=1.7.1 \
       pbccs=3.1.0 \
       pblaa=2.4.2 \
       pbsv=2.0.1
    conda clean --tarballs --index-cache --source-cache
    apt-get update && apt-get install -y procps

%environment
    export PATH="/opt/conda/bin:/usr/local/bin:/usr/bin:/bin:"
```

## Collection

 - Name: [bahlolab/nf-pacbio-amplicon-analysis](https://github.com/bahlolab/nf-pacbio-amplicon-analysis)
 - License: None

