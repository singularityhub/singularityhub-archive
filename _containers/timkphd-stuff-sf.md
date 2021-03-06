---
id: 10493
name: "timkphd/stuff"
branch: "master"
tag: "sf"
commit: "77b31172b29167c350294295b01eeb94be3cf004"
version: "c741b9160a2ce2b1e1185ef7f04bf70c252d8681ac277088a657afbc75e7fdea"
build_date: "2020-04-16T15:17:55.004Z"
size_mb: 882.8828125
size: 925769728
sif: "https://datasets.datalad.org/shub/timkphd/stuff/sf/2020-04-16-77b31172-c741b916/c741b9160a2ce2b1e1185ef7f04bf70c252d8681ac277088a657afbc75e7fdea.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/timkphd/stuff/sf/2020-04-16-77b31172-c741b916/
recipe: https://datasets.datalad.org/shub/timkphd/stuff/sf/2020-04-16-77b31172-c741b916/Singularity
collection: timkphd/stuff
---

# timkphd/stuff:sf

```bash
$ singularity pull shub://timkphd/stuff:sf
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

#initial was 18.04 built on mac with 16.04
#MAINTAINER bhaas@broadinstitute.org

%post
apt-get update && apt-get install -y gcc g++ perl python3 automake make \
                                       wget curl libdb-dev \
				       bzip2 zlibc zlib1g zlib1g-dev  default-jre \
                       python-setuptools python-dev python3-dev build-essential \
				       unzip libbz2-dev  liblzma-dev && \
    apt-get clean



ln -sf /usr/bin/python3 /usr/bin/python

#next line broke on 16.04
apt-get install -y python3-distutils

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python get-pip.py


pip install numpy requests igv-reports


curl -L https://cpanmin.us | perl - App::cpanminus

## set up tool config and deployment area:

export SRC=/usr/local/src
export BIN=/usr/local/bin

export DATA=/usr/local/data
mkdir $DATA


## perl lib installations

cpanm install PerlIO::gzip
cpanm install Set::IntervalTree  # now included w/ STAR-Fusion
cpanm install DB_File
cpanm install URI::Escape
cpanm install Carp::Assert
cpanm install JSON::XS.pm

########
# Samtools


 
export SAMTOOLS_VERSION=1.7

SAMTOOLS_URL="https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2" && \
   cd $SRC && \
   wget $SAMTOOLS_URL && \
   tar xvf samtools-${SAMTOOLS_VERSION}.tar.bz2 && \
   cd samtools-${SAMTOOLS_VERSION}/htslib-${SAMTOOLS_VERSION} && ./configure && make && make install && \
   cd ../ && ./configure --without-curses && make && make install


########
# Trinity

apt-get install -y cmake

export TRINITY_VERSION=2.8.4

TRINITY_URL="https://github.com/trinityrnaseq/trinityrnaseq/archive/Trinity-v${TRINITY_VERSION}.tar.gz" && \
   cd $SRC && \
   wget $TRINITY_URL && \
   tar xvf Trinity-v${TRINITY_VERSION}.tar.gz && \
   cd trinityrnaseq-Trinity-v${TRINITY_VERSION} && make


export TRINITY_HOME=/usr/local/src/trinityrnaseq-Trinity-v${TRINITY_VERSION}


## Bowtie2
cd $SRC
wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.3.3.1/bowtie2-2.3.3.1-linux-x86_64.zip/download -O bowtie2-2.3.3.1-linux-x86_64.zip && \
    unzip bowtie2-2.3.3.1-linux-x86_64.zip && \
    mv bowtie2-2.3.3.1-linux-x86_64/bowtie2* $BIN && \
    rm *.zip && \
    rm -r bowtie2-2.3.3.1-linux-x86_64

## Jellyfish
cd $SRC
wget https://github.com/gmarcais/Jellyfish/releases/download/v2.2.7/jellyfish-2.2.7.tar.gz && \
    tar xvf jellyfish-2.2.7.tar.gz && \
    cd jellyfish-2.2.7/ && \
    ./configure && make && make install
            
## Salmon
cd $SRC
wget https://github.com/COMBINE-lab/salmon/releases/download/v0.9.1/Salmon-0.9.1_linux_x86_64.tar.gz && \
    tar xvf Salmon-0.9.1_linux_x86_64.tar.gz && \
    ln -s $SRC/Salmon-latest_linux_x86_64/bin/salmon $BIN/.




##############
## STAR

export STAR_VERSION=2.7.0f
STAR_URL="https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz" &&\
    wget -P $SRC $STAR_URL &&\
    tar -xvf $SRC/${STAR_VERSION}.tar.gz -C $SRC && \
    mv $SRC/STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/local/bin



########
# GMAP  (compile this last because this version unfortunately disrupts some headers in DL_LIBRARY_PATH)

export GMAP_VERSION=2017-11-15
cd $SRC
GMAP_URL="http://research-pub.gene.com/gmap/src/gmap-gsnap-$GMAP_VERSION.tar.gz" && \
    wget $GMAP_URL && \
    tar xvf gmap-gsnap-$GMAP_VERSION.tar.gz && \
    cd gmap-$GMAP_VERSION && ./configure && make && make install


apt-get clean && apt-get update && apt-get install -y locales
locale-gen en_US.UTF-8

###############
## STAR-Fusion:
cd $SRC

export STAR_FUSION_VERSION=1.6.0
export STARF_CHECKOUT=c465cf33d111121f6be127483379bebd2f866fbd


apt-get update && apt-get install -y git

git clone https://github.com/STAR-Fusion/STAR-Fusion.git && \
     cd STAR-Fusion && \
     git checkout $STARF_CHECKOUT && \
     git submodule init && git submodule update && \
     cd FusionInspector && \
     git submodule init && git submodule update

export STAR_FUSION_HOME=$SRC/STAR-Fusion

%environment

export SRC=/usr/local/src
export BIN=/usr/local/bin
export DATA=/usr/local/data
export SAMTOOLS_VERSION=1.7
export TRINITY_VERSION=2.8.4
export TRINITY_HOME=/usr/local/src/trinityrnaseq-Trinity-v${TRINITY_VERSION}
export STAR_VERSION=2.7.0f
export GMAP_VERSION=2017-11-15
export STAR_FUSION_VERSION=1.6.0
export STARF_CHECKOUT=c465cf33d111121f6be127483379bebd2f866fbd
export STAR_FUSION_HOME=$SRC/STAR-Fusion


## FusionInspector and FusionAnnotator are bundled with STAR-Fusion

%labels
	Author bhaas@broadinstitute.org
```

## Collection

 - Name: [timkphd/stuff](https://github.com/timkphd/stuff)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

