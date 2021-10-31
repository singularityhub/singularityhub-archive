---
id: 11085
name: "cteerara/FEniCS_Singularity"
branch: "master"
tag: "recipe"
commit: "a29623debf8c7c30e8830809d6f15b782282f78c"
version: "4fcf26d79f16e9f4d6fedffe69fdbbdc31d5617508da5a00b9bcf71223a2a889"
build_date: "2019-10-01T04:31:38.387Z"
size_mb: 566.2109375
size: 593715200
sif: "https://datasets.datalad.org/shub/cteerara/FEniCS_Singularity/recipe/2019-10-01-a29623de-4fcf26d7/4fcf26d79f16e9f4d6fedffe69fdbbdc31d5617508da5a00b9bcf71223a2a889.sif"
url: https://datasets.datalad.org/shub/cteerara/FEniCS_Singularity/recipe/2019-10-01-a29623de-4fcf26d7/
recipe: https://datasets.datalad.org/shub/cteerara/FEniCS_Singularity/recipe/2019-10-01-a29623de-4fcf26d7/Singularity
collection: cteerara/FEniCS_Singularity
---

# cteerara/FEniCS_Singularity:recipe

```bash
$ singularity pull shub://cteerara/FEniCS_Singularity:recipe
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: quay.io/fenicsproject/stable:current

%post
    apt-get -y update
    python3 -m pip install numpy scipy matplotlib 
    apt-get -y update 
    ldconfig

%runscript
    exec /bin/bash -i
```

## Collection

 - Name: [cteerara/FEniCS_Singularity](https://github.com/cteerara/FEniCS_Singularity)
 - License: None

