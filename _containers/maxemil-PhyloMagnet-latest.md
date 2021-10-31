---
id: 10490
name: "maxemil/PhyloMagnet"
branch: "master"
tag: "latest"
commit: "c742de49e22fb820924d6b32311b501f6ab47d27"
version: "33bf1df183c46c2464fa00cfdd8b2fde"
build_date: "2021-04-07T12:42:12.051Z"
size_mb: 3042.0
size: 974110751
sif: "https://datasets.datalad.org/shub/maxemil/PhyloMagnet/latest/2021-04-07-c742de49-33bf1df1/33bf1df183c46c2464fa00cfdd8b2fde.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/maxemil/PhyloMagnet/latest/2021-04-07-c742de49-33bf1df1/
recipe: https://datasets.datalad.org/shub/maxemil/PhyloMagnet/latest/2021-04-07-c742de49-33bf1df1/Singularity
collection: maxemil/PhyloMagnet
---

# maxemil/PhyloMagnet:latest

```bash
$ singularity pull shub://maxemil/PhyloMagnet:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/miniconda3:4.6.14

%labels
    MAINTAINER Max Emil Schön <max-emil.schon@icm.uu.se>
    DESCRIPTION Singularity image containing all requirements for the PhyloMagnet pipeline
    VERSION 0.7

%environment
    PATH=/opt/conda/envs/PhyloMagnet-0.7/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    apt-get update
    apt-get install -y procps libxtst6
    apt-get clean -y

    ####### parapa #########
    cd /usr/local/bin
    wget https://cme.h-its.org/exelixis/resource/download/software/papara_nt-2.5-static_x86_64.tar.gz
    tar -xvf papara_nt-2.5-static_x86_64.tar.gz
    rm papara_nt-2.5-static_x86_64.tar.gz
    mv papara_static_x86_64 papara

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a


%test
VERSION="0.7"
/opt/conda/envs/PhyloMagnet-$VERSION/opt/megan-6.12.3/tools/daa-meganizer -h
/opt/conda/envs/PhyloMagnet-$VERSION/opt/megan-6.12.3/tools/gc-assembler -h
/opt/conda/envs/PhyloMagnet-$VERSION/bin/trimal --version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/mafft --version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/diamond version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/fastq-dump --version
which /opt/conda/envs/PhyloMagnet-$VERSION/bin/FastTree
/opt/conda/envs/PhyloMagnet-$VERSION/bin/iqtree -h
/opt/conda/envs/PhyloMagnet-$VERSION/bin/python3 --version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/raxml-ng -version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/epa-ng --version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/gappa --help
/opt/conda/envs/PhyloMagnet-$VERSION/bin/prank -version
/opt/conda/envs/PhyloMagnet-$VERSION/bin/python3 -c "import ete3"
/usr/local/bin/papara
```

## Collection

 - Name: [maxemil/PhyloMagnet](https://github.com/maxemil/PhyloMagnet)
 - License: [Other](None)

