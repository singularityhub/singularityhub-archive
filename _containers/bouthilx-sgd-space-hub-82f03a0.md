---
id: 5041
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "82f03a0"
commit: "9eb503c3fc3a5b520776f4a2b91747bb4252badc"
version: "8394875565b7f62460c505d82f22149c"
build_date: "2018-09-29T10:40:22.801Z"
size_mb: 1903
size: 849731615
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/82f03a0/2018-09-29-9eb503c3-83948755/8394875565b7f62460c505d82f22149c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/82f03a0/2018-09-29-9eb503c3-83948755/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/82f03a0/2018-09-29-9eb503c3-83948755/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:82f03a0

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:82f03a0
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
        git reset --hard 82f03a0

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

