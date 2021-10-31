---
id: 8783
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "stringtie"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "a7a401b691404bc6641ef59701153bba"
build_date: "2019-05-08T15:11:14.560Z"
size_mb: 411
size: 151154719
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/stringtie/2019-05-08-5f15386e-a7a401b6/a7a401b691404bc6641ef59701153bba.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/stringtie/2019-05-08-5f15386e-a7a401b6/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/stringtie/2019-05-08-5f15386e-a7a401b6/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:stringtie

```bash
$ singularity pull shub://jlboat/BioinfoContainers:stringtie
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: debian:latest

%help
    singularity run stringtie.simg -h

%post
    apt-get update --fix-missing && apt-get install -y git make g++ libz-dev
    git clone https://github.com/gpertea/stringtie
    cd stringtie
    make release

%runscript
    exec /stringtie/stringtie "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

