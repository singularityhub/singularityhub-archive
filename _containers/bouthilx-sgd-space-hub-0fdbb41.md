---
id: 4825
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "0fdbb41"
commit: "2ce1d7a9394ff2c3db6981e5273feaaa70bed279"
version: "8129093f813a2535e321cc87fc5a50f9"
build_date: "2018-09-16T00:53:04.843Z"
size_mb: 1841
size: 823902239
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0fdbb41/2018-09-16-2ce1d7a9-8129093f/8129093f813a2535e321cc87fc5a50f9.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0fdbb41/2018-09-16-2ce1d7a9-8129093f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0fdbb41/2018-09-16-2ce1d7a9-8129093f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:0fdbb41

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:0fdbb41
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
        git reset --hard 0fdbb41

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

