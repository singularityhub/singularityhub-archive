---
id: 6245
name: "linzhi2013/MitoZ"
branch: "master"
tag: "v1.0"
commit: "b690135b4ce654d5140ec586d800a5ff7af05ceb"
version: "9cc03345721b297802db9d409928a869"
build_date: "2020-08-03T01:49:05.604Z"
size_mb: 3397
size: 1168244767
sif: "https://datasets.datalad.org/shub/linzhi2013/MitoZ/v1.0/2020-08-03-b690135b-9cc03345/9cc03345721b297802db9d409928a869.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/linzhi2013/MitoZ/v1.0/2020-08-03-b690135b-9cc03345/
recipe: https://datasets.datalad.org/shub/linzhi2013/MitoZ/v1.0/2020-08-03-b690135b-9cc03345/Singularity
collection: linzhi2013/MitoZ
---

# linzhi2013/MitoZ:v1.0

```bash
$ singularity pull shub://linzhi2013/MitoZ:v1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:16.04

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
    mkdir /mitoz_tmp && cd /mitoz_tmp && wget -c https://raw.githubusercontent.com/linzhi2013/MitoZ/master/version_1.0/release_MitoZ_v1.0.tar.bz2 &&  tar -jxvf release_MitoZ_v1.0.tar.bz2  && mv release_MitoZ_v1.0 /app
    rm -rf /mitoz_tmp


%environment
    export LC_ALL=C
    export PATH=/app/anaconda/bin/:$PATH


%runscript
     /app/anaconda/bin/python3 /app/release_MitoZ_v1.0/MitoZ.py "$@"


%labels
AUTHOR    Guanliang MENG, BGI-Shenzhen
```

## Collection

 - Name: [linzhi2013/MitoZ](https://github.com/linzhi2013/MitoZ)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

