---
id: 4607
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "canopy"
commit: "0d7dddf82db777d90162a300315f4924844446e7"
version: "bdca7f47f30ac901bfa5f834ec0d506f"
build_date: "2018-09-02T17:27:42.159Z"
size_mb: 651
size: 228143135
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/canopy/2018-09-02-0d7dddf8-bdca7f47/bdca7f47f30ac901bfa5f834ec0d506f.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/canopy/2018-09-02-0d7dddf8-bdca7f47/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/canopy/2018-09-02-0d7dddf8-bdca7f47/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:canopy

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:canopy
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%files
    bin/cluster_to_fasta.py /usr/local/bin
    bin/fasta.py /usr/local/bin

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget zip libboost-dev libboost-program-options-dev python python-pip gawk
    
    pip install biopython
    
    wget https://bitbucket.org/HeyHo/mgs-canopy-algorithm/get/d55ed1a8b825.zip
    unzip d55ed1a8b825.zip
    cd HeyHo-mgs-canopy-algorithm-d55ed1a8b825/src/
    make -f Makefile
    mv * /usr/local/bin
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

