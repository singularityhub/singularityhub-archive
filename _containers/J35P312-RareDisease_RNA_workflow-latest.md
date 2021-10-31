---
id: 15715
name: "J35P312/RareDisease_RNA_workflow"
branch: "main"
tag: "latest"
commit: "f2d776902463dc26e39effa6d8c024d60dfe873c"
version: "5617a7beb3927b6715d5f73a12fb780b"
build_date: "2021-03-23T17:26:19.892Z"
size_mb: 2188.0
size: 1407647775
sif: "https://datasets.datalad.org/shub/J35P312/RareDisease_RNA_workflow/latest/2021-03-23-f2d77690-5617a7be/5617a7beb3927b6715d5f73a12fb780b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/J35P312/RareDisease_RNA_workflow/latest/2021-03-23-f2d77690-5617a7be/
recipe: https://datasets.datalad.org/shub/J35P312/RareDisease_RNA_workflow/latest/2021-03-23-f2d77690-5617a7be/Singularity
collection: J35P312/RareDisease_RNA_workflow
---

# J35P312/RareDisease_RNA_workflow:latest

```bash
$ singularity pull shub://J35P312/RareDisease_RNA_workflow:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
SHELL=/bin/bash
PATH=/opt/anaconda/bin:${PATH}
LC_ALL=C.UTF-8

%runscript
    echo "This is what happens when you run the container..."
    export PATH=/opt/anaconda/bin:${PATH}    

%post
    echo "Hello from inside the container"
    apt-get update
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip python3
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda3-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/anaconda/

    export PATH=/opt/anaconda/bin:${PATH}

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    cd /bin/ && git clone https://github.com/J35P312/BootstrapAnn.git

    conda install samtools star=2.7.8a gatk4=4.2.0 pip tabix
    pip install numpy
    pip install scipy
```

## Collection

 - Name: [J35P312/RareDisease_RNA_workflow](https://github.com/J35P312/RareDisease_RNA_workflow)
 - License: None

