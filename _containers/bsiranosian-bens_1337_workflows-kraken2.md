---
id: 9881
name: "bsiranosian/bens_1337_workflows"
branch: "master"
tag: "kraken2"
commit: "e2af0cef1a301986b5f683c971eb56c0793a2882"
version: "2428de4a97458af99ba97a302ca01357"
build_date: "2020-09-01T17:23:18.066Z"
size_mb: 1913
size: 975716383
sif: "https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/kraken2/2020-09-01-e2af0cef-2428de4a/2428de4a97458af99ba97a302ca01357.simg"
url: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/kraken2/2020-09-01-e2af0cef-2428de4a/
recipe: https://datasets.datalad.org/shub/bsiranosian/bens_1337_workflows/kraken2/2020-09-01-e2af0cef-2428de4a/Singularity
collection: bsiranosian/bens_1337_workflows
---

# bsiranosian/bens_1337_workflows:kraken2

```bash
$ singularity pull shub://bsiranosian/bens_1337_workflows:kraken2
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
    apt-get install -y locales wget build-essential libicu-dev

    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O ~/anaconda.sh && \
         bash ~/anaconda.sh -b -p /usr/local/anaconda && \
         rm ~/anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda install -y -c bioconda -c conda-forge -c r python=3.6 kraken2 bbmap

%runscript
   exec /bin/bash
```

## Collection

 - Name: [bsiranosian/bens_1337_workflows](https://github.com/bsiranosian/bens_1337_workflows)
 - License: None

