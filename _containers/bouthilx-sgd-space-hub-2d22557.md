---
id: 4888
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "2d22557"
commit: "22d0c01171781699e5f5787a250045261b0f0967"
version: "c7e609500381714677ef40c255b92119"
build_date: "2018-09-19T07:00:18.479Z"
size_mb: 1830
size: 819130399
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d22557/2018-09-19-22d0c011-c7e60950/c7e609500381714677ef40c255b92119.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d22557/2018-09-19-22d0c011-c7e60950/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d22557/2018-09-19-22d0c011-c7e60950/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:2d22557

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:2d22557
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
        git reset --hard 2d22557

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

