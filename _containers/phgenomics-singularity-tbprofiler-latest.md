---
id: 11920
name: "phgenomics-singularity/tbprofiler"
branch: "master"
tag: "latest"
commit: "215eb93ffc2e0176cdfae5c4e476e4b1f221992f"
version: "8459e8d0c02cd3539ed17c4ad5b50c9b"
build_date: "2020-01-06T01:52:28.113Z"
size_mb: 3645.0
size: 1781182495
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/tbprofiler/latest/2020-01-06-215eb93f-8459e8d0/8459e8d0c02cd3539ed17c4ad5b50c9b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/tbprofiler/latest/2020-01-06-215eb93f-8459e8d0/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/tbprofiler/latest/2020-01-06-215eb93f-8459e8d0/Singularity
collection: phgenomics-singularity/tbprofiler
---

# phgenomics-singularity/tbprofiler:latest

```bash
$ singularity pull shub://phgenomics-singularity/tbprofiler:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.12

%help
A Singularity image for TB-profiler

%labels
Maintainer Kristy Horan
Build 1.0
tb-profiler v2.8.1

%environment
export PATH=/opt/conda/bin:$PATH

%post

apt-get update
apt-get -y install locales sudo

export PATH=/opt/conda/bin:$PATH

conda upgrade -c defaults --override-channels conda
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda

conda install -c bioconda tb-profiler=2.8.1
```

## Collection

 - Name: [phgenomics-singularity/tbprofiler](https://github.com/phgenomics-singularity/tbprofiler)
 - License: None

