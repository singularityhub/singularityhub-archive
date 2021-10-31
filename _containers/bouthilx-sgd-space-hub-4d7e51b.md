---
id: 4735
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "4d7e51b"
commit: "e02a2848f5ce08f61cdaac4bae5c0c7a05dec690"
version: "eede9edaab217cd6703d3e6d55cc6fb9"
build_date: "2018-09-10T04:18:56.680Z"
size_mb: 1841
size: 823861279
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4d7e51b/2018-09-10-e02a2848-eede9eda/eede9edaab217cd6703d3e6d55cc6fb9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/4d7e51b/2018-09-10-e02a2848-eede9eda/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4d7e51b/2018-09-10-e02a2848-eede9eda/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:4d7e51b

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:4d7e51b
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.0.4.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    SGD_SPACE_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Installing kleio prototype"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/epistimio/kleio.git@prototype

    echo "------------------------------------------------------"
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard 4d7e51b

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install -e sgd-space

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/sgd-space-hub](https://github.com/bouthilx/sgd-space-hub)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

