---
id: 3693
name: "dominik-handler/AP_singu"
branch: "master"
tag: "minimap2"
commit: "0f5efa64baaa1ba282b2b10da88d2903b6a1c453"
version: "3f3b1354722e0f8526bc8871964696e0bb4801088cc1b4333e6da15bd2850642"
build_date: "2020-10-18T05:44:04.364Z"
size_mb: 126.8984375
size: 133062656
sif: "https://datasets.datalad.org/shub/dominik-handler/AP_singu/minimap2/2020-10-18-0f5efa64-3f3b1354/3f3b1354722e0f8526bc8871964696e0bb4801088cc1b4333e6da15bd2850642.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/dominik-handler/AP_singu/minimap2/2020-10-18-0f5efa64-3f3b1354/
recipe: https://datasets.datalad.org/shub/dominik-handler/AP_singu/minimap2/2020-10-18-0f5efa64-3f3b1354/Singularity
collection: dominik-handler/AP_singu
---

# dominik-handler/AP_singu:minimap2

```bash
$ singularity pull shub://dominik-handler/AP_singu:minimap2
```

## Singularity Recipe

```singularity
#minimap2 in singularity

Bootstrap: docker
From: ubuntu:18.04

%labels
  maintainer Dominik Handler <Dominik Handler@imba.oeaw.ac.at>
  minimap2 @ 081df6a

%runscript
    "$@"

%post
    apt-get update
    apt-get --assume-yes install wget curl bzip2 git-core build-essential zlib1g-dev

    git clone https://github.com/lh3/minimap2
    cd minimap2 && make
    cp minimap2 /usr/bin 

%environment

%test
```

## Collection

 - Name: [dominik-handler/AP_singu](https://github.com/dominik-handler/AP_singu)
 - License: None

