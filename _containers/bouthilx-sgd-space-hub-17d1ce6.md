---
id: 4942
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "17d1ce6"
commit: "46d1ab04792eed3fc879c4fb555ef8f8ae11137d"
version: "83474d3c1f77d8dd1eabb170bb569042"
build_date: "2018-09-21T20:39:54.736Z"
size_mb: 1903
size: 849596447
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/17d1ce6/2018-09-21-46d1ab04-83474d3c/83474d3c1f77d8dd1eabb170bb569042.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/17d1ce6/2018-09-21-46d1ab04-83474d3c/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/17d1ce6/2018-09-21-46d1ab04-83474d3c/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:17d1ce6

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:17d1ce6
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
        git reset --hard 17d1ce6

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

