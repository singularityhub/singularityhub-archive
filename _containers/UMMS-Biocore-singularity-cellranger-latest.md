---
id: 9068
name: "UMMS-Biocore/singularity-cellranger"
branch: "master"
tag: "latest"
commit: "f49c6a001a357ffa991d9a60e8103f57e03c35cd"
version: "8e153954fe7e47c6e1a891852e8e30f1"
build_date: "2019-05-14T23:21:57.555Z"
size_mb: 8571
size: 3771088927
sif: "https://datasets.datalad.org/shub/UMMS-Biocore/singularity-cellranger/latest/2019-05-14-f49c6a00-8e153954/8e153954fe7e47c6e1a891852e8e30f1.simg"
url: https://datasets.datalad.org/shub/UMMS-Biocore/singularity-cellranger/latest/2019-05-14-f49c6a00-8e153954/
recipe: https://datasets.datalad.org/shub/UMMS-Biocore/singularity-cellranger/latest/2019-05-14-f49c6a00-8e153954/Singularity
collection: UMMS-Biocore/singularity-cellranger
---

# UMMS-Biocore/singularity-cellranger:latest

```bash
$ singularity pull shub://UMMS-Biocore/singularity-cellranger:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/usr/local/bin/dolphin-bin:/usr/bin/bcl2fastq2-v2.17.1.14/bin:/usr/local/bin/dolphin-bin/tophat-2.0.14.Linux_x86_64:/usr/local/bin/dolphin-bin/kraken:/usr/local/bin/dolphin-bin/samtools-1.2:/usr/bin/cellranger-3.0.2
    export PATH

%post
    apt-get update 
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim sed \
    subversion g++ gcc gfortran libcurl4-openssl-dev curl zlib1g-dev build-essential libffi-dev  python-lzo
 
    pip install --upgrade pip==9.0.3
    pip install pysam
    pip install numpy scipy biopython
    export LC_ALL=C
    
    ###################
    ## JAVA 
    ###################
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

    # Fix certificate issues
    apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;
    which java
    
    ###################
    ## NEXTFLOW 
    ###################

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
which java
    mkdir /data && cd /data
    curl -s https://get.nextflow.io | bash 
    mv /data/nextflow /usr/bin/.
    mkdir -p /project /nl /share /.nextflow
    
    #################
    ## Dolphin-bin ##
    #################
    export GITUSER=UMMS-Biocore

    git clone https://github.com/${GITUSER}/dolphin-bin /usr/local/bin/dolphin-bin

    pip install -U boto
    pip install --upgrade pip    
    pip install RSeQC
    pip install multiqc

    make -C /usr/local/bin/dolphin-bin/RSEM-1.2.29
    
    ##kraken
    chmod 777 /usr/local/bin/dolphin-bin/kraken/*
    #################
    ## BCL2FASTQ v2.17.1.14
    #################
    add-apt-repository universe
    apt-get update
    apt-get -y install zip unzip zlibc libc6 libboost-all-dev cmake
    
    export TMP=/tmp/singularity/programs
    export SOURCE=${TMP}/bcl2fastq
    export BUILD=${TMP}/bcl2fastq2-v2.17.1.14-build
    export INSTALL_DIR=/usr/bin/bcl2fastq2-v2.17.1.14
    ## git clone https://github.com/onuryukselen/singularity /tmp/singularity
    mkdir -p /tmp/singularity/programs
    cd ${TMP}
    wget https://galaxyweb.umassmed.edu/pub/software/bcl2fastq2-v2.17.1.14.tar.zip
    ## wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/Software/bcl2fastq/bcl2fastq2-v2.17.1.14.tar.zip
    unzip bcl2fastq2-v2.17.1.14.tar.zip
    tar -xvzf bcl2fastq2-v2.17.1.14.tar.gz
    mkdir ${BUILD}
    cd ${BUILD}
    sed -i 's@HINTS ENV C_INCLUDE_PATH ENV CPATH ENV CPLUS_INCLUDE_PATH@HINTS ENV C_INCLUDE_PATH ENV CPATH ENV CPLUS_INCLUDE_PATH /usr/include/x86_64-linux-gnu/@g' ${SOURCE}/src/cmake/macros.cmake
    sed -i 's@boost::property_tree::xml_writer_make_settings@boost::property_tree::xml_writer_make_settings<ptree::key_type>@g' ${SOURCE}/src/cxx/lib/io/Xml.cpp
    ${SOURCE}/src/configure --prefix=${INSTALL_DIR}
    make
    make install
	

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
    apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 ghostscript  libicu52 \
    libgmp10 libgmp-dev fort77 aptitude libpcre3-dev liblzma-dev libmariadb-client-lgpl-dev
    aptitude install -y xorg-dev libreadline-dev
    apt-get install -y bioperl
    apt-get update 
  
    ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes 
    echo "Will use make with $NPROCS cores."
    make -j${NPROCS}
    make install
    
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite()"
    R --slave -e "install.packages(c('devtools', 'gplots', 'R.utils', 'Seurat'), dependencies = TRUE, repos='https://cloud.r-project.org', Ncpus=${NPROCS})"
    
    #################
    ## Cell Ranger ##
    #################

    cd /usr/bin
    wget https://galaxyweb.umassmed.edu/pub/software/cellranger-3.0.2.tar.gz
    tar -xzvf cellranger-3.0.2.tar.gz
```

## Collection

 - Name: [UMMS-Biocore/singularity-cellranger](https://github.com/UMMS-Biocore/singularity-cellranger)
 - License: None

