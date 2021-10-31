---
id: 14536
name: "edg1983/Singularity_images"
branch: "master"
tag: "qcbam-v1.0.def"
commit: "f4b53e73bdecc32b3168c64270ef1a86e9c2772a"
version: "0e6774fb498512d7b961aeb3539a87e6428b0ee50758e6ae71f3ff1265e5b231"
build_date: "2021-01-20T16:55:48.549Z"
size_mb: 576.94921875
size: 604975104
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/qcbam-v1.0.def/2021-01-20-f4b53e73-0e6774fb/0e6774fb498512d7b961aeb3539a87e6428b0ee50758e6ae71f3ff1265e5b231.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/edg1983/Singularity_images/qcbam-v1.0.def/2021-01-20-f4b53e73-0e6774fb/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/qcbam-v1.0.def/2021-01-20-f4b53e73-0e6774fb/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:qcbam-v1.0.def

```bash
$ singularity pull shub://edg1983/Singularity_images:qcbam-v1.0.def
```

## Singularity Recipe

```singularity
Bootstrap: library
From: centos:8

%labels
    Author Edoardo Giacopuzzi
    Contact edoardo.giacopuzzi@well.ox.ac.uk

%help
    Image with alignment tools:
    - fastqc v0.11.9
    - samtools v1.11
    - mosdepth v0.3.1
    - somalier v0.2.12
    - multiqc v1.9

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin
    LC_ALL=C.UTF-8

%post
    #yum update
    yum -y install \
        cmake \
        gcc \
        gcc-c++ \
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
        java-11-openjdk \
	procps

    yum -y groupinstall 'development tools'

    #install fastQC
    cd /opt
    wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip
    unzip fastqc_v0.11.9.zip
    rm fastqc_v0.11.9.zip
    cd FastQC/
    chmod 755 fastqc
    cd /usr/local/bin 
    ln -s /opt/FastQC/fastqc ./
    
    #install samtools
    cd /opt
    wget https://github.com/samtools/samtools/releases/download/1.11/samtools-1.11.tar.bz2
    tar -jxvf samtools-1.11.tar.bz2
    rm samtools-1.11.tar.bz2
    cd samtools-1.11
    ./configure
    make
    make install

    #install mosdepth
    cd /usr/local/bin
    wget https://github.com/brentp/mosdepth/releases/download/v0.3.1/mosdepth
    chmod 755 mosdepth

    #install somalier 
    wget https://github.com/brentp/somalier/releases/download/v0.2.12/somalier
    chmod 755 somalier

    #install multiqc
    pip3 install multiqc

%test
    samtools --version
    somalier
    mosdepth -h
    multiqc --help
    fastqc --help
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

