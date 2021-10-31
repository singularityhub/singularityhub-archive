---
id: 5579
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "clustalo"
commit: "c0af79dc032d20c5ae72f756e67aa8e6e0015256"
version: "471147b74611e8faf0cfd72e56f6262f"
build_date: "2020-12-05T15:43:09.717Z"
size_mb: 363
size: 140050463
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/clustalo/2020-12-05-c0af79dc-471147b7/471147b74611e8faf0cfd72e56f6262f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/clustalo/2020-12-05-c0af79dc-471147b7/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/clustalo/2020-12-05-c0af79dc-471147b7/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:clustalo

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:clustalo
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    # apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ========================
    # INSTALL clustal omega
    # ========================
    apt install -y clustalo
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

