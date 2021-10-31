---
id: 4916
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "a409de0"
commit: "a41550cd7573c8aa712af33b0993719311d84618"
version: "2a530c74550de8d06881ff14eb1050b7"
build_date: "2018-09-20T01:45:00.237Z"
size_mb: 1903
size: 849580063
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a409de0/2018-09-20-a41550cd-2a530c74/2a530c74550de8d06881ff14eb1050b7.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a409de0/2018-09-20-a41550cd-2a530c74/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a409de0/2018-09-20-a41550cd-2a530c74/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:a409de0

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:a409de0
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
        git reset --hard a409de0

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

