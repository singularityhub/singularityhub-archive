---
id: 8892
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "orthofinder"
commit: "92fc067f431e887caf8586509e7d142175e177ab"
version: "9618f47f1dd8ff0dbdb41cd0e9207f91"
build_date: "2021-03-19T20:26:10.298Z"
size_mb: 480
size: 190062623
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/orthofinder/2021-03-19-92fc067f-9618f47f/9618f47f1dd8ff0dbdb41cd0e9207f91.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/orthofinder/2021-03-19-92fc067f-9618f47f/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/orthofinder/2021-03-19-92fc067f-9618f47f/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:orthofinder

```bash
$ singularity pull shub://jlboat/BioinfoContainers:orthofinder
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

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

