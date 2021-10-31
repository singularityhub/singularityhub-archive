---
id: 11096
name: "cteerara/FenicsSing"
branch: "master"
tag: "def"
commit: "d457cebde2476a455942db72bbf4efda2f3ef59a"
version: "7aee338786415a0c3706945e42bf02e44cd83e92ed2d5216ebe5c5efd717efc8"
build_date: "2019-10-01T05:19:20.774Z"
size_mb: 566.58984375
size: 594112512
sif: "https://datasets.datalad.org/shub/cteerara/FenicsSing/def/2019-10-01-d457cebd-7aee3387/7aee338786415a0c3706945e42bf02e44cd83e92ed2d5216ebe5c5efd717efc8.sif"
url: https://datasets.datalad.org/shub/cteerara/FenicsSing/def/2019-10-01-d457cebd-7aee3387/
recipe: https://datasets.datalad.org/shub/cteerara/FenicsSing/def/2019-10-01-d457cebd-7aee3387/Singularity
collection: cteerara/FenicsSing
---

# cteerara/FenicsSing:def

```bash
$ singularity pull shub://cteerara/FenicsSing:def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/fenicsproject/stable:current

%post
    apt-get -y update
    apt-get -y install libgfortran3
    python3 -m pip install numpy scipy matplotlib 
    apt-get -y update 
    ldconfig

%runscript
    exec /bin/bash -i
```

## Collection

 - Name: [cteerara/FenicsSing](https://github.com/cteerara/FenicsSing)
 - License: None

