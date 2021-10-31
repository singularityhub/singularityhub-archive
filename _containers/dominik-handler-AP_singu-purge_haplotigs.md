---
id: 6556
name: "dominik-handler/AP_singu"
branch: "master"
tag: "purge_haplotigs"
commit: "a245049ab386be349c58c95156bdd100c78a0794"
version: "83a54648f5a0d6760a1a72caa99689d21d36227138f81637a336180aacceb622"
build_date: "2021-03-25T16:25:37.727Z"
size_mb: 535.16796875
size: 561164288
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_haplotigs/2021-03-25-a245049a-83a54648/83a54648f5a0d6760a1a72caa99689d21d36227138f81637a336180aacceb622.sif"
url: https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_haplotigs/2021-03-25-a245049a-83a54648/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/purge_haplotigs/2021-03-25-a245049a-83a54648/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:purge_haplotigs

```bash
$ singularity pull shub://dominik-handler/AP_singu:purge_haplotigs
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  purge_haplotigs 2019-12-10  

%runscript
    purge_haplotigs "$@"

%post
    #fix locale
    apt-get update
    apt-get -y install locales

    locale-gen en_US.UTF-8

    export LANG=en_US.UTF-8  
    export LANGUAGE=en_US:en  
    export LC_ALL=C

    #install commonly required tools
    apt-get -y  install sudo wget apt-transport-https build-essential software-properties-common lsb-release git python-dev
  
    #install samtools  
    apt-get --assume-yes install gcc make libbz2-dev zlib1g-dev libncurses5-dev libncursesw5-dev liblzma-dev tar libpng-dev uuid-dev

    cd /
    wget --quiet  https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
    tar -xjf htslib-1.9.tar.bz2
    cd htslib-1.9
    make
    make install

    cd /
    wget --quiet  https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
    tar -xjf samtools-1.9.tar.bz2
    cd samtools-1.9
    make   
    make install    
    
    #install bcftools
    cd /
    wget --quiet  https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
    tar -xjf bcftools-1.9.tar.bz2
    cd bcftools-1.9
    make
    make install

    #install bedtools
    cd /
    wget --quiet  --no-check-certificate --content-disposition https://github.com/arq5x/bedtools2/releases/download/v2.28.0/bedtools-2.28.0.tar.gz
    tar -zxf bedtools-2.28.0.tar.gz
    cd bedtools2
    make
    make install

    #install Rbase
    apt -y  install r-base r-base-dev
    su - -c "R -e \"install.packages('ggplot2', repos='http://cran.rstudio.com/')\""

    #install minimap2
    cd /
    wget https://github.com/lh3/minimap2/releases/download/v2.16/minimap2-2.16_x64-linux.tar.bz2
    tar xf minimap2-2.16_x64-linux.tar.bz2
    cp minimap2-2.16_x64-linux/minimap2 /usr/bin

    wget https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz
    tar xf mummer-4.0.0beta2.tar.gz
    cd mummer-4.0.0beta2
    ./configure
    make
    cd ../
    cp /mummer-4.0.0beta2/delta-filter /usr/bin/
    cp /mummer-4.0.0beta2/nucmer /usr/bin/
    cp /mummer-4.0.0beta2/show-coords /usr/bin/
    #@ ln -s /purge_haplotigs/mummer-4.0.0beta2/delta-filter /purge_haplotigs/bin/delta-filter
    #@ ln -s /purge_haplotigs/mummer-4.0.0beta2/nucmer /purge_haplotigs/bin/nucmer
    #@ ln -s /purge_haplotigs/mummer-4.0.0beta2/show-coords /purge_haplotigs/bin/show-coords


    #install purge haplotigs
    cd /

    git clone https://bitbucket.org/mroachawri/purge_haplotigs.git
    #cp /purge_haplotigs/bin/purge_haplotigs /usr/bin

%environment
    export PATH=$PATH:/purge_haplotigs/bin

%test
  export PATH=$PATH:/purge_haplotigs/bin
  purge_haplotigs test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

