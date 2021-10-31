---
id: 4629
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "khmer"
commit: "f84588bf7b9790fbec5075fa8852f5743a55f053"
version: "e80a367c572aa042495065138701d36d"
build_date: "2018-09-03T17:16:24.263Z"
size_mb: 544
size: 219140127
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/khmer/2018-09-03-f84588bf-e80a367c/e80a367c572aa042495065138701d36d.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/khmer/2018-09-03-f84588bf-e80a367c/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/khmer/2018-09-03-f84588bf-e80a367c/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:khmer

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:khmer
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
    apt -y install wget python2.7-dev python-pip gcc g++
    
	cd /home
    wget https://github.com/dib-lab/khmer/archive/v2.0.tar.gz
    tar -xzf v2.0.tar.gz
    rm v2.0.tar.gz
    pip install khmer
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

