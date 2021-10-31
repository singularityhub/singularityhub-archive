---
id: 4970
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "42f0f3c"
commit: "7985c118565c2ac7564546bc5ff2242e67a3bbd7"
version: "9c7342abfa415e063943612bd8772a3b"
build_date: "2018-09-25T05:46:39.922Z"
size_mb: 1903
size: 849588255
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/42f0f3c/2018-09-25-7985c118-9c7342ab/9c7342abfa415e063943612bd8772a3b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/42f0f3c/2018-09-25-7985c118-9c7342ab/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/42f0f3c/2018-09-25-7985c118-9c7342ab/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:42f0f3c

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:42f0f3c
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
        git reset --hard 42f0f3c

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

