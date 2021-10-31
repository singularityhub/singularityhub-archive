---
id: 5547
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "mummer"
commit: "442878c964afcaa4c5ddd19c17cccee6cc010974"
version: "f269bcc949b591e03b57ce1d6fa1b778"
build_date: "2018-11-11T00:03:03.114Z"
size_mb: 620
size: 226455583
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mummer/2018-11-11-442878c9-f269bcc9/f269bcc949b591e03b57ce1d6fa1b778.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mummer/2018-11-11-442878c9-f269bcc9/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mummer/2018-11-11-442878c9-f269bcc9/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:mummer

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:mummer
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
    apt install -y git wget build-essential
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    echo 'export LC_ALL=C.UTF-8' >> $SINGULARITY_ENVIRONMENT
    echo 'export LANG=C.UTF-8' >> $SINGULARITY_ENVIRONMENT

    # ========================
    # INSTALL mummer
    # ========================
    apt install -y csh

    VERSION="3.23"
    URL=https://sourceforge.net/projects/mummer/files/mummer/"$VERSION"/MUMmer"$VERSION".tar.gz/download
    wget -O - "$URL" | tar xzf -
    cd MUMmer*
    make install
    echo "export PATH=$(pwd):$PATH" >> $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

