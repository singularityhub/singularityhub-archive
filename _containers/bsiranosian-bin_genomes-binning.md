---
id: 9254
name: "bsiranosian/bin_genomes"
branch: "master"
tag: "binning"
commit: "06691f2e4549841992673000a4955e92f385ec0c"
version: "5e904677f909f3b80034a5b10b2f1dd3"
build_date: "2021-03-05T06:01:28.455Z"
size_mb: 6231
size: 2693918751
sif: "https://datasets.datalad.org/shub/bsiranosian/bin_genomes/binning/2021-03-05-06691f2e-5e904677/5e904677f909f3b80034a5b10b2f1dd3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bin_genomes/binning/2021-03-05-06691f2e-5e904677/
recipe: https://datasets.datalad.org/shub/bsiranosian/bin_genomes/binning/2021-03-05-06691f2e-5e904677/Singularity
collection: bsiranosian/bin_genomes
---

# bsiranosian/bin_genomes:binning

```bash
$ singularity pull shub://bsiranosian/bin_genomes:binning
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04


# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"

%post 
    apt-get update
    apt-get install -y locales
    # localle update necessary for quast
    locale-gen --purge "en_US.UTF-8"
    update-locale LANG="en_US.UTF-8"

    apt-get install -y wget curl less
    apt-get install -y build-essential


    # apt-get install -y eatmydata
    # eatmydata apt-get install -y wget bzip2 \
    #   ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
    #   git
    # apt-get clean



    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    # requirements for mgwf workflow 
    conda install -y -c conda-forge -c bioconda -c ursky -c anaconda python=3.6 minimap2 \
    readline=6.2 r-ggplot2 r-doBy r-circlize prodigal aragorn metabat2 barrnap \
    prokka samtools ncurses bedtools kraken2 bwa pip kraken2 pandas requests maxbin2
    
    # manual quast installation 
    apt-get install -y zlib1g-dev
    apt-get install -y pkg-config libfreetype6-dev libpng-dev python-matplotlib
    wget https://downloads.sourceforge.net/project/quast/quast-5.0.2.tar.gz
    tar -xzf quast-5.0.2.tar.gz
    cd quast-5.0.2
    ./setup.py install
    echo "alias quast=~/quast-5.0.2/quast.py" >> ~/.bashrc 
    cd 

    pip install snakemake
    pip install pysam

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bin_genomes](https://github.com/bsiranosian/bin_genomes)
 - License: None

