---
id: 6149
name: "bahlolab/nf-pacbio-amplicon-analysis"
branch: "master"
tag: "pacbio_smrt_v0.2"
commit: "6d85d8ba681f98bb7b532bc448e169bc6a1b9a61"
version: "4082e5537b741ab0408135de43803760"
build_date: "2019-01-08T15:14:12.075Z"
size_mb: 1725
size: 601894943
sif: "https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.2/2019-01-08-6d85d8ba-4082e553/4082e5537b741ab0408135de43803760.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.2/2019-01-08-6d85d8ba-4082e553/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-pacbio-amplicon-analysis/pacbio_smrt_v0.2/2019-01-08-6d85d8ba-4082e553/Singularity
collection: bahlolab/nf-pacbio-amplicon-analysis
---

# bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.2

```bash
$ singularity pull shub://bahlolab/nf-pacbio-amplicon-analysis:pacbio_smrt_v0.2
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
       pbmm2=0.10.1 \
       blasr=5.3.2 \
       lima=1.8.0 \
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

