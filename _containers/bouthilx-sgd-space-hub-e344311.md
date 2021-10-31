---
id: 4928
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e344311"
commit: "80e47e2a2b6c073407db0922bb6d3c5a89aceb8f"
version: "2c3d613f4c52763d3ef201dbd9732443"
build_date: "2018-09-21T02:27:50.657Z"
size_mb: 1903
size: 849596447
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e344311/2018-09-21-80e47e2a-2c3d613f/2c3d613f4c52763d3ef201dbd9732443.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/e344311/2018-09-21-80e47e2a-2c3d613f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e344311/2018-09-21-80e47e2a-2c3d613f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e344311

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e344311
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
        git reset --hard e344311

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

