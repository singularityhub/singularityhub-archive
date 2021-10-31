---
id: 8598
name: "MontrealSergiy/bosh"
branch: "master"
tag: "latest"
commit: "d886464d2f3789492be6f71e9d635a7bf9a40f08"
version: "0f377f00ac3870a414da5f7787cb234f"
build_date: "2019-04-23T21:56:10.209Z"
size_mb: 479
size: 182538271
sif: "https://datasets.datalad.org/shub/MontrealSergiy/bosh/latest/2019-04-23-d886464d-0f377f00/0f377f00ac3870a414da5f7787cb234f.simg"
url: https://datasets.datalad.org/shub/MontrealSergiy/bosh/latest/2019-04-23-d886464d-0f377f00/
recipe: https://datasets.datalad.org/shub/MontrealSergiy/bosh/latest/2019-04-23-d886464d-0f377f00/Singularity
collection: MontrealSergiy/bosh
---

# MontrealSergiy/bosh:latest

```bash
$ singularity pull shub://MontrealSergiy/bosh:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post
    apt-get update -y
    apt-get install python3-pip -y
    pip3 install --no-cache-dir --upgrade pip
  
    # delete cache and tmp files
    apt-get clean
    apt-get autoclean 
    rm -rf /var/cache/* 
    rm -rf /tmp/* 
    rm -rf /var/tmp/*
    rm -rf /var/lib/apt/lists/* 
    
    pip install boutiques
```

## Collection

 - Name: [MontrealSergiy/bosh](https://github.com/MontrealSergiy/bosh)
 - License: None

