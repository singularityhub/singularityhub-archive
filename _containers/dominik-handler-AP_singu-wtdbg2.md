---
id: 8626
name: "dominik-handler/AP_singu"
branch: "master"
tag: "wtdbg2"
commit: "06114618bd611da070c379d22be072dd2dade263"
version: "6c6c7d1d27868efe5d04f2bb0f3be38e"
build_date: "2019-04-24T11:31:09.102Z"
size_mb: 425
size: 165457951
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/wtdbg2/2019-04-24-06114618-6c6c7d1d/6c6c7d1d27868efe5d04f2bb0f3be38e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/wtdbg2/2019-04-24-06114618-6c6c7d1d/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/wtdbg2/2019-04-24-06114618-6c6c7d1d/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:wtdbg2

```bash
$ singularity pull shub://dominik-handler/AP_singu:wtdbg2
```

## Singularity Recipe

```singularity
#wtdbg2 in singularity

Bootstrap: docker
From: ubuntu:16.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  wtdbg2 v2.4 

%runscript
    wtdbg2 "$@"

%post
    apt-get update
    apt-get --assume-yes install wget curl apt-utils

    apt-get update
    apt-get -y install build-essential cmake git-core zlib1g-dev
       
    cd /
    git clone https://github.com/ruanjue/wtdbg2
    cd wtdbg2 && make    

    mkdir /groups
    mkdir /scratch
    mkdir /scratch-ii2

%environment
    PATH=/wtdbg2/:$PATH
    export PATH

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

