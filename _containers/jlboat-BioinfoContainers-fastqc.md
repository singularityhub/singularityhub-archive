---
id: 8773
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "fastqc"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "d9971b3acc1d414066f3b7e9396a972f"
build_date: "2021-03-06T01:05:19.949Z"
size_mb: 559
size: 207487007
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastqc/2021-03-06-5f15386e-d9971b3a/d9971b3acc1d414066f3b7e9396a972f.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastqc/2021-03-06-5f15386e-d9971b3a/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastqc/2021-03-06-5f15386e-d9971b3a/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:fastqc

```bash
$ singularity pull shub://jlboat/BioinfoContainers:fastqc
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget
    apt-get install -y zip default-jre perl
    wget --quiet https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.8.zip -O /opt/fastqc_v0.11.8.zip
    unzip /opt/fastqc_v0.11.8.zip
    rm /opt/fastqc_v0.11.8.zip
    chmod a+x /FastQC/fastqc

%runscript
    exec /FastQC/fastqc "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

