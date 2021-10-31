---
id: 11868
name: "onuryukselen/singularity-cellranger"
branch: "master"
tag: "latest"
commit: "8b7245657eb46cfc90c600dd8df974a10e700adc"
version: "05bfcab713a3e906a49e75c41e981aa3"
build_date: "2020-11-13T09:03:34.383Z"
size_mb: 12054.0
size: 5308686367
sif: "https://datasets.datalad.org/shub/onuryukselen/singularity-cellranger/latest/2020-11-13-8b724565-05bfcab7/05bfcab713a3e906a49e75c41e981aa3.sif"
url: https://datasets.datalad.org/shub/onuryukselen/singularity-cellranger/latest/2020-11-13-8b724565-05bfcab7/
recipe: https://datasets.datalad.org/shub/onuryukselen/singularity-cellranger/latest/2020-11-13-8b724565-05bfcab7/Singularity
collection: onuryukselen/singularity-cellranger
---

# onuryukselen/singularity-cellranger:latest

```bash
$ singularity pull shub://onuryukselen/singularity-cellranger:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/usr/bin/bcl2fastq2-v2.17.1.14/bin:/usr/bin/cellranger-3.0.2:/usr/bin/cellranger-atac-1.2.0
    export PATH
    export LC_ALL=C

%post
    apt-get update 
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev  liblzma-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim sed make libncurses5-dev libncursesw5-dev\
    subversion g++ gcc gfortran libcurl4-openssl-dev curl zlib1g-dev build-essential libffi-dev  python-lzo libxml-libxml-perl 
 
    pip install --upgrade pip==9.0.3
    pip install pysam==0.15.2
    pip install numpy scipy biopython
    pip install --upgrade pip    
    pip install multiqc

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
    apt-get update
    apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 ghostscript \
    libgmp10 libgmp-dev fort77 aptitude libpcre3-dev liblzma-dev libmariadb-client-lgpl-dev pandoc libhdf5-dev \
    libx11-dev libxt-dev qpdf  xvfb xauth xfonts-base xorg libx11-dev libglu1-mesa-dev libfreetype6-dev \
    libx11-6 libxss1 libxt6 libxext6 libsm6 libice6 xdg-utils libbz2-dev libcairo2-dev libcurl4-openssl-dev libpango1.0-dev \
    libjpeg-dev libicu-dev  libpcre3-dev libpng-dev libreadline-dev libtiff5-dev liblzma-dev  libx11-dev libxt-dev tcl8.6-dev \
    texinfo tk8.6-dev texlive-extra-utils texlive-fonts-recommended texlive-fonts-extra texlive-latex-recommended x11proto-core-dev \
    zlib1g-dev  fonts-texgyre libblas-dev libbz2-1.0  libopenblas-dev libpangocairo-1.0-0 libpcre3 libpng16-16 \
    libtiff5 liblzma5 zlib1g
    aptitude install -y xorg-dev libreadline-dev libcurl4-openssl-dev
    
    NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo` && \
    cd /tmp && wget http://security.ubuntu.com/ubuntu/pool/main/i/icu/libicu52_52.1-3ubuntu0.8_amd64.deb && \
    dpkg -i libicu52_52.1-3ubuntu0.8_amd64.deb && wget https://cran.rstudio.com/src/base/R-3/R-3.5.1.tar.gz && \
    tar xvf R-3.5.1.tar.gz && cd /tmp/R-3.5.1 && ./configure --enable-memory-profiling  --with-readline  --with-blas --with-tcltk  --with-recommended-packages --with-libpng --with-libtiff --with-jpeglib --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes && \
    make -j${NPROCS} && make install
    
    apt-get install -y bioperl
    apt-get update 
    
    R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite()"
    R --slave -e "install.packages(c('devtools', 'gplots', 'R.utils'), dependencies = TRUE, repos='https://cloud.r-project.org', Ncpus=${NPROCS})"
    R --slave -e "BiocManager::install(c('multtest'))"
    R --slave -e "install.packages(c('Seurat', 'rmarkdown'), dependencies = TRUE, repos='https://cloud.r-project.org', Ncpus=${NPROCS})"
    R --slave -e "install.packages(c('RColorBrewer', 'Cairo'), dependencies = TRUE, repos='https://cloud.r-project.org', Ncpus=${NPROCS})"
    
    #X11 display fix
    Xvfb :0 -ac -screen 0 1960x2000x24 &

    #################
    ## Cell Ranger ##
    #################

    cd /usr/bin
    wget https://galaxyweb.umassmed.edu/pub/software/cellranger-3.0.2.tar.gz
    tar -xzvf cellranger-3.0.2.tar.gz

    ######################
    ## Cell Ranger-ATAC ##
    ######################

   wget https://galaxyweb.umassmed.edu/pub/software/cellranger-atac-1.2.0.tar.gz
   tar -xzvf cellranger-atac-1.2.0.tar.gz
```

## Collection

 - Name: [onuryukselen/singularity-cellranger](https://github.com/onuryukselen/singularity-cellranger)
 - License: None

