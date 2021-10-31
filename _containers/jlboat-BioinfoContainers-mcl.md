---
id: 8859
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "mcl"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "b48ccc5ecb55ab7b970d1e4b4cc5990a"
build_date: "2019-05-08T15:11:14.356Z"
size_mb: 131
size: 56786975
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/mcl/2019-05-08-5f15386e-b48ccc5e/b48ccc5ecb55ab7b970d1e4b4cc5990a.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/mcl/2019-05-08-5f15386e-b48ccc5e/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/mcl/2019-05-08-5f15386e-b48ccc5e/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:mcl

```bash
$ singularity pull shub://jlboat/BioinfoContainers:mcl
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%post
    apt-get update --fix-missing && apt-get install -y mcl

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

