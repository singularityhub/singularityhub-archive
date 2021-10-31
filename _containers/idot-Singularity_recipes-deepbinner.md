---
id: 3762
name: "idot/Singularity_recipes"
branch: "master"
tag: "deepbinner"
commit: "1b71b09c4ad747cd1e96ac7f1978522b31cc2b2d"
version: "fcc9b5dfa87647d388b64c77c9278241"
build_date: "2018-07-30T16:14:05.752Z"
size_mb: 1337
size: 521240607
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/deepbinner/2018-07-30-1b71b09c-fcc9b5df/fcc9b5dfa87647d388b64c77c9278241.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/idot/Singularity_recipes/deepbinner/2018-07-30-1b71b09c-fcc9b5df/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/deepbinner/2018-07-30-1b71b09c-fcc9b5df/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:deepbinner

```bash
$ singularity pull shub://idot/Singularity_recipes:deepbinner
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

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

