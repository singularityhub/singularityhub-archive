---
id: 4900
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "0cb1db5"
commit: "fc0bd683a75226452a1bbff32ca82f7114a0cc1d"
version: "031b3ac639ac42b0f3f45c4da1414f57"
build_date: "2018-09-19T07:00:18.472Z"
size_mb: 1903
size: 849547295
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0cb1db5/2018-09-19-fc0bd683-031b3ac6/031b3ac639ac42b0f3f45c4da1414f57.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/0cb1db5/2018-09-19-fc0bd683-031b3ac6/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0cb1db5/2018-09-19-fc0bd683-031b3ac6/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:0cb1db5

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:0cb1db5
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
        git reset --hard 0cb1db5

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

