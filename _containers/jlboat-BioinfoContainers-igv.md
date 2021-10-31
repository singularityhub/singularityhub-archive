---
id: 8777
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "igv"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "016e63c7cc81aa0994d79f21742d28e7"
build_date: "2019-05-08T15:11:14.274Z"
size_mb: 593
size: 254853151
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/igv/2019-05-08-5f15386e-016e63c7/016e63c7cc81aa0994d79f21742d28e7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/igv/2019-05-08-5f15386e-016e63c7/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/igv/2019-05-08-5f15386e-016e63c7/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:igv

```bash
$ singularity pull shub://jlboat/BioinfoContainers:igv
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y wget openjdk-8-jre unzip
    wget http://data.broadinstitute.org/igv/projects/downloads/2.4/IGV_2.4.18.zip
    unzip IGV_2.4.18.zip

%runscript
    exec /IGV_2.4.18/igv.sh
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

