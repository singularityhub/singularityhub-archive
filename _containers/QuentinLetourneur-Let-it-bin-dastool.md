---
id: 4616
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "dastool"
commit: "8988e8717cfe4a73ada9cc0e84dc0019a0dfcfbe"
version: "52def799b68117db99a8763cde210f15"
build_date: "2018-09-03T17:16:24.278Z"
size_mb: 1571
size: 623177759
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/dastool/2018-09-03-8988e871-52def799/52def799b68117db99a8763cde210f15.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/dastool/2018-09-03-8988e871-52def799/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/dastool/2018-09-03-8988e871-52def799/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:dastool

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:dastool
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget zip build-essential ruby zlib1g zlib1g-dev libtool m4 automake libpcre3 libpcre3-dev
    
    cd /home
    wget https://cran.r-project.org/bin/linux/ubuntu/xenial/r-base-core_3.4.1-2xenial0_amd64.deb
    apt -y install ./r-base-core_3.4.1-2xenial0_amd64.deb
    rm r-base-core_3.4.1-2xenial0_amd64.deb
    R --vanilla -e 'install.packages("data.table", repo="http://mirror.ibcp.fr/pub/CRAN/")'
    R --vanilla -e 'install.packages("doMC", repo="http://mirror.ibcp.fr/pub/CRAN/")'
    R --vanilla -e 'install.packages("ggplot2", repo="http://mirror.ibcp.fr/pub/CRAN/")'
    
    wget https://github.com/bcthomas/pullseq/archive/1.0.2.zip
    unzip 1.0.2.zip
    rm 1.0.2.zip
    cd pullseq-1.0.2
    ./bootstrap
    ./configure
    make
    make install
    
    cd /home
    wget https://github.com/hyattpd/Prodigal/archive/v2.6.3.zip
    unzip v2.6.3.zip
    rm v2.6.3.zip
    cd Prodigal-2.6.3
    make install
    
    cd /home
    wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/ncbi-blast-2.2.31+-x64-linux.tar.gz
    tar -xzf ncbi-blast-2.2.31+-x64-linux.tar.gz
    rm ncbi-blast-2.2.31+-x64-linux.tar.gz
    mv ncbi-blast-2.2.31+/bin/* /usr/local/bin
    
    wget https://github.com/cmks/DAS_Tool/archive/1.1.0.zip
    unzip 1.1.0.zip
    rm 1.1.0.zip
    cd DAS_Tool-1.1.0
    R CMD INSTALL ./package/DASTool_1.1.0.tar.gz
    unzip db.zip
    
    chmod +x /home/DAS_Tool-1.1.0/DAS_Tool
    ln -s /home/DAS_Tool-1.1.0/DAS_Tool /usr/local/bin/
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

