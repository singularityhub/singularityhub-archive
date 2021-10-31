---
id: 4615
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "contigs_annotation"
commit: "595828a19dfce3afde08afd9d4583b1e076a539f"
version: "e9a7187ad16aafe59fcf574b0324d167"
build_date: "2018-09-02T22:05:36.535Z"
size_mb: 1354
size: 528773151
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/contigs_annotation/2018-09-02-595828a1-e9a7187a/e9a7187ad16aafe59fcf574b0324d167.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/contigs_annotation/2018-09-02-595828a1-e9a7187a/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/contigs_annotation/2018-09-02-595828a1-e9a7187a/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:contigs_annotation

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:contigs_annotation
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%files
    bin/ExtractAnnotation.py /usr/local/bin
    bin/sum_contigs_length_per_annotation.R /usr/local/bin

%post
    mkdir /pasteur
    apt update
    apt install -y wget build-essential python2.7 python-pip
    pip install numpy
    pip install cogent
    
    cd /home    
    wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
    tar -xzf ncbi-blast-2.2.31+-x64-linux.tar.gz
    rm ncbi-blast-2.2.31+-x64-linux.tar.gz
    mv ncbi-blast-2.2.31+/bin/* /usr/local/bin
    
    wget https://cran.r-project.org/bin/linux/ubuntu/xenial/r-base-core_3.2.5-1xenial_amd64.deb
    apt install -y ./r-base-core_3.2.5-1xenial_amd64.deb 
    rm r-base-core_3.2.5-1xenial_amd64.deb
    R --vanilla -e 'install.packages("plyr", repo="http://mirror.ibcp.fr/pub/CRAN/")'
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

