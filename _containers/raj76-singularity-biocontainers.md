---
id: 1757
name: "raj76/singularity"
branch: "master"
tag: "biocontainers"
commit: "e4757bb12a126482b3d2bce922ac5278a9182422"
version: "b3140d02605371110112713831ed81c1"
build_date: "2019-09-04T14:37:57.566Z"
size_mb: 965
size: 354299935
sif: "https://datasets.datalad.org/shub/raj76/singularity/biocontainers/2019-09-04-e4757bb1-b3140d02/b3140d02605371110112713831ed81c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/raj76/singularity/biocontainers/2019-09-04-e4757bb1-b3140d02/
recipe: https://datasets.datalad.org/shub/raj76/singularity/biocontainers/2019-09-04-e4757bb1-b3140d02/Singularity
collection: raj76/singularity
---

# raj76/singularity:biocontainers

```bash
$ singularity pull shub://raj76/singularity:biocontainers
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
Maintainer Raj Ayyampalayam
base.image="ubuntu:16.04"
version="4"
software="Biocontainers base Image"
software.version="08252016"
description="Base image for BioDocker"
website="http://biocontainers.pro"
documentation="https://github.com/BioContainers/specs/wiki"
license="https://github.com/BioContainers/containers/blob/master/LICENSE"
tags="Genomics,Proteomics,Transcriptomics,General,Metabolomics"

%post
export DEBIAN_FRONTEND noninteractive

mv /etc/apt/sources.list /etc/apt/sources.list.bkp 
bash -c 'echo -e "deb mirror://mirrors.ubuntu.com/mirrors.txt xenial main restricted universe multiverse\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-updates main restricted universe multiverse\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-backports main restricted universe multiverse\n\
deb mirror://mirrors.ubuntu.com/mirrors.txt xenial-security main restricted universe multiverse\n\n" > /etc/apt/sources.list' && \
cat /etc/apt/sources.list.bkp >> /etc/apt/sources.list && \
cat /etc/apt/sources.list

apt-get clean all
apt-get update
apt-get upgrade -y
apt-get install -y  \
        autotools-dev   \
        automake        \
        cmake           \
        curl            \
        grep            \
        sed             \
        dpkg            \
        fuse            \
        git             \
        wget            \
        zip             \
        openjdk-8-jre   \
        build-essential \
        pkg-config      \
        python          \
	python-dev      \
        python-pip      \
        bzip2           \
        ca-certificates \
        libglib2.0-0    \
        libxext6        \
        libsm6          \
        libxrender1     \
        git             \
        mercurial       \
        subversion      \
        zlib1g-dev
apt-get clean
apt-get purge
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh
wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh -O ~/miniconda.sh
/bin/bash ~/miniconda.sh -b -p /opt/conda
rm ~/miniconda.sh

TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'`
curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb
dpkg -i tini.deb
rm tini.deb
apt-get clean

# give write permissions to conda folder
chmod 777 -R /opt/conda/

export PATH=$PATH:/opt/conda/bin
conda config --add channels r
conda config --add channels bioconda

conda upgrade conda



%environment
export LC_ALL=C
export DEBIAN_FRONTEND noninteractive
export PATH=$PATH:/opt/conda/bin
```

## Collection

 - Name: [raj76/singularity](https://github.com/raj76/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

