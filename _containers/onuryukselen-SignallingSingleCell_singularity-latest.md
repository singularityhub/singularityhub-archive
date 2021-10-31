---
id: 3454
name: "onuryukselen/SignallingSingleCell_singularity"
branch: "master"
tag: "latest"
commit: "81689462fd4665457fd873340b8921570ee354e7"
version: "262b2a0c0b8a9a59132b578a323b50ab"
build_date: "2018-07-29T13:44:02.861Z"
size_mb: 3494
size: 1247858719
sif: "https://datasets.datalad.org/shub/onuryukselen/SignallingSingleCell_singularity/latest/2018-07-29-81689462-262b2a0c/262b2a0c0b8a9a59132b578a323b50ab.simg"
url: https://datasets.datalad.org/shub/onuryukselen/SignallingSingleCell_singularity/latest/2018-07-29-81689462-262b2a0c/
recipe: https://datasets.datalad.org/shub/onuryukselen/SignallingSingleCell_singularity/latest/2018-07-29-81689462-262b2a0c/Singularity
collection: onuryukselen/SignallingSingleCell_singularity
---

# onuryukselen/SignallingSingleCell_singularity:latest

```bash
$ singularity pull shub://onuryukselen/SignallingSingleCell_singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin
    export PATH

%post
    apt-get update
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim \
    subversion g++ gcc gfortran libcurl4-openssl-dev curl

    ###################
    ## Python modules 
    ###################
	
	export LC_ALL=C
	pip install --upgrade pip==9.0.3
	pip install pysam
	pip install numpy scipy biopython

    ###################
    ## JAVA 
    ###################

    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java && \
    apt-get update && \
    apt-get install -y oracle-java8-installer && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /var/cache/oracle-jdk8-installer

    apt-get -y autoremove
    
    ###################
    ## NEXTFLOW 
    ###################

    export JAVA_HOME=/usr/lib/jvm/java-8-oracle
    mkdir /data && cd /data
    curl -s https://get.nextflow.io | bash 
    mv /data/nextflow /usr/bin/.
    mkdir /project /nl /share /.nextflow
    
    #################
    ## R ##
    #################
    NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
    cd /tmp 
    wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.8_amd64.deb
    dpkg -i libicu52_52.1-3ubuntu0.8_amd64.deb
    wget https://cran.rstudio.com/src/base/R-3/R-3.5.1.tar.gz
    tar xvf R-3.5.1.tar.gz
    cd /tmp/R-3.5.1
    apt-get update
    apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 ghostscript  libicu52
    apt-get install -y libgmp10 libgmp-dev
    apt-get install -y fort77 aptitude
    aptitude install -y xorg-dev
    aptitude install -y libreadline-dev
    apt install -y   libpcre3-dev liblzma-dev  
    apt-get update
    apt-get install -y bioperl
    apt-get update 
  
    ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes 
    echo "Will use make with $NPROCS cores."
    make -j${NPROCS}
    make install

    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite()"
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('scran')"
    echo install.packages\(\"devtools\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
    yes | apt-get install libmariadb-client-lgpl-dev
    R --slave -e "library(devtools); devtools::install_github('davismcc/scater', build_vignettes = TRUE)"
    echo install.packages\(\"rmarkdown\"\, dependencies = TRUE, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('scater')"
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('BiocStyle')"
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('destiny')"
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('mvoutlier')"
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('mvoutlier')"
    R --slave -e "library(devtools); install_github('garber-lab/SignallingSingleCell')"
    R --slave -e "library('SignallingSingleCell')"
    R --slave -e "library('SingleCellExperiment')"
```

## Collection

 - Name: [onuryukselen/SignallingSingleCell_singularity](https://github.com/onuryukselen/SignallingSingleCell_singularity)
 - License: None

