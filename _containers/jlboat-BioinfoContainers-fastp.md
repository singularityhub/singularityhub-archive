---
id: 8772
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "fastp"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "4e42d1f1f92022f29c4016d02906ae4f"
build_date: "2021-01-20T15:19:39.950Z"
size_mb: 117
size: 52506655
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastp/2021-01-20-5f15386e-4e42d1f1/4e42d1f1f92022f29c4016d02906ae4f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/fastp/2021-01-20-5f15386e-4e42d1f1/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/fastp/2021-01-20-5f15386e-4e42d1f1/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:fastp

```bash
$ singularity pull shub://jlboat/BioinfoContainers:fastp
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:latest

%post
    apt-get update --fix-missing && apt-get install -y wget
    wget --quiet http://opengene.org/fastp/fastp -O /opt/fastp
    chmod 777 /opt/fastp

%runscript
    exec /opt/fastp "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

