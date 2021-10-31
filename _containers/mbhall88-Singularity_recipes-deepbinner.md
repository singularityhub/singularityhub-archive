---
id: 3552
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "deepbinner"
commit: "1b71b09c4ad747cd1e96ac7f1978522b31cc2b2d"
version: "6812c725b250fb3dc783c2beb9f9a40a"
build_date: "2020-05-15T07:00:06.524Z"
size_mb: 1334
size: 509128735
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinner/2020-05-15-1b71b09c-6812c725/6812c725b250fb3dc783c2beb9f9a40a.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinner/2020-05-15-1b71b09c-6812c725/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/deepbinner/2020-05-15-1b71b09c-6812c725/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:deepbinner

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:deepbinner
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the nanopore barcode demultiplexer deepbinner.
  Run `singularity exec deepbinner.simg deepbinner`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y wget git python3-pip
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #================================
    # INSTALL DEEPBINNER
    #================================
    git clone https://github.com/rrwick/Deepbinner.git
    cd Deepbinner
    pip3 install -r requirements.txt
    python3 setup.py install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

