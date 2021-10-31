---
id: 10187
name: "DrVale83/bioinfo"
branch: "master"
tag: "vcftools"
commit: "ddabf5b72deb10a2fcfa2d4772cbd340e9135514"
version: "3631cd21ad609f5822935ac6785a22f9"
build_date: "2021-03-03T08:41:49.734Z"
size_mb: 561
size: 191954975
sif: "https://datasets.datalad.org/shub/DrVale83/bioinfo/vcftools/2021-03-03-ddabf5b7-3631cd21/3631cd21ad609f5822935ac6785a22f9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DrVale83/bioinfo/vcftools/2021-03-03-ddabf5b7-3631cd21/
recipe: https://datasets.datalad.org/shub/DrVale83/bioinfo/vcftools/2021-03-03-ddabf5b7-3631cd21/Singularity
collection: DrVale83/bioinfo
---

# DrVale83/bioinfo:vcftools

```bash
$ singularity pull shub://DrVale83/bioinfo:vcftools
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    Input VCF
    vcftools latest

%help
    singularity run vcftools.simg -h

%post
    apt-get update --fix-missing && apt-get install -y git autoconf g++ zlib1g gcc make automake pkg-config zlib1g-dev curl perl libcurl4-gnutls-dev libbz2-dev liblzma-dev
    cd /opt/
    git clone https://github.com/vcftools/vcftools.git
    cd vcftools
    ./autogen.sh
    ./configure
    make
    make install
    chmod -R 777 /opt/vcftools
    cd /opt/
    git clone https://github.com/samtools/htslib
    cd htslib
    autoheader
    autoconf
    ./configure
    make
    make install
    chmod -R 777 /opt/htslib

%runscript
    exec "$@"
```

## Collection

 - Name: [DrVale83/bioinfo](https://github.com/DrVale83/bioinfo)
 - License: None

