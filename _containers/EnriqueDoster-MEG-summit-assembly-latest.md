---
id: 4845
name: "EnriqueDoster/MEG-summit-assembly"
branch: "master"
tag: "latest"
commit: "b1f2fc0069f4d8db2ed8393c288cdcc81211a8b1"
version: "7d5ffd60364f9ef55079fe1e5fe9a872"
build_date: "2019-10-10T19:31:22.717Z"
size_mb: 1745
size: 681218079
sif: "https://datasets.datalad.org/shub/EnriqueDoster/MEG-summit-assembly/latest/2019-10-10-b1f2fc00-7d5ffd60/7d5ffd60364f9ef55079fe1e5fe9a872.simg"
url: https://datasets.datalad.org/shub/EnriqueDoster/MEG-summit-assembly/latest/2019-10-10-b1f2fc00-7d5ffd60/
recipe: https://datasets.datalad.org/shub/EnriqueDoster/MEG-summit-assembly/latest/2019-10-10-b1f2fc00-7d5ffd60/Singularity
collection: EnriqueDoster/MEG-summit-assembly
---

# EnriqueDoster/MEG-summit-assembly:latest

```bash
$ singularity pull shub://EnriqueDoster/MEG-summit-assembly:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie-slim

#Includes idba, trimmomatic, samtools, bwa, bedtools, freebayes, bbmap, resistomeanalyzer, rarefactionanalyzer

%environment

%post
    ## Jave install doesn't work, but can load java module from summit
    apt update \
    && apt install -y --no-install-recommends \
    build-essential ca-certificates sudo \
    git make automake autoconf wget unzip sed \
    zlib1g-dev curl libbz2-dev locales libncurses5-dev liblzma-dev libcurl4-openssl-dev software-properties-common apt-transport-https\
    python3-pip python3-docopt python3-pytest python-dev python3-dev\
    libcurl4-openssl-dev libssl-dev zlib1g-dev fonts-texgyre \
    gcc g++ gfortran libblas-dev liblapack-dev dos2unix tabix \
    r-base-core r-recommended hmmer\
    && rm -rf /var/lib/apt/lists/*

    python3 -m pip install biopython


    ## IDBA
    cd /opt
    git clone https://github.com/loneknightpy/idba \
    && cd idba \
    && sed -i 's/kMaxShortSequence = 128/kMaxShortSequence = 500/' src/sequence/short_sequence.h \
    && ./build.sh \
    && make
    cd /usr/local/bin
    ln -s /opt/idba/bin/idba_ud
    ln -s /opt/idba/bin/fq2fa
    cd /

    ## Trimmomatic
    TRIMMOMATIC_SOURCE="Trimmomatic-0.36.zip" \
    TRIMMOMATIC_HOME="/opt/trimmomatic"
    wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip -O /opt/trimmomatic.zip && \
    unzip /opt/trimmomatic.zip -d /opt/ && \
    rm /opt/trimmomatic.zip
    cd /

    ## BWA #/usr/local/bin/bwa
    cd /usr/local/
    mkdir install_bwa
    cd install_bwa
    git clone https://github.com/lh3/bwa.git
    cd bwa; make
    rm -r .git*
    rm .travis.yml
    rm READ*
    rm CO*
    rm Ch*
    rm NEWS.md
    rm Makefile
    ln -s /usr/local/install_bwa/bwa/* /usr/local/bin/
    cd /

    ## SAMTOOLS
    cd /usr/local/
    HTSLIB_VERSION=1.9 # indexes versions for samtools and bcftools
    wget https://github.com/samtools/samtools/releases/download/1.9/samtools-${HTSLIB_VERSION}.tar.bz2
    tar xvjf samtools-${HTSLIB_VERSION}.tar.bz2
    cd samtools-${HTSLIB_VERSION}
    autoheader
    autoconf -Wno-syntax
    ./configure --prefix /usr/local/bin
    make
    make install
    ln -s /usr/local/samtools-${HTSLIB_VERSION}/* /usr/local/bin/
    cd /

    # Bedtools
    cd /usr/local/
    wget https://github.com/arq5x/bedtools2/releases/download/v2.25.0/bedtools-2.25.0.tar.gz
    tar -zxvf bedtools-2.25.0.tar.gz
    cd bedtools2
    make
    ln -s /usr/local/bedtools2/bin/* /usr/local/bin/
    cd /

    # freebayes
    cd /usr/local
    git clone --recursive git://github.com/ekg/freebayes.git
    cd freebayes
    make
    ln -s /usr/local/freebayes/bin/* /usr/local/bin/
    ln -s /usr/local/freebayes/vcflib/bin/* /usr/local/bin/
    cd /

    # bbmap
    cd /usr/local
    wget https://sourceforge.net/projects/bbmap/files/latest/download
    tar xzf download
    ln -s /usr/local/bbmap/* /usr/local/bin/
    cd /
    export JAVA_HOME=`/usr/lib/jvm/java-7-openjdk-amd64/bin/java`
    
    # resistomeanalyzer
    cd /usr/local
    git clone https://github.com/cdeanj/resistomeanalyzer.git
    cd resistomeanalyzer
    make
    cp resistome /usr/local/bin
    #ln -s /usr/local/resistomeanalyzer/* /usr/local/bin/
    cd /

    # RarefactionAnalyzer
    cd /usr/local
    git clone https://github.com/cdeanj/RarefactionAnalyzer.git
    cd RarefactionAnalyzer
    make
    cp rarefaction /usr/local/bin
    cd /

    ## SNPfinder
    cd /usr/local
    git clone https://github.com/cdeanj/snpfinder.git
    cd snpfinder
    make
    cp snpfinder /usr/local/bin
    cd /
    
    # Install VCF tools
    cd /usr/local
    git clone --recursive git://github.com/ekg/vcflib.git
    cd vcflib
    make
    ln -s /usr/local/vcflib/bin/* /usr/local/bin/
    cd /
    
    ## htslib
    cd /usr/local/
    HTSLIB_VERSION=1.9 # indexes versions for samtools and bcftools
    wget https://github.com/samtools/htslib/releases/download/1.9/htslib-${HTSLIB_VERSION}.tar.bz2
    tar xvjf htslib-${HTSLIB_VERSION}.tar.bz2
    cd htslib-${HTSLIB_VERSION}
    autoheader
    autoconf -Wno-syntax
    ./configure --prefix /usr/local/bin
    make
    make install
    echo 'export PATH=$PATH:$(pwd)' >>$SINGULARITY_ENVIRONMENT
    cd /

    # Install kraken
    cd /usr/local
    git clone https://github.com/DerrickWood/kraken2.git
    cd kraken2/
    ./install_kraken2.sh /usr/local/kraken2
    cp /usr/local/kraken2/kraken2 /usr/local/bin
    cp /usr/local/kraken2/kraken2-build /usr/local/bin
    cp /usr/local/kraken2/kraken2-inspect /usr/local/bin
    cd /
    
%test
```

## Collection

 - Name: [EnriqueDoster/MEG-summit-assembly](https://github.com/EnriqueDoster/MEG-summit-assembly)
 - License: [MIT License](https://api.github.com/licenses/mit)

