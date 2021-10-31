---
id: 12989
name: "TomHarrop/funannotate-singularity"
branch: "master"
tag: "funannotate-conda_1.7.4"
commit: "3390245344a27803bd8481fd00f8d2cd2635d239"
version: "052660f1ee7195881937e3f306194a063a36d9d0bc03f8ad972f6f6aaf09e1b5"
build_date: "2020-12-06T05:30:25.318Z"
size_mb: 1413.90625
size: 1482588160
sif: "https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate-conda_1.7.4/2020-12-06-33902453-052660f1/052660f1ee7195881937e3f306194a063a36d9d0bc03f8ad972f6f6aaf09e1b5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/TomHarrop/funannotate-singularity/funannotate-conda_1.7.4/2020-12-06-33902453-052660f1/
recipe: https://datasets.datalad.org/shub/TomHarrop/funannotate-singularity/funannotate-conda_1.7.4/2020-12-06-33902453-052660f1/Singularity
collection: TomHarrop/funannotate-singularity
---

# TomHarrop/funannotate-singularity:funannotate-conda_1.7.4

```bash
$ singularity pull shub://TomHarrop/funannotate-singularity:funannotate-conda_1.7.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.7.12

%environment
    export LC_ALL=C
    export BASH_ENV=/condarc
    export GENEMARK_PATH=/genemark
    export PATH="${PATH}:/genemark"

%post
    export DEBIAN_FRONTEND=noninteractive
    export LC_ALL=C
    export FUNANNOTATE_DB=/home/funannotate_db
    export BASH_ENV=/condarc
    export GENEMARK_PATH=/genemark
    export PATH="${PATH}:/genemark"

    # reset sources.list to something-like-default (with backports and
    # non-free)
    rm -r /var/lib/apt/lists/*
cat << _EOF_ > /etc/apt/sources.list
deb http://deb.debian.org/debian/ buster main contrib non-free
deb-src http://deb.debian.org/debian/ buster main contrib non-free

deb http://deb.debian.org/debian/ buster-updates main contrib non-free
deb-src http://deb.debian.org/debian/ buster-updates main contrib non-free

deb http://deb.debian.org/debian-security buster/updates main
deb-src http://deb.debian.org/debian-security buster/updates main

deb http://deb.debian.org/debian buster-backports main contrib non-free
deb-src http://deb.debian.org/debian buster-backports main contrib non-free
_EOF_
    apt-get update

    # deps
    apt-get install -y \
        libfile-which-perl \
        python-pip
        # python3-pip   # ete3 won't load, so don't need pip3

    # set up conda
    . /opt/conda/etc/profile.d/conda.sh
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    conda update --yes -n base -c defaults conda

    conda create -n funannotate --yes "funannotate=1.7.4"
    conda clean -afy

    # genemark
    (
    wget -O /genemark_download.sh \
        --no-check-certificate \
        https://raw.githubusercontent.com/TomHarrop/funannotate-singularity/master/src/genemark_download.sh
    cd / && bash genemark_download.sh || exit 1
    rm /genemark_download.sh

    # fix genemark shebangs
    find /genemark -name "*.pl" -type f \
        -exec perl -i -0pe 's/^#\!.*perl.*/#\!\/usr\/bin\/env perl/g' {} +
    )

    # emapper
    /usr/bin/pip2 install --upgrade pip
    /usr/local/bin/pip2 install \
        git+https://github.com/jhcepas/eggnog-mapper.git

    # ete3 is broken
    # /usr/bin/pip3 install --upgrade pip
    # /usr/local/bin/pip3 install \
    #     ete3

    # set up BASH_ENV to activate conda
    echo ". /opt/conda/etc/profile.d/conda.sh" >> "${BASH_ENV}"
    echo "conda activate funannotate" >> "${BASH_ENV}"

%runscript
    exec bash -c 'funannotate check --show-versions'
```

## Collection

 - Name: [TomHarrop/funannotate-singularity](https://github.com/TomHarrop/funannotate-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

