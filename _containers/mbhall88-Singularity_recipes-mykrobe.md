---
id: 2227
name: "mbhall88/Singularity_recipes"
branch: "master"
tag: "mykrobe"
commit: "54c141a214e113dfa7366affc7afcdcbf819508b"
version: "09da57a12121bfa7c57cdd5183d9b815"
build_date: "2019-10-29T05:50:16.554Z"
size_mb: 1240
size: 577699871
sif: "https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mykrobe/2019-10-29-54c141a2-09da57a1/09da57a12121bfa7c57cdd5183d9b815.simg"
url: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mykrobe/2019-10-29-54c141a2-09da57a1/
recipe: https://datasets.datalad.org/shub/mbhall88/Singularity_recipes/mykrobe/2019-10-29-54c141a2-09da57a1/Singularity
collection: mbhall88/Singularity_recipes
---

# mbhall88/Singularity_recipes:mykrobe

```bash
$ singularity pull shub://mbhall88/Singularity_recipes:mykrobe
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL:  http://us.archive.ubuntu.com/ubuntu/

%environment
    export PATH=/usr/local/bin:$PATH
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

%post
    apt-get update
    apt-get install -y software-properties-common wget build-essential zlib1g-dev git
    apt-add-repository universe
    apt-get update
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

    # ========================
    # INSTALL Mykrobe
    # ========================
    VERSION=0.7.0
    URL=https://github.com/Mykrobe-tools/mykrobe/archive/v"$VERSION".tar.gz
    apt-get install -y python3-pip mongodb
    wget "$URL" -O - | tar -xzf -
    cd mykrobe*
    wget https://bit.ly/2H9HKTU -O - | tar -vxzf  -
    rm -fr src/mykrobe/data
    mv mykrobe-data src/mykrobe/data
    pip3 install .

# %test
    pip3 install pytest
    mykrobe --help
    mykrobe predict --help
    mykrobe variants --help
    mykrobe genotype --help

    cd /mykrobe*
    # only run tests that dont require mongodb
    pytest tests/metagenomics_tests \
        tests/predict_tests \
        tests/stats_tests \
        tests/typer_tests
```

## Collection

 - Name: [mbhall88/Singularity_recipes](https://github.com/mbhall88/Singularity_recipes)
 - License: [MIT License](https://api.github.com/licenses/mit)

