---
id: 1259
name: "ResearchIT/tofu2"
branch: "master"
tag: "v17"
commit: "4dba1b53dc1d5ae07b829e62e650de75f0a4df04"
version: "9863702e2125b56bfbb5f890b41d7b60"
build_date: "2018-01-11T17:30:50.108Z"
size_mb: 6185
size: 1573474335
sif: "https://datasets.datalad.org/shub/ResearchIT/tofu2/v17/2018-01-11-4dba1b53-9863702e/9863702e2125b56bfbb5f890b41d7b60.simg"
url: https://datasets.datalad.org/shub/ResearchIT/tofu2/v17/2018-01-11-4dba1b53-9863702e/
recipe: https://datasets.datalad.org/shub/ResearchIT/tofu2/v17/2018-01-11-4dba1b53-9863702e/Singularity
collection: ResearchIT/tofu2
---

# ResearchIT/tofu2:v17

```bash
$ singularity pull shub://ResearchIT/tofu2:v17
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu

%environment
    PATH=$PATH:/root/tofu2/pitchfork/bin:/root/tofu2/pitchfork/cDNA_Cupcake/sequence
    LD_LIBRARY_PATH=/root/tofu2/pitchfork/lib:$LD_LIBRARY_PATH
    export PATH
    export LD_LIBRARY_PATH

%post
    apt-get update && apt-get -y install git wget minimap python python-dev python-biopython python-setuptools graphviz gcc gfortran make pkg-config libjpeg-dev libfreetype6-dev python-networkx time
    git clone https://github.com/PacificBiosciences/pitchfork.git
    cd pitchfork
    git checkout isoseq_sa5.0.0
    cat settings.mk.example > settings.mk
    make init
    make isoseq-core
    git clone https://github.com/Magdoll/cDNA_Cupcake.git
    cd cDNA_Cupcake
    git checkout -b tofu2 tofu2_v17
    python setup.py build
    python setup.py install

%runscript
    exec echo "$@"
```

## Collection

 - Name: [ResearchIT/tofu2](https://github.com/ResearchIT/tofu2)
 - License: None

