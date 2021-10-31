---
id: 8785
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "vcftools"
commit: "350eaa3618b50b6102b5130c111f14beb3ddd248"
version: "4b1666de3bfbcf8710f12ff76c45dcfe"
build_date: "2021-04-19T05:43:25.916Z"
size_mb: 565
size: 192614431
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/vcftools/2021-04-19-350eaa36-4b1666de/4b1666de3bfbcf8710f12ff76c45dcfe.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/vcftools/2021-04-19-350eaa36-4b1666de/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/vcftools/2021-04-19-350eaa36-4b1666de/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:vcftools

```bash
$ singularity pull shub://jlboat/BioinfoContainers:vcftools
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

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

