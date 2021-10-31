---
id: 8229
name: "EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation"
branch: "master"
tag: "latest"
commit: "46f8ead6d40bdfd883e504e51efc42c2486869c1"
version: "7ba47dd0deb40d30d7f111d71b2570c6"
build_date: "2019-04-08T08:50:14.651Z"
size_mb: 8304
size: 3725676575
sif: "https://datasets.datalad.org/shub/EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation/latest/2019-04-08-46f8ead6-7ba47dd0/7ba47dd0deb40d30d7f111d71b2570c6.simg"
url: https://datasets.datalad.org/shub/EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation/latest/2019-04-08-46f8ead6-7ba47dd0/
recipe: https://datasets.datalad.org/shub/EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation/latest/2019-04-08-46f8ead6-7ba47dd0/Singularity
collection: EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation
---

# EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation:latest

```bash
$ singularity pull shub://EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:jessie-slim

#Includes rgi idba trimmomatic bwa samtools bedtools freebayes bbmap vcftools htslib resistomeanalyzer, rarefactionanalyzer, SNPfinder
%environment
    export PATH=/usr/local/envs/compute/bin/:${PATH}
    
%post
    ## Java install doesn't work, but can load java module from summit
    apt update \
    && apt install -y --no-install-recommends \
    build-essential ca-certificates sudo \
    git make automake autoconf wget unzip sed \
    zlib1g-dev curl libbz2-dev locales libncurses5-dev liblzma-dev libcurl4-openssl-dev software-properties-common apt-transport-https\
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    python3-pip python3-docopt python3-pytest python-dev python3-dev\
    libssl-dev zlib1g-dev fonts-texgyre \
    gcc g++ gfortran libblas-dev liblapack-dev dos2unix tabix \
    r-base-core r-recommended hmmer\
    && rm -rf /var/lib/apt/lists/*

    #Installing Anaconda 2 and Conda 4.5.11
    wget -c https://repo.continuum.io/archive/Anaconda2-5.3.0-Linux-x86_64.sh
    sh Anaconda2-5.3.0-Linux-x86_64.sh -bfp /usr/local

    # add bioconda channels
    conda config --add channels defaults
    conda config --add channels conda-forge
    conda config --add channels bioconda
    conda update conda
    conda clean --all --yes
    
    # install bulk of bioinformatic tools using conda 
    conda create -n compute python=3 rgi idba trimmomatic bwa samtools bedtools freebayes bbmap vcftools htslib ncurses    

    # make /data and /scripts so we can mount it to access external resources
    #if [ ! -d /data ]; then mkdir /data; fi
    #if [ ! -d /scripts ]; then mkdir /scripts; fi
    
    . /usr/local/bin/activate compute
        
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

    # Install kraken
    cd /usr/local
    git clone https://github.com/DerrickWood/kraken2.git
    cd kraken2/
    ./install_kraken2.sh /usr/local/kraken2
    cp /usr/local/kraken2/kraken2 /usr/local/bin
    cp /usr/local/kraken2/kraken2-build /usr/local/bin
    cp /usr/local/kraken2/kraken2-inspect /usr/local/bin
    cd /
    
    chmod -R 777 /usr/local/
    
%runscript
    echo "Now inside Singularity container woah..."
    exec /bin/bash    
   
%test
```

## Collection

 - Name: [EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation](https://github.com/EnriqueDoster/MEG-amrplusplus-RGI-SNPconfirmation)
 - License: [MIT License](https://api.github.com/licenses/mit)

