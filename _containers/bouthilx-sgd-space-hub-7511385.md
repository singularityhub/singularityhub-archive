---
id: 5126
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "7511385"
commit: "8d42042086d35e80bbe8a051dfd0cd4290ae429c"
version: "b5292da2d0b09e802743e3dba70b88ba"
build_date: "2018-10-04T05:19:39.708Z"
size_mb: 1932
size: 862298143
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/7511385/2018-10-04-8d420420-b5292da2/b5292da2d0b09e802743e3dba70b88ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/7511385/2018-10-04-8d420420-b5292da2/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/7511385/2018-10-04-8d420420-b5292da2/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:7511385

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:7511385
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
        git reset --hard 7511385

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

