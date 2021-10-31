---
id: 15348
name: "edg1983/Singularity_images"
branch: "master"
tag: "vcf_processing.def"
commit: "3a1dcaecf83a5bb3fc3c4ce573dccd2be3c13ade"
version: "19e60a30382e9861cbfd11337960829f17a828b592c8ee38b520056cc4a404c8"
build_date: "2021-01-20T17:10:10.597Z"
size_mb: 366.5
size: 384303104
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/vcf_processing.def/2021-01-20-3a1dcaec-19e60a30/19e60a30382e9861cbfd11337960829f17a828b592c8ee38b520056cc4a404c8.sif"
url: https://datasets.datalad.org/shub/edg1983/Singularity_images/vcf_processing.def/2021-01-20-3a1dcaec-19e60a30/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/vcf_processing.def/2021-01-20-3a1dcaec-19e60a30/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:vcf_processing.def

```bash
$ singularity pull shub://edg1983/Singularity_images:vcf_processing.def
```

## Singularity Recipe

```singularity
Bootstrap: library
From: centos:8

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin
    LC_ALL=C.UTF-8

%help
    Set of tools to process and QC a VCF file.
    Includes: bcftools, vt, multiqc and a custom script (VCF_fixes_opt)

%post
    yum -y install cmake \
        curl \
        gcc \
        gcc-c++ \
        git \
        bzip2 \
        bzip2-devel \
        openssl-devel \
        xz-devel \
        openssl-devel \
        ncurses-devel \
        make \
        wget \
        zlib-devel \
        autoconf \
        tar \
        unzip \
        python3 \
        python3-devel \
        procps
    
    ## Install bcftools and htslib
    cd /opt/ && wget https://github.com/samtools/bcftools/releases/download/1.10.2/bcftools-1.10.2.tar.bz2
    tar -jxvf bcftools-1.10.2.tar.bz2
    rm bcftools-1.10.2.tar.bz2
    cd bcftools-1.10.2
    ./configure
    make
    make install
    cd htslib-1.10.2
    ./configure
    make
    make install

    #install vt
    cd /opt
    wget https://github.com/atks/vt/archive/0.5772.tar.gz  
    tar -zxvf 0.5772.tar.gz
    rm 0.5772.tar.gz
    cd vt-0.5772
    make

    #install multiqc
    pip3 install multiqc

    #Get compiled VCF_fixes_opt
    cd /opt
    wget https://github.com/edg1983/VCF_fixes/raw/master/VCF_fixes
    chmod a+x VCF_fixes

    #Make links
    cd /usr/local/bin
    ln -s /opt/vt-0.5772/vt vt
    ln -s /opt/VCF_fixes VCF_fixes

%test
    bcftools --help
    vt
    multiqc --help
    VCF_fixes --help
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

