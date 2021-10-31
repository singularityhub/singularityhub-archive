---
id: 5467
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "porechop"
commit: "c45bed96c50e230a37fe94bda3d991b41c41620f"
version: "3499ffb89a2bbc6e7945f07620541b3e"
build_date: "2019-09-13T08:25:48.729Z"
size_mb: 633
size: 227250207
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/porechop/2019-09-13-c45bed96-3499ffb8/3499ffb89a2bbc6e7945f07620541b3e.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/porechop/2019-09-13-c45bed96-3499ffb8/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/porechop/2019-09-13-c45bed96-3499ffb8/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:porechop

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:porechop
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

    # ================================
    # INSTALL porechop 
    # ================================
    VERSION="0.2.4"
    URL=https://github.com/rrwick/Porechop/archive/v"$VERSION".tar.gz
    apt-get install -y python3-setuptools \
        python3-pkg-resources \
        python3-distutils \
        python3-lib2to3
    wget -O - "$URL" | tar xzf -
    cd Porechop*
    python3 setup.py install
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

