---
id: 11934
name: "EnriqueDoster/sing_biotools"
branch: "master"
tag: "latest"
commit: "9b32ac3fa96087b410f9f936ae7216fbf2017e8f"
version: "57d50ed527271d60d0a9989f303e6ff2"
build_date: "2021-03-07T16:21:16.054Z"
size_mb: 8349.0
size: 4487159839
sif: "https://datasets.datalad.org/shub/EnriqueDoster/sing_biotools/latest/2021-03-07-9b32ac3f-57d50ed5/57d50ed527271d60d0a9989f303e6ff2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/EnriqueDoster/sing_biotools/latest/2021-03-07-9b32ac3f-57d50ed5/
recipe: https://datasets.datalad.org/shub/EnriqueDoster/sing_biotools/latest/2021-03-07-9b32ac3f-57d50ed5/Singularity
collection: EnriqueDoster/sing_biotools
---

# EnriqueDoster/sing_biotools:latest

```bash
$ singularity pull shub://EnriqueDoster/sing_biotools:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie-slim

#Includes kSNP3 and LYVEset (couldn't get CFSAN-snp to work on this container)

%environment
    export LC_ALL=C

%post
    apt update \
    && apt install -y --no-install-recommends \
    build-essential ca-certificates sudo tcsh\
    git make automake autoconf wget gzip unzip sed\
    zlib1g-dev curl libbz2-dev locales libncurses5-dev liblzma-dev libcurl4-openssl-dev software-properties-common apt-transport-https\
    python3-pip python3-docopt python3-pytest python-dev python3-dev\
    libcurl4-openssl-dev libssl-dev zlib1g-dev fonts-texgyre \
    gcc g++ gfortran libblas-dev liblapack-dev dos2unix libstdc++6\
    r-base-core r-recommended hmmer\
    && rm -rf /var/lib/apt/lists/*

    # Not my favorite workaround, but to get cfsan snp to work with samtools, we have to change which libncurses library is used. Problem is anaconda doesn't have the right version of samtools.
    sudo ln -s /lib/x86_64-linux-gnu/libncursesw.so.5  /lib/x86_64-linux-gnu/libncursesw.so.6

    #Installing Anaconda 2 and Conda 4.5.11
    wget -c https://repo.continuum.io/archive/Anaconda2-5.3.0-Linux-x86_64.sh
    sh Anaconda2-5.3.0-Linux-x86_64.sh -bfp /usr/local

    # add bioconda channels
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda config --add channels cyclus
    # channel for Lyveset
    conda config --add channels hcc

    # install bulk of bioinformatic tools using conda
    conda install smalt picard varscan tabix bcftools bowtie2 bwa gatk libdeflate samtools java-jdk lyve-set

    ## Workaround to get 3.8 version of GenomeAnalysisTK.jar
    git clone https://github.com/EnriqueDoster/sing_biotools.git
    mv sing_biotools/bin/GenomeAnalysisTK.jar /usr/local/bin/GenomeAnalysisTK.jar

    #ln -s /usr/local/envs/snp-tools/bin/* /usr/local/bin/

    #Still experimenting with how to change $PATH location. Need to remove GATK jar file to work with cfsan snp
    #echo 'export PATH=$PATH:/usr/local/envs/snp-tools/bin/' >> $SINGULARITY_ENVIRONMENT
    echo 'export CLASSPATH=/usr/local/share/varscan-2.4.4-0/VarScan.jar:$CLASSPATH' >> $SINGULARITY_ENVIRONMENT
    echo 'export CLASSPATH=/usr/local/share/picard-2.21.6-0/picard.jar:$CLASSPATH' >> $SINGULARITY_ENVIRONMENT
    echo 'export CLASSPATH=/usr/local/bin/GenomeAnalysisTK.jar:$CLASSPATH' >> $SINGULARITY_ENVIRONMENT


    # kSNP3 installation
    cd /usr/local/bin/
    wget https://sourceforge.net/projects/ksnp/files/kSNP3.021_Linux_package.zip
    unzip kSNP3.021_Linux_package.zip
    # kSNP by default looks for the it's tools within /usr/local/kSNP3/
    # Move the downloaded folder to that location
    mv /usr/local/bin/kSNP3.021_Linux_package/kSNP3 /usr/local/kSNP3
    echo 'export PATH=/usr/local/kSNP3/:$PATH' >> $SINGULARITY_ENVIRONMENT


%test
```

## Collection

 - Name: [EnriqueDoster/sing_biotools](https://github.com/EnriqueDoster/sing_biotools)
 - License: [MIT License](https://api.github.com/licenses/mit)

