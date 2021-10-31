---
id: 3763
name: "idot/Singularity_recipes"
branch: "master"
tag: "nanopolish"
commit: "038971187f22c5838113cac3cc4a314ddb57bb10"
version: "5f268231c9c7f29787c87d5b6b2ecaf7"
build_date: "2018-07-30T16:14:05.745Z"
size_mb: 1048
size: 340152351
sif: "https://datasets.datalad.org/shub/idot/Singularity_recipes/nanopolish/2018-07-30-03897118-5f268231/5f268231c9c7f29787c87d5b6b2ecaf7.simg"
url: https://datasets.datalad.org/shub/idot/Singularity_recipes/nanopolish/2018-07-30-03897118-5f268231/
recipe: https://datasets.datalad.org/shub/idot/Singularity_recipes/nanopolish/2018-07-30-03897118-5f268231/Singularity
collection: idot/Singularity_recipes
---

# idot/Singularity_recipes:nanopolish

```bash
$ singularity pull shub://idot/Singularity_recipes:nanopolish
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

 - Name: [idot/Singularity_recipes](https://github.com/idot/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

