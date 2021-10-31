---
id: 1506
name: "maxemil/singularity-container"
branch: "master"
tag: "iqtree"
commit: "9633d9a2365bf22bad7e83a8c016fb97ec8069a9"
version: "a8207348b66bc55874a520885ef30263"
build_date: "2018-01-30T14:49:35.398Z"
size_mb: 766
size: 300285983
sif: "https://datasets.datalad.org/shub/maxemil/singularity-container/iqtree/2018-01-30-9633d9a2-a8207348/a8207348b66bc55874a520885ef30263.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/maxemil/singularity-container/iqtree/2018-01-30-9633d9a2-a8207348/
recipe: https://datasets.datalad.org/shub/maxemil/singularity-container/iqtree/2018-01-30-9633d9a2-a8207348/Singularity
collection: maxemil/singularity-container
---

# maxemil/singularity-container:iqtree

```bash
$ singularity pull shub://maxemil/singularity-container:iqtree
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: finalduty/archlinux:daily

%post
######## base system ########
pacman -Syu --noconfirm
pacman -S --noconfirm base-devel git wget

######## IQtree #########
cd /usr/local
wget https://github.com/Cibiv/IQ-TREE/releases/download/v1.6.1/iqtree-1.6.1-Linux.tar.gz
tar -xvf iqtree-1.6.1-Linux.tar.gz
ln -s /usr/local/iqtree-1.6.1-Linux/bin/iqtree /usr/local/bin/iqtree-1.6.1

mkdir /sw /pica /proj /scratch

%test
iqtree-1.6.1 -h

%labels
Maintainer	max-emil.schon@icm.uu.se
```

## Collection

 - Name: [maxemil/singularity-container](https://github.com/maxemil/singularity-container)
 - License: None

