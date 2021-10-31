---
id: 11095
name: "cteerara/FEniCS_Singularity"
branch: "master"
tag: "def"
commit: "d8a89bc538b8015adb6140206a089ea819c27793"
version: "f206010f3d1567d06c0b0a8245c48c081e6b22555be6cbd59d01e4298118ccad"
build_date: "2019-10-01T04:58:42.016Z"
size_mb: 566.58984375
size: 594112512
sif: "https://datasets.datalad.org/shub/cteerara/FEniCS_Singularity/def/2019-10-01-d8a89bc5-f206010f/f206010f3d1567d06c0b0a8245c48c081e6b22555be6cbd59d01e4298118ccad.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cteerara/FEniCS_Singularity/def/2019-10-01-d8a89bc5-f206010f/
recipe: https://datasets.datalad.org/shub/cteerara/FEniCS_Singularity/def/2019-10-01-d8a89bc5-f206010f/Singularity
collection: cteerara/FEniCS_Singularity
---

# cteerara/FEniCS_Singularity:def

```bash
$ singularity pull shub://cteerara/FEniCS_Singularity:def
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

 - Name: [cteerara/FEniCS_Singularity](https://github.com/cteerara/FEniCS_Singularity)
 - License: None

