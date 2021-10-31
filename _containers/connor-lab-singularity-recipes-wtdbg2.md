---
id: 7006
name: "connor-lab/singularity-recipes"
branch: "master"
tag: "wtdbg2"
commit: "3b2f76898f2518a737bc995646da3f2092caa156"
version: "03f501316a77b9bc61312164f711e881"
build_date: "2019-02-07T19:57:01.383Z"
size_mb: 389
size: 138969119
sif: "https://datasets.datalad.org/shub/connor-lab/singularity-recipes/wtdbg2/2019-02-07-3b2f7689-03f50131/03f501316a77b9bc61312164f711e881.simg"
url: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/wtdbg2/2019-02-07-3b2f7689-03f50131/
recipe: https://datasets.datalad.org/shub/connor-lab/singularity-recipes/wtdbg2/2019-02-07-3b2f7689-03f50131/Singularity
collection: connor-lab/singularity-recipes
---

# connor-lab/singularity-recipes:wtdbg2

```bash
$ singularity pull shub://connor-lab/singularity-recipes:wtdbg2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:latest

%post
    yum -y update
    yum -y install gcc git make zlib-devel 
    

    cd /usr/local/bin
    git clone https://github.com/ruanjue/wtdbg2.git wtdbg2-latest
    cd wtdbg2-latest && make
    find /usr/local/bin/wtdbg2-latest -maxdepth 1 -type f -executable -exec ln -s {} /usr/local/bin/ \;

%labels
    Maintainer m-bull
    Version wtdbg2-latest
```

## Collection

 - Name: [connor-lab/singularity-recipes](https://github.com/connor-lab/singularity-recipes)
 - License: None

