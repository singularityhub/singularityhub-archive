---
id: 4634
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "metabat"
commit: "0fc51ccaf70f7db45129dbdb3b353d2f22300185"
version: "3a28d3b7367d3ab6730a8a5eb61578ca"
build_date: "2018-09-03T17:16:24.242Z"
size_mb: 218
size: 91545631
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metabat/2018-09-03-0fc51cca-3a28d3b7/3a28d3b7367d3ab6730a8a5eb61578ca.simg"
url: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metabat/2018-09-03-0fc51cca-3a28d3b7/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/metabat/2018-09-03-0fc51cca-3a28d3b7/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:metabat

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:metabat
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget python
    
	cd /home
    wget https://bitbucket.org/berkeleylab/metabat/downloads/metabat-static-binary-linux-x64_v2.12.1.tar.gz
    tar -xzf metabat-static-binary-linux-x64_v2.12.1.tar.gz
    rm metabat-static-binary-linux-x64_v2.12.1.tar.gz
    chmod +x metabat/*
    mv metabat/* /usr/local/bin
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

