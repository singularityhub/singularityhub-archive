---
id: 8775
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "hmmsplicer"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "d9bd9b493fd9689a726039a9f28cdbf6"
build_date: "2019-05-08T15:11:14.224Z"
size_mb: 292
size: 127434783
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/hmmsplicer/2019-05-08-5f15386e-d9bd9b49/d9bd9b493fd9689a726039a9f28cdbf6.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/hmmsplicer/2019-05-08-5f15386e-d9bd9b49/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/hmmsplicer/2019-05-08-5f15386e-d9bd9b49/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:hmmsplicer

```bash
$ singularity pull shub://jlboat/BioinfoContainers:hmmsplicer
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%environment
    PATH=$PATH:/hmmSplicer-0.9.5/

%post
    apt-get update --fix-missing && apt-get install -y wget python
    wget http://derisilab.ucsf.edu/software/HMMSplicer/hmmSplicer-0.9.5.tar.gz
    tar -zxvf hmmSplicer-0.9.5.tar.gz
    chmod -R 777 hmmSplicer-0.9.5/

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

