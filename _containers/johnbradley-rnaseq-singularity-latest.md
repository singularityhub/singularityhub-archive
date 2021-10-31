---
id: 962
name: "johnbradley/rnaseq-singularity"
branch: "master"
tag: "latest"
commit: "e559dd55a4159b4ec15464c6889d382abb60d9d8"
version: "eba0e3bd44b8b8803f329b9bf7aa0070"
build_date: "2019-07-23T07:49:20.854Z"
size_mb: 1408
size: 714235935
sif: "https://datasets.datalad.org/shub/johnbradley/rnaseq-singularity/latest/2019-07-23-e559dd55-eba0e3bd/eba0e3bd44b8b8803f329b9bf7aa0070.simg"
url: https://datasets.datalad.org/shub/johnbradley/rnaseq-singularity/latest/2019-07-23-e559dd55-eba0e3bd/
recipe: https://datasets.datalad.org/shub/johnbradley/rnaseq-singularity/latest/2019-07-23-e559dd55-eba0e3bd/Singularity
collection: johnbradley/rnaseq-singularity
---

# johnbradley/rnaseq-singularity:latest

```bash
$ singularity pull shub://johnbradley/rnaseq-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
Include: yum

%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    yum -y update
    yum -y install vim-minimal bzip2-devel sqlite-devel xz-devel tk-devel gdbm-devel readline-devel openssl-devel git vim wget gcc make bzip2 patch gcc-c++
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda
    export PATH="/opt/miniconda/bin:$PATH"
    conda install -c bioconda fastqc
```

## Collection

 - Name: [johnbradley/rnaseq-singularity](https://github.com/johnbradley/rnaseq-singularity)
 - License: None

