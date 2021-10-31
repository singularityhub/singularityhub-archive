---
id: 8860
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "ncbi-blast+"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "7d0cfc2c6acea0064ea5e5c04fc9ce2f"
build_date: "2020-09-16T08:06:57.615Z"
size_mb: 275
size: 97087519
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/ncbi-blast+/2020-09-16-5f15386e-7d0cfc2c/7d0cfc2c6acea0064ea5e5c04fc9ce2f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jlboat/BioinfoContainers/ncbi-blast+/2020-09-16-5f15386e-7d0cfc2c/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/ncbi-blast+/2020-09-16-5f15386e-7d0cfc2c/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:ncbi-blast+

```bash
$ singularity pull shub://jlboat/BioinfoContainers:ncbi-blast+
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y ncbi-blast+

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

