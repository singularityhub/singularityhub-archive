---
id: 9075
name: "linzhi2013/MitoZ"
branch: "master"
tag: "v2.4-alpha"
commit: "006b30b75a8aad06237bb33e56dcb945598a8dad"
version: "f60d845d70ba32470039506b6bc36609"
build_date: "2021-04-13T17:51:56.193Z"
size_mb: 3183
size: 1099788319
sif: "https://datasets.datalad.org/shub/linzhi2013/MitoZ/v2.4-alpha/2021-04-13-006b30b7-f60d845d/f60d845d70ba32470039506b6bc36609.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/linzhi2013/MitoZ/v2.4-alpha/2021-04-13-006b30b7-f60d845d/
recipe: https://datasets.datalad.org/shub/linzhi2013/MitoZ/v2.4-alpha/2021-04-13-006b30b7-f60d845d/Singularity
collection: linzhi2013/MitoZ
---

# linzhi2013/MitoZ:v2.4-alpha

```bash
$ singularity pull shub://linzhi2013/MitoZ:v2.4-alpha
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
    mkdir /mitoz_tmp && cd /mitoz_tmp && wget -c https://raw.githubusercontent.com/linzhi2013/MitoZ/master/version_2.4/release_MitoZ_v2.4-alpha.tar.bz2 &&  tar -jxvf release_MitoZ_v2.4-alpha.tar.bz2  && mv release_MitoZ_v2.4-alpha /app
    rm -rf /mitoz_tmp


%environment
    export LC_ALL=C
    export PATH=/app/anaconda/bin:$PATH


%runscript
     /app/anaconda/bin/python3 /app/release_MitoZ_v2.4-alpha/MitoZ.py "$@"


%labels
AUTHOR    Guanliang MENG, BGI-Shenzhen
```

## Collection

 - Name: [linzhi2013/MitoZ](https://github.com/linzhi2013/MitoZ)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

