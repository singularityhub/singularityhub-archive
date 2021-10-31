---
id: 4631
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "maxbin"
commit: "b2b9f90f7a7b03a450c02c4b8ffd68e2968d8854"
version: "947698ceb363cf4867049ebe95495eb4"
build_date: "2018-09-03T17:16:24.249Z"
size_mb: 905
size: 329936927
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/maxbin/2018-09-03-b2b9f90f-947698ce/947698ceb363cf4867049ebe95495eb4.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/maxbin/2018-09-03-b2b9f90f-947698ce/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/maxbin/2018-09-03-b2b9f90f-947698ce/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:maxbin

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:maxbin
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%setup
    export LC_ALL=C

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget gawk build-essential perl autoconf zip
    
	cd /home
    wget https://downloads.jbei.org/data/microbial_communities/MaxBin/getfile.php?MaxBin-2.2.3.tar.gz
    tar -xzf getfile.php?MaxBin-2.2.3.tar.gz
    rm getfile.php?MaxBin-2.2.3.tar.gz
    cd MaxBin-2.2.3/src
    make
    cd /home/MaxBin-2.2.3
    ./autobuild_auxiliary
    cd auxiliary/hmmer-3.1b1/
    make install
    cd ../idba-1.1.1/
    make install
    mv bin/idba_ud /usr/local/bin
    cd ../bowtie2-2.2.3
    find -mindepth 1 -maxdepth 1 -executable -exec mv {} /usr/local/bin/ \;
    cd ../FragGeneScan1.30
    find -mindepth 1 -maxdepth 1 -executable -exec mv {} /usr/local/bin/ \;
    cd /home/MaxBin-2.2.3
    mv setting heatmap.r marker.hmm bacar_marker.hmm run_MaxBin.pl src _getmarker.pl _getabund.pl _sepReads.pl /usr/local/bin/
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

