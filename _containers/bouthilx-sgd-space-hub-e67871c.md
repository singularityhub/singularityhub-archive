---
id: 4987
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e67871c"
commit: "88c7bf38b378691cd4b66c369237a7e01d2e8d5a"
version: "2c48090bb6f19eefea9a13817e73e7a9"
build_date: "2018-09-26T06:55:03.600Z"
size_mb: 1903
size: 849715231
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e67871c/2018-09-26-88c7bf38-2c48090b/2c48090bb6f19eefea9a13817e73e7a9.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e67871c/2018-09-26-88c7bf38-2c48090b/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e67871c/2018-09-26-88c7bf38-2c48090b/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e67871c

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e67871c
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
        git reset --hard e67871c

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

