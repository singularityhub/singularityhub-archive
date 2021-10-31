---
id: 8820
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "admixture"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "6d025a40036d1218342e84814b8d07c3"
build_date: "2019-05-08T15:55:10.463Z"
size_mb: 113
size: 53551135
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/admixture/2019-05-08-5f15386e-6d025a40/6d025a40036d1218342e84814b8d07c3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/admixture/2019-05-08-5f15386e-6d025a40/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/admixture/2019-05-08-5f15386e-6d025a40/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:admixture

```bash
$ singularity pull shub://jlboat/BioinfoContainers:admixture
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%labels
    Topic Bioinformatics
    admixture 1.3.0

%post
    apt-get update --fix-missing && apt-get install -y wget
    cd /opt
    wget http://software.genetics.ucla.edu/admixture/binaries/admixture_linux-1.3.0.tar.gz
    tar -zxvf admixture_linux-1.3.0.tar.gz
    cd admixture_linux-1.3.0/
    chmod -R 777 /opt/admixture_linux-1.3.0

%runscript
    exec /opt/admixture_linux-1.3.0/admixture "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

