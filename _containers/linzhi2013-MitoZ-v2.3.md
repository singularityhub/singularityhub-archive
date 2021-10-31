---
id: 6598
name: "linzhi2013/MitoZ"
branch: "master"
tag: "v2.3"
commit: "365f68ef7fc7af748c3a0e5da9ecd8938437ae87"
version: "ff174f05723116d01f22a998de112ade"
build_date: "2021-04-13T10:22:36.129Z"
size_mb: 3252
size: 1118027807
sif: "https://datasets.datalad.org/shub/linzhi2013/MitoZ/v2.3/2021-04-13-365f68ef-ff174f05/ff174f05723116d01f22a998de112ade.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/linzhi2013/MitoZ/v2.3/2021-04-13-365f68ef-ff174f05/
recipe: https://datasets.datalad.org/shub/linzhi2013/MitoZ/v2.3/2021-04-13-365f68ef-ff174f05/Singularity
collection: linzhi2013/MitoZ
---

# linzhi2013/MitoZ:v2.3

```bash
$ singularity pull shub://linzhi2013/MitoZ:v2.3
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:16.04

# Beware that Mac OS's file system is case-insensitive by default,
# which can cause some potential problems sometimes


%post
    apt-get update
    apt-get install -y  wget bzip2
    mkdir /app
    # install anaconda
    if [ ! -d /app/anaconda ]; then
        #  wget -c https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda-latest-Linux-x86_64.sh \
        wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
        -O /app/anaconda.sh && \
        bash /app/anaconda.sh -b -p /app/anaconda && \
        rm -rf /app/anaconda.sh
    fi

    apt-get clean && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    # set anaconda path
    export PATH="/app/anaconda/bin:$PATH"

    # install dependency for MitoZ
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    # conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/ # for China users
    # conda config --add channels http://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/  # for China users

    conda install -y libgd=2.2.4 python=3.6.0 biopython=1.69 ete3=3.0.0b35  perl-list-moreutils perl-params-validate perl-clone circos=0.69 perl-bioperl blast=2.2.31  hmmer=3.1b2  bwa=0.7.12 samtools=1.3.1 infernal=1.1.1 tbl2asn openjdk

    conda clean -y -a

    # download MitoZ and install
    mkdir /mitoz_tmp && cd /mitoz_tmp && wget -c https://raw.githubusercontent.com/linzhi2013/MitoZ/master/version_2.3/release_MitoZ_v2.3.tar.bz2 &&  tar -jxvf release_MitoZ_v2.3.tar.bz2  && mv release_MitoZ_v2.3 /app
    rm -rf /mitoz_tmp


%environment
    export LC_ALL=C
    export PATH=/app/anaconda/bin:$PATH


%runscript
     /app/anaconda/bin/python3 /app/release_MitoZ_v2.3/MitoZ.py "$@"


%labels
AUTHOR    Guanliang MENG, BGI-Shenzhen
```

## Collection

 - Name: [linzhi2013/MitoZ](https://github.com/linzhi2013/MitoZ)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

