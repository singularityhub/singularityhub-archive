---
id: 5991
name: "J35P312/TayWhale"
branch: "master"
tag: "latest"
commit: "37bebe362032f93b925b76f2cca8f83259a045d4"
version: "251034f53ac40249ac0f69a6583c72a8"
build_date: "2018-12-17T16:03:48.677Z"
size_mb: 3735
size: 1645273119
sif: "https://datasets.datalad.org/shub/J35P312/TayWhale/latest/2018-12-17-37bebe36-251034f5/251034f53ac40249ac0f69a6583c72a8.simg"
url: https://datasets.datalad.org/shub/J35P312/TayWhale/latest/2018-12-17-37bebe36-251034f5/
recipe: https://datasets.datalad.org/shub/J35P312/TayWhale/latest/2018-12-17-37bebe36-251034f5/Singularity
collection: J35P312/TayWhale
---

# J35P312/TayWhale:latest

```bash
$ singularity pull shub://J35P312/TayWhale:latest
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
    apt-get -y install wget git bzip2 build-essential gcc zlib1g-dev language-pack-en-base apt-transport-https make cmake unzip
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    cd /root/ && wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && chmod 700 ./Miniconda2-latest-Linux-x86_64.sh
    cd /root/ && bash ./Miniconda2-latest-Linux-x86_64.sh -b -p /opt/anaconda/

    export PATH=/opt/anaconda/bin:${PATH}

    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

	conda install -c bioconda STAR --yes
	conda install -c bioconda picard --yes	
	conda install -c bioconda samtools --yes
	conda install -c bioconda STAR-Fusion --yes
	conda install -c bioconda stringtie --yes
	conda install -c bioconda salmon --yes
	conda install -c bioconda gffcompare --yes
```

## Collection

 - Name: [J35P312/TayWhale](https://github.com/J35P312/TayWhale)
 - License: None

