---
id: 4940
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "7b2cfcd"
commit: "ff555426827f6a5d675ea73650235fb936563755"
version: "7df14b3fe6d4e24b836d379a0c0ab413"
build_date: "2018-09-21T20:39:54.744Z"
size_mb: 1903
size: 849604639
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/7b2cfcd/2018-09-21-ff555426-7df14b3f/7df14b3fe6d4e24b836d379a0c0ab413.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/7b2cfcd/2018-09-21-ff555426-7df14b3f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/7b2cfcd/2018-09-21-ff555426-7df14b3f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:7b2cfcd

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:7b2cfcd
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
        git reset --hard 7b2cfcd

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

