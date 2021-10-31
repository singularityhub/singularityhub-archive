---
id: 14471
name: "tgac-vumc/RNA-seq"
branch: "master"
tag: "latest"
commit: "46687d759e25538296245c85d5beca6c4c269236"
version: "1f96f720adafe064ee6c32d9efe3537e"
build_date: "2021-02-22T12:43:04.730Z"
size_mb: 2448.0
size: 919171103
sif: "https://datasets.datalad.org/shub/tgac-vumc/RNA-seq/latest/2021-02-22-46687d75-1f96f720/1f96f720adafe064ee6c32d9efe3537e.sif"
url: https://datasets.datalad.org/shub/tgac-vumc/RNA-seq/latest/2021-02-22-46687d75-1f96f720/
recipe: https://datasets.datalad.org/shub/tgac-vumc/RNA-seq/latest/2021-02-22-46687d75-1f96f720/Singularity
collection: tgac-vumc/RNA-seq
---

# tgac-vumc/RNA-seq:latest

```bash
$ singularity pull shub://tgac-vumc/RNA-seq:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-7/7/os/x86_64/
Include: yum

%environment    
    export PATH=/usr/local/bin:$PATH

%post
    ./environment

    yum -y update
    yum -qq -y install curl tar bzip2 git zip
    curl -sSL https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/miniconda.sh
    bash /tmp/miniconda.sh -bfp /usr/local
    conda update conda -y
    
    git clone https://github.com/tgac-vumc/RNA-seq
    conda install mamba -c conda-forge -y
    mamba install -c conda-forge -c bioconda snakemake==5.25.0 subread -y


    rm -rf /tmp/miniconda.sh
```

## Collection

 - Name: [tgac-vumc/RNA-seq](https://github.com/tgac-vumc/RNA-seq)
 - License: None

