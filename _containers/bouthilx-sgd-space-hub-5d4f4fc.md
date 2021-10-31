---
id: 4990
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "5d4f4fc"
commit: "3cb2828b231f59a128cbf9afa7f5da799b29b4d8"
version: "91cce9113faeda749eb932219b40b3ff"
build_date: "2018-09-26T06:55:03.588Z"
size_mb: 1903
size: 849715231
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/5d4f4fc/2018-09-26-3cb2828b-91cce911/91cce9113faeda749eb932219b40b3ff.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/5d4f4fc/2018-09-26-3cb2828b-91cce911/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/5d4f4fc/2018-09-26-3cb2828b-91cce911/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:5d4f4fc

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:5d4f4fc
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
        git reset --hard 5d4f4fc

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

