---
id: 6706
name: "maehler/bcftools-singularity"
branch: "master"
tag: "1.9"
commit: "d06e3b4799c7270df84c55d4a99ef4611f893327"
version: "f77f23f6e257889dc0e6d54dd37f4f33"
build_date: "2020-11-02T09:19:41.036Z"
size_mb: 436
size: 175398943
sif: "https://datasets.datalad.org/shub/maehler/bcftools-singularity/1.9/2020-11-02-d06e3b47-f77f23f6/f77f23f6e257889dc0e6d54dd37f4f33.simg"
url: https://datasets.datalad.org/shub/maehler/bcftools-singularity/1.9/2020-11-02-d06e3b47-f77f23f6/
recipe: https://datasets.datalad.org/shub/maehler/bcftools-singularity/1.9/2020-11-02-d06e3b47-f77f23f6/Singularity
collection: maehler/bcftools-singularity
---

# maehler/bcftools-singularity:1.9

```bash
$ singularity pull shub://maehler/bcftools-singularity:1.9
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get update
    apt-get install -y \
        build-essential \
        libz-dev \
        libbz2-dev \
        liblzma-dev \
        git
    git clone git://github.com/samtools/htslib.git
    git clone git://github.com/samtools/bcftools.git
    cd bcftools
    git checkout 1.9
    make && make install
```

## Collection

 - Name: [maehler/bcftools-singularity](https://github.com/maehler/bcftools-singularity)
 - License: None

