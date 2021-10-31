---
id: 6176
name: "bhattlab/wits_workshop"
branch: "master"
tag: "classification"
commit: "378137db6c401cbc8422b7a820619ece2c9ae86e"
version: "47cd119e7269909380c67f2991da1e2c"
build_date: "2019-01-11T15:17:05.162Z"
size_mb: 4339
size: 1848410143
sif: "https://datasets.datalad.org/shub/bhattlab/wits_workshop/classification/2019-01-11-378137db-47cd119e/47cd119e7269909380c67f2991da1e2c.simg"
url: https://datasets.datalad.org/shub/bhattlab/wits_workshop/classification/2019-01-11-378137db-47cd119e/
recipe: https://datasets.datalad.org/shub/bhattlab/wits_workshop/classification/2019-01-11-378137db-47cd119e/Singularity
collection: bhattlab/wits_workshop
---

# bhattlab/wits_workshop:classification

```bash
$ singularity pull shub://bhattlab/wits_workshop:classification
```

## Singularity Recipe

```singularity
# Metagenomics Singularity environment definition
# Eli Moss
# elimoss@stanford.edu
# January 2019
# build this environment with `sudo singularity build bhatt_meta_singularity.img bhatt_meta_singularity.def`
# for development, build with sudo singularity build --sandbox bhatt_meta_singularity bhatt_meta_singularity.def,
# and then modify with sudo singularity shell --writable bhatt_meta_singularity/
# When complete, use sudo singularity build bhatt_meta.simg bhatt_meta_singularity/

bootstrap: docker
from: neurodebian:jessie

# this command assumes at least singularity 2.3
%environment
    PATH="/usr/local/anaconda/bin:$PATH"
%post
    # install debian packages
    apt-get update
    apt-get install -y eatmydata
    eatmydata apt-get install -y wget bzip2 \
      ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
      git git-annex-standalone
    apt-get clean

    apt-get install -y g++ build-essential


    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
    # set anaconda path
    export PATH="/usr/local/anaconda/bin:$PATH"

    # requirements for taxonomic classification
    conda install -y -c conda-forge -c bioconda -c r \
		kraken2 krona kraken ncurses datrie r-ggplot2 r-doby r-rcolorbrewer r-scales r-plyr r-stringi

    mkdir /usr/local/anaconda/bin/taxonomy
    ktUpdateTaxonomy.sh

    #install bracken from source
    git clone https://github.com/jenniferlu717/Bracken.git
    cd Bracken
    bash install_bracken.sh
    cp -r * /usr/local/bin/


    # make /data and /scripts so we can mount it to access external resources
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /scripts ]; then mkdir /scripts; fi



%runscript
    exec /bin/bash
```

## Collection

 - Name: [bhattlab/wits_workshop](https://github.com/bhattlab/wits_workshop)
 - License: None

