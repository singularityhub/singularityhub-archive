---
id: 10683
name: "meglab-metagenomics/amrplusplus_v2"
branch: "master"
tag: "latest"
commit: "c3dad185f37462e85ea090358648a582cd7fb661"
version: "b4cd8f6073072e2d0f1d671a2e9ccce7"
build_date: "2021-04-16T11:58:57.097Z"
size_mb: 7441.0
size: 3740483615
sif: "https://datasets.datalad.org/shub/meglab-metagenomics/amrplusplus_v2/latest/2021-04-16-c3dad185-b4cd8f60/b4cd8f6073072e2d0f1d671a2e9ccce7.sif"
url: https://datasets.datalad.org/shub/meglab-metagenomics/amrplusplus_v2/latest/2021-04-16-c3dad185-b4cd8f60/
recipe: https://datasets.datalad.org/shub/meglab-metagenomics/amrplusplus_v2/latest/2021-04-16-c3dad185-b4cd8f60/Singularity
collection: meglab-metagenomics/amrplusplus_v2
---

# meglab-metagenomics/amrplusplus_v2:latest

```bash
$ singularity pull shub://meglab-metagenomics/amrplusplus_v2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie-slim

#Includes trimmomatic, samtools, bwa, bedtools, vcftools, htslib,  kraken2, SNPfinder, freebayes, bbmap

%environment
    export LC_ALL=C

%post
    apt update \
    && apt install -y --no-install-recommends \
    build-essential ca-certificates sudo tcsh\
    git make automake autoconf openjdk-7-jre wget gzip unzip sed\
    zlib1g-dev curl libbz2-dev locales libncurses5-dev liblzma-dev libcurl4-openssl-dev software-properties-common apt-transport-https\
    python3-pip python3-docopt python3-pytest python-dev python3-dev\
    libcurl4-openssl-dev libssl-dev zlib1g-dev fonts-texgyre \
    gcc g++ gfortran libblas-dev liblapack-dev dos2unix libstdc++6\
    r-base-core r-recommended hmmer\
    && rm -rf /var/lib/apt/lists/*


    wget -c https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh
    sh Anaconda3-2020.02-Linux-x86_64.sh -bfp /usr/local

    # add bioconda channels
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda

    # install bulk of bioinformatic tools using conda
    conda create -n AmrPlusPlus_env python=3 trimmomatic bwa samtools bedtools freebayes bbmap vcftools htslib kraken2

    . /usr/local/bin/activate AmrPlusPlus_env
    
    #ln -s /usr/local/envs/AmrPlusPlus_env/bin/* /usr/local/bin/
    
    #Still experimenting with how to change $PATH location. 
    echo 'export PATH=$PATH:/usr/local/envs/AmrPlusPlus_env/bin/' >> $SINGULARITY_ENVIRONMENT

    # SNPfinder
    cd /usr/local
    git clone https://github.com/cdeanj/snpfinder.git
    cd snpfinder
    make
    cp snpfinder /usr/local/bin
    cd /

    # Make sure all the tools have the right permissions to use the tools
    chmod -R 777 /usr/local/
    
%test
```

## Collection

 - Name: [meglab-metagenomics/amrplusplus_v2](https://github.com/meglab-metagenomics/amrplusplus_v2)
 - License: [MIT License](https://api.github.com/licenses/mit)

