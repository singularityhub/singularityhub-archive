---
id: 3368
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "nanopolish"
commit: "8df7771a981a19074c76bc57b1074f5381e3e8f8"
version: "57fc0728f6aecd5f5c5844f737437cc7"
build_date: "2020-05-15T06:49:43.805Z"
size_mb: 1048
size: 340082719
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/nanopolish/2020-05-15-8df7771a-57fc0728/57fc0728f6aecd5f5c5844f737437cc7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/Singularity_recipes/nanopolish/2020-05-15-8df7771a-57fc0728/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/nanopolish/2020-05-15-8df7771a-57fc0728/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:nanopolish

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:nanopolish
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container to hold the assembler nanopolish.
  Run `singularity exec nanopolish.simg canu`

%environment
  PATH=/usr/local/bin:$PATH

%post
    apt update
    apt install -y software-properties-common
    apt-add-repository universe
    apt update
    apt install -y wget build-essential git zlib1g-dev
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    #================================
    # INSTALL NANOPOLISH
    #================================
    VERSION="0.9.2"
    git clone --recursive https://github.com/jts/nanopolish.git
    cd nanopolish
    git checkout v"$VERSION"
    make
    ln -s $(realpath nanopolish) /usr/local/bin/nanopolish
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

