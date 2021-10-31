---
id: 14533
name: "edg1983/Singularity_images"
branch: "master"
tag: "aligndedup-v1.0.def"
commit: "3899fa9f414d2c201b812c4b9b19153f25b6e287"
version: "f8e258afa22a02287f92b182cc72d0b139c24efadf48434f3597daaf564e63bd"
build_date: "2020-10-02T07:32:14.682Z"
size_mb: 274.640625
size: 287981568
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/aligndedup-v1.0.def/2020-10-02-3899fa9f-f8e258af/f8e258afa22a02287f92b182cc72d0b139c24efadf48434f3597daaf564e63bd.sif"
url: https://datasets.datalad.org/shub/edg1983/Singularity_images/aligndedup-v1.0.def/2020-10-02-3899fa9f-f8e258af/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/aligndedup-v1.0.def/2020-10-02-3899fa9f-f8e258af/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:aligndedup-v1.0.def

```bash
$ singularity pull shub://edg1983/Singularity_images:aligndedup-v1.0.def
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
    - bwa v0.7.17
    - bwa.kit v0.7.15
    - samtools v1.11
    - samblaster v0.1.26

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
	procps
        #apt-transport-https \
        #build-essential \
        #language-pack-en-base \
    
    #localectl set-locale LANG=en_US.UTF-8

    #install bwa
    cd /opt
    wget https://github.com/lh3/bwa/releases/download/v0.7.17/bwa-0.7.17.tar.bz2
    tar -jxvf bwa-0.7.17.tar.bz2
    rm bwa-0.7.17.tar.bz2
    cd bwa-0.7.17
    make
    cd /usr/local/bin
    ln -s /opt/bwa-0.7.17/bwa ./

    #install bwa.kit
    cd /opt
    wget -O bwakit-0.7.15.tar.bz2 https://sourceforge.net/projects/bio-bwa/files/bwakit/bwakit-0.7.15_x64-linux.tar.bz2/download
    tar -jxvf bwakit-0.7.15.tar.bz2
    rm bwakit-0.7.15.tar.bz2
    cd /usr/local/bin 
    ln -s /opt/bwa.kit/k8 ./

    #install samtools
    cd /opt
    wget https://github.com/samtools/samtools/releases/download/1.11/samtools-1.11.tar.bz2
    tar -jxvf samtools-1.11.tar.bz2
    rm samtools-1.11.tar.bz2
    cd samtools-1.11
    ./configure
    make
    make install

    #install samblaster
    cd /opt
    wget https://github.com/GregoryFaust/samblaster/releases/download/v.0.1.26/samblaster-v.0.1.26.tar.gz
    tar -zxvf samblaster-v.0.1.26.tar.gz
    rm samblaster-v.0.1.26.tar.gz
    cd samblaster-v.0.1.26
    make
    cd /usr/local/bin
    ln -s /opt/samblaster-v.0.1.26/samblaster ./

%test
    samtools --version
    k8 /opt/bwa.kit/bwa-postalt.js -v
    samblaster --version
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

