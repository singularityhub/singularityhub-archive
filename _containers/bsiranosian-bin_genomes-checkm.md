---
id: 9253
name: "bsiranosian/bin_genomes"
branch: "master"
tag: "checkm"
commit: "dd352b12899baa79aed36c8416f03ea94d23ef89"
version: "aee385ce96858a2fd90a8d561db80d2e"
build_date: "2021-04-14T23:42:59.510Z"
size_mb: 2872
size: 1086980127
sif: "https://datasets.datalad.org/shub/bsiranosian/bin_genomes/checkm/2021-04-14-dd352b12-aee385ce/aee385ce96858a2fd90a8d561db80d2e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bsiranosian/bin_genomes/checkm/2021-04-14-dd352b12-aee385ce/
recipe: https://datasets.datalad.org/shub/bsiranosian/bin_genomes/checkm/2021-04-14-dd352b12-aee385ce/Singularity
collection: bsiranosian/bin_genomes
---

# bsiranosian/bin_genomes:checkm

```bash
$ singularity pull shub://bsiranosian/bin_genomes:checkm
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
    apt-get install -y locales wget build-essential
    # localle update necessary for quast
    locale-gen --purge "en_US.UTF-8"
    update-locale LANG="en_US.UTF-8"

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda install -y -c bioconda python=2.7 hmmer prodigal pplacer 

    # checkm install 
    pip install checkm-genome
    mkdir checkm_data
    cd checkm_data
    wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz
    tar xvfz checkm_data_2015_01_16.tar.gz
    yes "." | checkm data setRoot

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bin_genomes](https://github.com/bsiranosian/bin_genomes)
 - License: None

