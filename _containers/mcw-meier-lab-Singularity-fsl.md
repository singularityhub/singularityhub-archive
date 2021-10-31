---
id: 8428
name: "mcw-meier-lab/Singularity"
branch: "master"
tag: "fsl"
commit: "5e51bb88a5e3a75c894b8dfd0cd8cd1add3af8c0"
version: "907388919cf6651ff32aa4558bb9435a"
build_date: "2019-04-16T01:22:32.913Z"
size_mb: 9130
size: 4086022175
sif: "https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/fsl/2019-04-16-5e51bb88-90738891/907388919cf6651ff32aa4558bb9435a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-meier-lab/Singularity/fsl/2019-04-16-5e51bb88-90738891/
recipe: https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/fsl/2019-04-16-5e51bb88-90738891/Singularity
collection: mcw-meier-lab/Singularity
---

# mcw-meier-lab/Singularity:fsl

```bash
$ singularity pull shub://mcw-meier-lab/Singularity:fsl
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
    Maintainer Lezlie Espana
    Version v1.0

%help
    This is a test container for installing FSL version 5.0.11.

%environment
    export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

%files
    fslinstaller.py /usr/local/

%post
    mkdir -p /scratch/global /scratch/local
    apt-get update && apt-get install -y git \
        build-essential \
        gcc-multilib \
        curl \
        bc \
        wget \
        tcsh \
        python

    python /usr/local/fslinstaller.py -V 5.0.11 -D -d /usr/local/fsl
    echo '. /usr/local/fsl/etc/fslconf/fsl.sh' >> /usr/local/.bashrc
    echo 'export PATH=/usr/local/fsl/bin:$PATH' >> $SINGULARITY_ENVIRONMENT
    chmod +x /usr/local/fsl/etc/fslconf/fsl.sh
    exec /usr/local/fsl/etc/fslconf/fsl.sh

    apt-get clean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [mcw-meier-lab/Singularity](https://github.com/mcw-meier-lab/Singularity)
 - License: None

