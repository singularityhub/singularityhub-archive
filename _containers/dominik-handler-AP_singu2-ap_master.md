---
id: 11356
name: "dominik-handler/AP_singu2"
branch: "master"
tag: "ap_master"
commit: "5ca8a8a6a8ca07d363bcd0f9ae85601ddd227e7b"
version: "6ba797583a270a47298a2663528cd134d3e06276110ef765880ecfeb04f4e34e"
build_date: "2021-03-18T14:53:10.831Z"
size_mb: 1302.609375
size: 1365884928
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu2/ap_master/2021-03-18-5ca8a8a6-6ba79758/6ba797583a270a47298a2663528cd134d3e06276110ef765880ecfeb04f4e34e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu2/ap_master/2021-03-18-5ca8a8a6-6ba79758/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu2/ap_master/2021-03-18-5ca8a8a6-6ba79758/Singularity
collection: dominik-handler/AP_singu2
---

# dominik-handler/AP_singu2:ap_master

```bash
$ singularity pull shub://dominik-handler/AP_singu2:ap_master
```

## Singularity Recipe

```singularity
Bootstrap: library
From: ubuntu:18.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at  
  all tools required for the AnnotationPipeline

%post    
  apt-get update
  apt-get -y install locales software-properties-common

  locale-gen en_US.UTF-8

  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=C
  mkdir /install

  #install all required tools
  add-apt-repository universe
  apt-get update

  apt-get update
  apt-get -y install parallel wget build-essential bzip2 python3-dev python3-setuptools python-dev unzip zip default-jre gawk curl cmake git-core autoconf zlib1g-dev rsync 
  
  wget --quiet  https://bootstrap.pypa.io/get-pip.py
  python3 get-pip.py
  pip3 install setuptools --upgrade

  #install enaTools
  cd /
  pip3 install chardet certifi
  wget --no-check-certificate --content-disposition  https://github.com/enasequence/enaBrowserTools/archive/v1.6.tar.gz
  tar -zxf enaBrowserTools-1.6.tar.gz
  rm -rf enaBrowserTools-1.6.tar.gz
  mv enaBrowserTools-1.6 enaBrowserTools

  #install samtools
    apt-get --assume-yes install gcc make libbz2-dev zlib1g-dev libncurses5-dev libncursesw5-dev liblzma-dev tar libpng-dev uuid-dev

    cd /install
    wget --quiet  https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
    tar -xjf htslib-1.9.tar.bz2
    cd htslib-1.9
    make
    make install

    cd /install
    wget --quiet  https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar -xjf samtools-1.9.tar.bz2
    cd samtools-1.9
    make   
    make install

    cd /install
    wget --quiet  https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar -xjf bcftools-1.9.tar.bz2
    cd bcftools-1.9
    make
    make install

  #install bedtools
    cd /install
    wget --quiet  --no-check-certificate --content-disposition https://github.com/arq5x/bedtools2/releases/download/v2.28.0/bedtools-2.28.0.tar.gz
    tar -zxf bedtools-2.28.0.tar.gz
    cd bedtools2
    make
    make install

  #install cutadapt
    pip3 install cutadapt
    
  #install illumina2bam
    cd /install/
    wget --quiet  https://github.com/wtsi-npg/illumina2bam/releases/download/V1.19/Illumina2bam-tools-V1.19.zip
    unzip Illumina2bam-tools-V1.19.zip
    chmod 777 /install/Illumina2bam-tools-V1.19/*
    mv Illumina2bam-tools-V1.19/* /usr/local/bin/

  #install seqkit
    cd /install
    wget --quiet  --no-check-certificate --content-disposition https://github.com/shenwei356/seqkit/releases/download/v0.11.0-dev/seqkit_linux_amd64.tar.gz
    tar -zxf seqkit_linux_amd64.tar.gz
    mv seqkit /usr/local/bin/

  #install bbtools
    cd /install
    wget --quiet  -O BBMap.tar.gz https://sourceforge.net/projects/bbmap/files/latest/download
    tar -zxf BBMap.tar.gz 
    mv bbmap/* /usr/local/bin/

  #install sra-toolkit
    cd /install
    wget --quiet  http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.6/sratoolkit.2.9.6-ubuntu64.tar.gz
    tar -xzf sratoolkit.2.9.6-ubuntu64.tar.gz
    mv sratoolkit.2.9.6-ubuntu64/bin/* /usr/local/bin/

  #install mawk v1.3.4
    cd /install
    wget --quiet  https://invisible-island.net/datafiles/release/mawk.tar.gz
    tar -xzf mawk.tar.gz
    cd mawk*
    ./configure
    make
    rm -rf /usr/bin/mawk
    cp mawk /usr/bin/
  
  #install bowtie v1.2.3
    cd /install
    wget --quiet  -O bowtie.zip https://sourceforge.net/projects/bowtie-bio/files/bowtie/1.2.3/bowtie-1.2.3-linux-x86_64.zip/download
    unzip bowtie.zip
    cp bowtie-1.2.3-linux-x86_64/bowtie* /usr/local/bin/

  #install STAR
    cd /install
    git clone https://github.com/alexdobin/STAR.git
    cd STAR/source && make
    cp /install/STAR/bin/Linux_x86_64/* /usr/local/bin/

  #kentUCSC
    apt-get update
    apt-get --assume-yes install mysql-client libssl-dev openssl libmysqlclient-dev
    apt-get clean  
    
    cd /install
    wget --quiet  http://hgdownload.soe.ucsc.edu/admin/exe/userApps.src.tgz 
    tar zxf userApps.src.tgz 
    cd userApps
    make
    mv bin/* /usr/local/bin/
    
  #salmon
    cd /install
    echo "deb http://cz.archive.ubuntu.com/ubuntu eoan main universe" |  tee -a  /etc/apt/sources.list
    apt update
    apt-get --assume-yes install libtbb-dev
    wget  https://github.com/COMBINE-lab/salmon/archive/v0.10.2.tar.gz
    tar zxf v0.10.2.tar.gz 
    cd salmon-0.10.2 
    mkdir build
    cd build
    cmake -DFETCH_BOOST=TRUE -DCMAKE_INSTALL_PREFIX=/usr/local/ ..
    make
    make install
    
    #install homer
    apt-get update
    apt-get -y install perl

    mkdir -p /homer/
    cd /homer
    wget --quiet  http://homer.ucsd.edu/homer/configureHomer.pl
    perl /homer/configureHomer.pl -install

  #clean up and make container smaller
    rm -rf /install
   
%environment
  #!/bin/bash
  export LANG=en_US.UTF-8  
  export LANGUAGE=en_US:en  
  export LC_ALL=C
  export PATH=/homer/bin:$PATH
  alias enaDataGet=/enaBrowserTools/python3/enaDataGet
  alias enaGroupGet=/enaBrowserTools/python3/enaGroupGet

%runscript
  $@
```

## Collection

 - Name: [dominik-handler/AP_singu2](https://github.com/dominik-handler/AP_singu2)
 - License: None

