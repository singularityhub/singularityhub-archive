---
id: 9064
name: "botaoliuphd/singularitysc"
branch: "master"
tag: "majiq2.1"
commit: "2fec43b0cd2a85ed25c17f69e987bc3edffb9515"
version: "71a5d84c832992b919b39b01a3e69f52"
build_date: "2019-08-06T14:45:04.970Z"
size_mb: 7240
size: 2455986207
sif: "https://datasets.datalad.org/shub/botaoliuphd/singularitysc/majiq2.1/2019-08-06-2fec43b0-71a5d84c/71a5d84c832992b919b39b01a3e69f52.simg"
url: https://datasets.datalad.org/shub/botaoliuphd/singularitysc/majiq2.1/2019-08-06-2fec43b0-71a5d84c/
recipe: https://datasets.datalad.org/shub/botaoliuphd/singularitysc/majiq2.1/2019-08-06-2fec43b0-71a5d84c/Singularity
collection: botaoliuphd/singularitysc
---

# botaoliuphd/singularitysc:majiq2.1

```bash
$ singularity pull shub://botaoliuphd/singularitysc:majiq2.1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR Alper Kucukural <alper.kucukural@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/usr/local/bin/dolphin-bin:/usr/bin/bcl2fastq2-v2.17.1.14/bin:/usr/local/bin/dolphin-bin/tophat-2.0.14.Linux_x86_64:/usr/local/bin/dolphin-bin/kraken:/usr/local/bin/dolphin-bin/samtools-1.2:/usr/bin/subread-1.6.4-Linux-x86_64/bin:/usr/local/bin/julia/bin:/usr/local/bin/sratoolkit/bin:/home/botaoliu/.cargo/bin:/usr/local/bin/matt
    export PATH

%post
    apt-get update
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim \
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
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  apt-get install -y ant && \
  apt-get clean;

  # Fix certificate issues
  apt-get update && \
  apt-get install ca-certificates-java && \
  apt-get clean && \
  update-ca-certificates -f;

    ###################
    ## NEXTFLOW
    ###################

    export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
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
#    wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/Software/bcl2fastq/bcl2fastq2-v2.17.1.14.tar.zip
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
	pip install umi_tools==0.5.5


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

  #################
  ##subread-featureCounts
  ##################
  cd /usr/bin/
  wget https://galaxyweb.umassmed.edu/pub/software/subread-1.6.4-Linux-x86_64.tar.gz
  tar zxvf subread-1.6.4-Linux-x86_64.tar.gz

    ## The following package are added by Botao ##

    #################
    ## whippet ##
    #################

    cd /tmp
    wget https://julialang-s3.julialang.org/bin/linux/x64/0.6/julia-0.6.4-linux-x86_64.tar.gz
    tar -xvzf julia-0.6.4-linux-x86_64.tar.gz
    mkdir /usr/local/bin/julia
    mv julia-9d11f62bcb/* /usr/local/bin/julia
    # Haven't figure out how to install julia package from command line.

    #################
    ## dexseq ##
    #################
    apt-get install -y build-essential python-matplotlib python-htseq
    pip install 'HTSeq==0.11.0'


    #################
    ## majiq 2.1 ##
    #################
    cd /tmp
    wget "https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2"
    tar -vxjf htslib-1.9.tar.bz2
    cd htslib-1.9
    make
    make install

    apt-get install -y python3-dev python3-pip
    pip3 install virtualenv awscli
    pip3 install pip
    pip3 install wheel setuptools
    pip3 install cython numpy GitPython
    pip3 install Flask==1.0.2 Flask-WTF==0.14.2 gunicorn==19.9.0
    pip3 install h5py>=2.8.0 psutil>=5.4.8 scipy>=1.1.0 waitress==1.1.0
    pip3 install git+https://bitbucket.org/biociphers/majiq_stable.git#egg=majiq

    #################
    ## sratoolkit ###
    #################
    cd /tmp
    wget "https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.2/sratoolkit.2.9.2-ubuntu64.tar.gz"
    tar -xvzf sratoolkit.2.9.2-ubuntu64.tar.gz
    mkdir /usr/local/bin/sratoolkit
    mv sratoolkit.2.9.2-ubuntu64/* /usr/local/bin/sratoolkit

    #################
    ##### rMATS #####
    #################
    cd /tmp
    wget "http://mirrors.kernel.org/ubuntu/pool/main/g/gsl/libgsl0ldbl_1.16+dfsg-1ubuntu1_amd64.deb"
    dpkg -i libgsl0ldbl_1.16+dfsg-1ubuntu1_amd64.deb

    #################
    ##### Matt  #####
    #################
    cd /usr/local/bin
    mkdir matt
    cd matt
    wget matt.crg.eu/matt.tar.gz
    tar -xvzf matt.tar.gz
    ./INSTALL
```

## Collection

 - Name: [botaoliuphd/singularitysc](https://github.com/botaoliuphd/singularitysc)
 - License: None

