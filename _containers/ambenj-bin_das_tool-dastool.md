---
id: 9457
name: "ambenj/bin_das_tool"
branch: "master"
tag: "dastool"
commit: "75dad1fb422ff021f896d2a9391a920c8923135f"
version: "02413fc64f488cc7b999742e8762a9a4"
build_date: "2019-09-03T13:58:28.495Z"
size_mb: 3084
size: 1350897695
sif: "https://datasets.datalad.org/shub/ambenj/bin_das_tool/dastool/2019-09-03-75dad1fb-02413fc6/02413fc64f488cc7b999742e8762a9a4.simg"
url: https://datasets.datalad.org/shub/ambenj/bin_das_tool/dastool/2019-09-03-75dad1fb-02413fc6/
recipe: https://datasets.datalad.org/shub/ambenj/bin_das_tool/dastool/2019-09-03-75dad1fb-02413fc6/Singularity
collection: ambenj/bin_das_tool
---

# ambenj/bin_das_tool:dastool

```bash
$ singularity pull shub://ambenj/bin_das_tool:dastool
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


    # install anaconda
    if [ ! -d /usr/local/anaconda ]; then
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
            -O /anaconda.sh && \
         bash /anaconda.sh -b -p /usr/local/anaconda && \
         rm /anaconda.sh
    fi
        export PATH="/usr/local/anaconda/bin:$PATH"

    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge

    # requirements for das_tool workflow
    conda install -c bioconda das_tool
    sed -i "s#/bin/env#/usr/bin/env#g" /usr/local/anaconda/bin/Fasta_to_Scaffolds2Bin.sh

    conda install -c bioconda -c conda-forge snakemake
    conda install -c r r-data.table

%runscript
   exec /bin/bash
```

## Collection

 - Name: [ambenj/bin_das_tool](https://github.com/ambenj/bin_das_tool)
 - License: None

