---
id: 4730
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "c2fa0e3"
commit: "d1abdaf1272b8029f479a98a58b8f9523b771e57"
version: "94d44289f98e4e27e781fa7fada15cb1"
build_date: "2018-09-10T04:18:56.694Z"
size_mb: 1841
size: 823857183
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/c2fa0e3/2018-09-10-d1abdaf1-94d44289/94d44289f98e4e27e781fa7fada15cb1.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/c2fa0e3/2018-09-10-d1abdaf1-94d44289/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/c2fa0e3/2018-09-10-d1abdaf1-94d44289/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:c2fa0e3

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:c2fa0e3
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
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard c2fa0e3

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install -e sgd-space

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

