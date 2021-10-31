---
id: 10186
name: "DrVale83/bioinfo"
branch: "master"
tag: "orthofinder"
commit: "93734416d097ed8c250ecd6902afd2fcccfab6a6"
version: "0983e113864ec809de2a6ed3fbdd2733"
build_date: "2021-03-19T20:23:12.178Z"
size_mb: 474
size: 188137503
sif: "https://datasets.datalad.org/shub/DrVale83/bioinfo/orthofinder/2021-03-19-93734416-0983e113/0983e113864ec809de2a6ed3fbdd2733.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/DrVale83/bioinfo/orthofinder/2021-03-19-93734416-0983e113/
recipe: https://datasets.datalad.org/shub/DrVale83/bioinfo/orthofinder/2021-03-19-93734416-0983e113/Singularity
collection: DrVale83/bioinfo
---

# DrVale83/bioinfo:orthofinder

```bash
$ singularity pull shub://DrVale83/bioinfo:orthofinder
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    Input FASTA
    OrthoFinder 2.3.3

%environment
    export PATH="$PATH:/opt/OrthoFinder-2.3.3/"

%post
    apt-get update --fix-missing && apt-get install -y wget build-essential automake mcl ncbi-blast+ && rm -rf /var/lib/apt/lists/*
    
    # Install FastME
    cd /opt/
    wget https://gite.lirmm.fr/atgc/FastME/raw/master/tarball/fastme-2.1.6.1.tar.gz
    tar -xvzf fastme-2.1.6.1.tar.gz
    rm fastme-2.1.6.1.tar.gz
    cd fastme-2.1.6.1
    ./configure
    make
    make install

    # Install Diamond
    cd /opt
    wget https://github.com/bbuchfink/diamond/releases/download/v0.9.22/diamond-linux64.tar.gz
    tar xzf diamond-linux64.tar.gz
    chmod 777 diamond
    cp diamond /usr/bin    
    
    # Install mafft
    wget https://mafft.cbrc.jp/alignment/software/mafft_7.427-1_amd64.deb
    dpkg -i mafft_7.427-1_amd64.deb

    # Install fasttree
    wget http://www.microbesonline.org/fasttree/FastTree
    chmod 777 FastTree
    mv FastTree /usr/bin/

    # Install OrthoFinder
    cd /opt
    wget https://github.com/davidemms/OrthoFinder/releases/download/2.3.3/OrthoFinder-2.3.3.tar.gz
    tar -xvzf OrthoFinder-2.3.3.tar.gz
    rm OrthoFinder-2.3.3.tar.gz
    cd OrthoFinder-2.3.3/
    ln -s /usr/bin/diamond
    ln -s /usr/bin/mafft
    ln -s /usr/bin/FastTree
   
    apt-get remove -y wget build-essential automake  
    chmod -R 777 /opt/*

%runscript
    exec orthofinder "$@"
```

## Collection

 - Name: [DrVale83/bioinfo](https://github.com/DrVale83/bioinfo)
 - License: None

