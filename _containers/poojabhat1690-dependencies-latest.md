---
id: 11201
name: "poojabhat1690/dependencies"
branch: "master"
tag: "latest"
commit: "93a993c7023d85f08125b17620baf44738f6c02d"
version: "fb4293b43518eac8d8e1ae98bbc5626d"
build_date: "2021-03-15T19:57:40.455Z"
size_mb: 1667.0
size: 611991583
sif: "https://datasets.datalad.org/shub/poojabhat1690/dependencies/latest/2021-03-15-93a993c7-fb4293b4/fb4293b43518eac8d8e1ae98bbc5626d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/poojabhat1690/dependencies/latest/2021-03-15-93a993c7-fb4293b4/
recipe: https://datasets.datalad.org/shub/poojabhat1690/dependencies/latest/2021-03-15-93a993c7-fb4293b4/Singularity
collection: poojabhat1690/dependencies
---

# poojabhat1690/dependencies:latest

```bash
$ singularity pull shub://poojabhat1690/dependencies:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From:ubuntu:16.04





%post


    apt-get -y update
  apt-get install -y libopenblas-dev  libcurl4-openssl-dev libopenmpi-dev openmpi-bin openmpi-common openmpi-doc openssh-client openssh-server libssh-dev wget vim git nano git cmake  gfortran g++ curl wget python autoconf bzip2 libtool libtool-bin

        apt-get -y install bedtools
    apt-get -y  install python3-dev python3-pip

    apt-get -y install fastqc
    apt-get -y install fastx-toolkit
    #apt-get -y install r-base

        #### install samtools and dependencies
        apt-get -y install gcc
        apt-get -y install make
        apt-get -y install libbz2-dev
        apt-get -y install zlib1g-dev
        apt-get -y install libncurses5-dev
        apt-get -y install libncursesw5-dev
        apt-get -y install liblzma-dev


        cd /usr/bin
        wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
        tar -vxjf htslib-1.9.tar.bz2
        cd htslib-1.9
        make

        cd ..
        wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
        tar -vxjf samtools-1.9.tar.bz2
        cd samtools-1.9
        make


        cd ..
        wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
        tar -vxjf bcftools-1.9.tar.bz2
        cd bcftools-1.9
        make


        export PATH="$PATH:/usr/bin/bcftools-1.9"
        export PATH="$PATH:/usr/bin/samtools-1.9"
        export PATH="$PATH:/usr/bin/htslib-1.9"



        ###### install using pip
        pip3 install 'cutadapt'

	 apt-get install -y tzdata && \
        apt-get install -y software-properties-common && \
        add-apt-repository -y -u ppa:certbot/certbot && \
        apt-get install -y   r-base-core libxml2-dev



R --slave -e 'source("https://bioconductor.org/biocLite.R")'
R --slave -e 'BiocInstaller::biocLite(c("GenomicRanges"))'
R --slave -e 'BiocInstaller::biocLite(c("biomaRt"))'
R --slave -e 'BiocInstaller::biocLite(c("Biostrings"))'
R --slave -e 'install.packages(c("checkmate", "ggplot2","reshape","dplyr","plyr","tibble"), repos="https://cloud.r-project.org/")'




%environment
export LC_ALL=C
export PATH=$PATH
```

## Collection

 - Name: [poojabhat1690/dependencies](https://github.com/poojabhat1690/dependencies)
 - License: None

