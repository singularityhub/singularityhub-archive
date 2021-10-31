---
id: 14427
name: "repeatexplorer/repex_tarean"
branch: "master"
tag: "latest"
commit: "ec6bbbddd38eb2d1c52fdb56f561998df01126f1"
version: "0e508250fb93433902086deb62773bb8"
build_date: "2021-04-12T16:31:09.726Z"
size_mb: 2795.0
size: 1082744863
sif: "https://datasets.datalad.org/shub/repeatexplorer/repex_tarean/latest/2021-04-12-ec6bbbdd-0e508250/0e508250fb93433902086deb62773bb8.sif"
url: https://datasets.datalad.org/shub/repeatexplorer/repex_tarean/latest/2021-04-12-ec6bbbdd-0e508250/
recipe: https://datasets.datalad.org/shub/repeatexplorer/repex_tarean/latest/2021-04-12-ec6bbbdd-0e508250/Singularity
collection: repeatexplorer/repex_tarean
---

# repeatexplorer/repex_tarean:latest

```bash
$ singularity pull shub://repeatexplorer/repex_tarean:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04
%files
    R_install.R  /opt/R_install.R


%post
    export DEBIAN_FRONTEND=noninteractive
    apt-get -y update
    apt-get -y install git python3 ncbi-blast+-legacy ncbi-blast+ python3 mafft python3-pip imagemagick diamond-aligner last-align
    apt-get -y install r-base libcurl4-openssl-dev libxml2-dev libgtk2.0-dev libssl-dev build-essential gfortran libblas-dev liblapack-dev r-cran-future
    apt-get -y install r-cran-stringr r-cran-dt r-cran-scales r-cran-igraph r-cran-hwriter r-bioc-biostrings 
    apt-get -y install r-cran-plotrix r-cran-png r-cran-dplyr r-cran-plyr r-cran-optparse r-cran-dbi r-cran-rsqlite
    dpkg --add-architecture i386
    apt-get update
    apt-get -y install libc6:i386 libncurses5:i386 libstdc++6:i386
    Rscript /opt/R_install.R
    pip3 install pyRserve
    cd opt
    git clone https://petrnovak@bitbucket.org/petrnovak/repex_tarean.git
    cd repex_tarean && make
    ln -s /opt/repex_tarean/seqclust /usr/local/bin/seqclust
%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH
    export TMPDIR=""
%runscript
    seqclust $@

%labels
    Author petr@umbr.cas.cz
    Version v0.0.2

%test
    cd /opt/repex_tarean/
    /opt/repex_tarean/test_repex_pipeline.py SHORT_SUITE
```

## Collection

 - Name: [repeatexplorer/repex_tarean](https://github.com/repeatexplorer/repex_tarean)
 - License: None

