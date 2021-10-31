---
id: 5073
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "dc8e55e"
commit: "9214cbb886e800f2b77a1936777bfa5415523005"
version: "47915259ece945292bb40ba911e4f56d"
build_date: "2018-10-01T22:51:28.793Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dc8e55e/2018-10-01-9214cbb8-47915259/47915259ece945292bb40ba911e4f56d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/dc8e55e/2018-10-01-9214cbb8-47915259/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dc8e55e/2018-10-01-9214cbb8-47915259/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:dc8e55e

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:dc8e55e
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
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard dc8e55e

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e sgd-space[execute,configure,deploy]

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

