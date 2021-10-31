---
id: 4981
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "58a31a0"
commit: "9bce5898ed5838173e24fa3b3731e44fdb132236"
version: "236608b5a5d0c2400a7f1031940ade88"
build_date: "2018-09-26T06:55:03.606Z"
size_mb: 1903
size: 849711135
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/58a31a0/2018-09-26-9bce5898-236608b5/236608b5a5d0c2400a7f1031940ade88.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/58a31a0/2018-09-26-9bce5898-236608b5/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/58a31a0/2018-09-26-9bce5898-236608b5/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:58a31a0

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:58a31a0
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
    echo "Installing flow"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/flow.git

    echo "------------------------------------------------------"
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard 58a31a0

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install -e sgd-space[execute,deploy]

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

