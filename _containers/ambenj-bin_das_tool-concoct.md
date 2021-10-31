---
id: 9504
name: "ambenj/bin_das_tool"
branch: "master"
tag: "concoct"
commit: "ace82aa52a9457856ac5398bc1241e442296b79b"
version: "0f400cb69ee661b80c568925a1ace292"
build_date: "2019-06-04T20:29:11.505Z"
size_mb: 2959
size: 1419812895
sif: "https://datasets.datalad.org/shub/ambenj/bin_das_tool/concoct/2019-06-04-ace82aa5-0f400cb6/0f400cb69ee661b80c568925a1ace292.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ambenj/bin_das_tool/concoct/2019-06-04-ace82aa5-0f400cb6/
recipe: https://datasets.datalad.org/shub/ambenj/bin_das_tool/concoct/2019-06-04-ace82aa5-0f400cb6/Singularity
collection: ambenj/bin_das_tool
---

# ambenj/bin_das_tool:concoct

```bash
$ singularity pull shub://ambenj/bin_das_tool:concoct
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
    conda install -c bioconda concoct bedtools picard samtools bowtie2 pysam parallel
    wget https://github.com/BinPro/CONCOCT/archive/1.0.0.tar.gz
    tar -xzf 1.0.0.tar.gz

    conda install -c bioconda -c conda-forge snakemake

%runscript
   exec /bin/bash
```

## Collection

 - Name: [ambenj/bin_das_tool](https://github.com/ambenj/bin_das_tool)
 - License: None

