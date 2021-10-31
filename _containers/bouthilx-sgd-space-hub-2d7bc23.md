---
id: 4857
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "2d7bc23"
commit: "030cda26e35e1b2f55f1fc25e69a132764f5f60b"
version: "71fe735408a3c15ca770eee2a37735e0"
build_date: "2018-09-18T03:28:18.899Z"
size_mb: 1857
size: 830660639
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d7bc23/2018-09-18-030cda26-71fe7354/71fe735408a3c15ca770eee2a37735e0.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d7bc23/2018-09-18-030cda26-71fe7354/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d7bc23/2018-09-18-030cda26-71fe7354/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:2d7bc23

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:2d7bc23
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
        git reset --hard 2d7bc23

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

