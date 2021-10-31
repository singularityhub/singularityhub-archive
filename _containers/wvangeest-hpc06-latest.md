---
id: 11765
name: "wvangeest/hpc06"
branch: "master"
tag: "latest"
commit: "cd9ffe27ae4d8659f873aa03e63816d4f5f50096"
version: "780e33f908e22412d1cec419ecaaf0ed"
build_date: "2019-12-05T14:11:58.312Z"
size_mb: 2603.0
size: 1736069151
sif: "https://datasets.datalad.org/shub/wvangeest/hpc06/latest/2019-12-05-cd9ffe27-780e33f9/780e33f908e22412d1cec419ecaaf0ed.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/wvangeest/hpc06/latest/2019-12-05-cd9ffe27-780e33f9/
recipe: https://datasets.datalad.org/shub/wvangeest/hpc06/latest/2019-12-05-cd9ffe27-780e33f9/Singularity
collection: wvangeest/hpc06
---

# wvangeest/hpc06:latest

```bash
$ singularity pull shub://wvangeest/hpc06:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%runscript
    exec echo "This is your own Ubuntu singularity!"

%labels
    AUTHOR w.j.m.vangeest@tudelft.nl

%post
    apt-get update && apt-get -y install python3 python3-pip git wget
    apt-get update && apt-get -y upgrade
    pip3 install torch
```

## Collection

 - Name: [wvangeest/hpc06](https://github.com/wvangeest/hpc06)
 - License: None

