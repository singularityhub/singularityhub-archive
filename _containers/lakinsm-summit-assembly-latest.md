---
id: 3215
name: "lakinsm/summit-assembly"
branch: "master"
tag: "latest"
commit: "deb5015e87d7c5a9e2e3a02536b858a43279d447"
version: "3eb8581ceeaabd872c2b81bdad16eb6f"
build_date: "2018-08-28T03:21:34.065Z"
size_mb: 604
size: 214450207
sif: "https://datasets.datalad.org/shub/lakinsm/summit-assembly/latest/2018-08-28-deb5015e-3eb8581c/3eb8581ceeaabd872c2b81bdad16eb6f.simg"
url: https://datasets.datalad.org/shub/lakinsm/summit-assembly/latest/2018-08-28-deb5015e-3eb8581c/
recipe: https://datasets.datalad.org/shub/lakinsm/summit-assembly/latest/2018-08-28-deb5015e-3eb8581c/Singularity
collection: lakinsm/summit-assembly
---

# lakinsm/summit-assembly:latest

```bash
$ singularity pull shub://lakinsm/summit-assembly:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie-slim


%post
    apt update \
    && apt install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    git \
    gcc \
    make \
    automake \
    autoconf \
    openjdk-7-jre \
    wget \
    unzip \
    sed \
    && rm -rf /var/lib/apt/lists/*
    cd /opt
    git clone https://github.com/loneknightpy/idba \
    && cd idba \
    && sed -i 's/kMaxShortSequence = 128/kMaxShortSequence = 500/' src/sequence/short_sequence.h \
    && ./build.sh \
    && make
    cd /usr/local/bin
    ln -s /opt/idba/bin/idba_ud
    ln -s /opt/idba/bin/fq2fa
    cd /
    TRIMMOMATIC_SOURCE="Trimmomatic-0.36.zip" \
    TRIMMOMATIC_HOME="/opt/trimmomatic"
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip -O /opt/trimmomatic.zip && \
    unzip /opt/trimmomatic.zip -d /opt/ && \
    rm /opt/trimmomatic.zip
    cd /

    
%test
    which idba_ud
```

## Collection

 - Name: [lakinsm/summit-assembly](https://github.com/lakinsm/summit-assembly)
 - License: None

