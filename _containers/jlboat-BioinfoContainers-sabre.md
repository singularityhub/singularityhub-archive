---
id: 8780
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "sabre"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "cfbadf4b05af1e1d6f318d97f2236810"
build_date: "2019-05-08T15:11:14.458Z"
size_mb: 307
size: 114819103
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/sabre/2019-05-08-5f15386e-cfbadf4b/cfbadf4b05af1e1d6f318d97f2236810.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/sabre/2019-05-08-5f15386e-cfbadf4b/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/sabre/2019-05-08-5f15386e-cfbadf4b/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:sabre

```bash
$ singularity pull shub://jlboat/BioinfoContainers:sabre
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y git gcc make zlib1g zlib1g-dev
    cd /opt/
    git clone https://github.com/najoshi/sabre
    cd sabre
    make
    chmod -R 777 /opt/sabre

%runscript
    exec /opt/sabre/sabre "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

