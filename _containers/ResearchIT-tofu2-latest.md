---
id: 1260
name: "ResearchIT/tofu2"
branch: "master"
tag: "latest"
commit: "fec325b41849c7c1b6b11abd66bc8035c2db380c"
version: "602bed32fe9740c5d504a316a284d491"
build_date: "2018-01-11T17:30:50.098Z"
size_mb: 6175
size: 1571880991
sif: "https://datasets.datalad.org/shub/ResearchIT/tofu2/latest/2018-01-11-fec325b4-602bed32/602bed32fe9740c5d504a316a284d491.simg"
url: https://datasets.datalad.org/shub/ResearchIT/tofu2/latest/2018-01-11-fec325b4-602bed32/
recipe: https://datasets.datalad.org/shub/ResearchIT/tofu2/latest/2018-01-11-fec325b4-602bed32/Singularity
collection: ResearchIT/tofu2
---

# ResearchIT/tofu2:latest

```bash
$ singularity pull shub://ResearchIT/tofu2:latest
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
    apt-get update && apt-get -y install git wget minimap python python-dev python-biopython python-setuptools graphviz gcc gfortran make pkg-config libjpeg-dev libfreetype6-dev
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

