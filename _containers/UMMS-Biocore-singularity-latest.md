---
id: 5822
name: "UMMS-Biocore/singularity"
branch: "master"
tag: "latest"
commit: "5a972f61af101dfa28be737fc4bb77229a8e6a10"
version: "72556467dbb838723882fb8404f66c01"
build_date: "2018-12-07T19:40:49.894Z"
size_mb: 5892
size: 2006487071
sif: "https://datasets.datalad.org/shub/UMMS-Biocore/singularity/latest/2018-12-07-5a972f61-72556467/72556467dbb838723882fb8404f66c01.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/UMMS-Biocore/singularity/latest/2018-12-07-5a972f61-72556467/
recipe: https://datasets.datalad.org/shub/UMMS-Biocore/singularity/latest/2018-12-07-5a972f61-72556467/Singularity
collection: UMMS-Biocore/singularity
---

# UMMS-Biocore/singularity:latest

```bash
$ singularity pull shub://UMMS-Biocore/singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Alper Kucukural <alper.kucukural@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/usr/local/bin/dolphin-bin:/usr/bin/bcl2fastq2-v2.17.1.14/bin:/usr/local/bin/dolphin-bin/tophat-2.0.14.Linux_x86_64:/usr/local/bin/dolphin-bin/kraken
    export PATH

%post
    apt-get update 
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim sed \
    subversion g++ gcc gfortran libcurl4-openssl-dev curl zlib1g-dev build-essential libffi-dev  python-lzo
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
    mkdir -p /project /nl /share /.nextflow
    
    #################
    ## Dolphin-bin ##
    #################
    export GITUSER=UMMS-Biocore

    git clone https://github.com/${GITUSER}/dolphin-bin /usr/local/bin/dolphin-bin

    pip install -U boto
    pip install --upgrade pip    
    pip install RSeQC

    cd /usr/local/bin/dolphin-bin/MACS2 && python setup.py install
    make -C /usr/local/bin/dolphin-bin/RSEM-1.2.29
    
    ##kraken
    chmod 777 /usr/local/bin/dolphin-bin/kraken/*
    
    ###tophat-2.0.14
    cd /tmp
    wget https://ccb.jhu.edu/software/tophat/downloads/tophat-2.0.14.Linux_x86_64.tar.gz
    tar -xvzf tophat-2.0.14.Linux_x86_64.tar.gz
    rm -rf /usr/local/bin/dolphin-bin/tophat2_2.0.12
    mv tophat-2.0.14.Linux_x86_64/ /usr/local/bin/dolphin-bin/.

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
    git clone https://github.com/onuryukselen/singularity /tmp/singularity
    cd ${TMP}
    wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/Software/bcl2fastq/bcl2fastq2-v2.17.1.14.tar.zip
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
    ## UMI-TOOLS
    #################
	pip install umi_tools

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
    R --slave -e "install.packages(c('devtools', 'gplots', 'R.utils', 'RColorBrewer'), dependencies = TRUE, repos='https://cloud.r-project.org', Ncpus=${NPROCS})"
    R --slave -e "BiocManager::install(c('XVector', 'GenomicRanges','ShortRead', 'scran'), version = '3.8')"
    sed -i 's/, ignoreSelf=TRUE//g' /usr/local/bin/dolphin-bin/kraken/seqimp-13-274/bin/miR_table.R
```

## Collection

 - Name: [UMMS-Biocore/singularity](https://github.com/UMMS-Biocore/singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

