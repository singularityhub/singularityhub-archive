---
id: 4750
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "b4c750e"
commit: "ad2b624a8c25a683a94b2a0d847fd7163af416d7"
version: "e13f7f8431763210d84e4c7120b864a6"
build_date: "2018-09-12T04:10:17.769Z"
size_mb: 1841
size: 823869471
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b4c750e/2018-09-12-ad2b624a-e13f7f84/e13f7f8431763210d84e4c7120b864a6.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b4c750e/2018-09-12-ad2b624a-e13f7f84/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b4c750e/2018-09-12-ad2b624a-e13f7f84/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:b4c750e

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:b4c750e
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
        git reset --hard b4c750e

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

