---
id: 8603
name: "simrnsethi/singularity-image"
branch: "master"
tag: "latest"
commit: "2e308e97f548e49bbe001b24c0e5e49528e95d6e"
version: "356614e069806b9585fd3e7e0e0de0b7"
build_date: "2019-04-23T21:56:56.033Z"
size_mb: 1266
size: 432750623
sif: "https://datasets.datalad.org/shub/simrnsethi/singularity-image/latest/2019-04-23-2e308e97-356614e0/356614e069806b9585fd3e7e0e0de0b7.simg"
url: https://datasets.datalad.org/shub/simrnsethi/singularity-image/latest/2019-04-23-2e308e97-356614e0/
recipe: https://datasets.datalad.org/shub/simrnsethi/singularity-image/latest/2019-04-23-2e308e97-356614e0/Singularity
collection: simrnsethi/singularity-image
---

# simrnsethi/singularity-image:latest

```bash
$ singularity pull shub://simrnsethi/singularity-image:latest
```

## Singularity Recipe

```singularity
# Singularity definition example with miniconda
# Matteo Visconti di Oleggio Castello; Eshin Jolly
# mvdoc.gr@dartmouth.edu; eshin.jolly.gr@dartmouth.edu
# May 2017

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

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.continuum.io/miniconda/Miniconda2-4.3.14-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
    # set anaconda path
    export PATH="/usr/local/anaconda/bin:$PATH"

    # install the bare minimum
    conda install\
      numpy scipy
    conda clean --tarballs

    # make /data and /scripts so we can mount it to access external resources
    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /scripts ]; then mkdir /scripts; fi

%runscript
    echo "Now inside Singularity container woah..." > Hello
```

## Collection

 - Name: [simrnsethi/singularity-image](https://github.com/simrnsethi/singularity-image)
 - License: None

