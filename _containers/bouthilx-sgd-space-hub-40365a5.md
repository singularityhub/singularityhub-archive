---
id: 4991
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "40365a5"
commit: "813331219c7f805687f62b5cf065fec3a6aecc45"
version: "c6c27e6e96171992eb58aa943365da8a"
build_date: "2018-09-26T06:55:03.581Z"
size_mb: 1903
size: 849715231
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/40365a5/2018-09-26-81333121-c6c27e6e/c6c27e6e96171992eb58aa943365da8a.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/40365a5/2018-09-26-81333121-c6c27e6e/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/40365a5/2018-09-26-81333121-c6c27e6e/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:40365a5

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:40365a5
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
        git reset --hard 40365a5

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

