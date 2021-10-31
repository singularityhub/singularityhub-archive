---
id: 5211
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "8193418"
commit: "9b13caf3e1a79956065689e26f577fa2bcd0b7a5"
version: "02ccdb715a5c6a43821ca4dc7a5b42c7"
build_date: "2018-10-12T03:09:52.845Z"
size_mb: 1932
size: 862310431
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8193418/2018-10-12-9b13caf3-02ccdb71/02ccdb715a5c6a43821ca4dc7a5b42c7.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8193418/2018-10-12-9b13caf3-02ccdb71/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8193418/2018-10-12-9b13caf3-02ccdb71/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:8193418

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:8193418
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
        git reset --hard 8193418

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

