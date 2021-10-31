---
id: 8774
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "hisat2"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "5d6d9cd8106d7ba1681d98c5ccb4b661"
build_date: "2019-09-24T17:55:41.866Z"
size_mb: 277
size: 124588063
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/hisat2/2019-09-24-5f15386e-5d6d9cd8/5d6d9cd8106d7ba1681d98c5ccb4b661.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/hisat2/2019-09-24-5f15386e-5d6d9cd8/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/hisat2/2019-09-24-5f15386e-5d6d9cd8/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:hisat2

```bash
$ singularity pull shub://jlboat/BioinfoContainers:hisat2
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%environment
    PATH=$PATH:/hisat2-2.1.0

%post
    apt-get update --fix-missing && apt-get install -y wget unzip python
    apt-get clean && apt-get purge
    wget http://ccb.jhu.edu/software/hisat2/dl/hisat2-2.1.0-Linux_x86_64.zip
    unzip hisat2-2.1.0-Linux_x86_64.zip

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

