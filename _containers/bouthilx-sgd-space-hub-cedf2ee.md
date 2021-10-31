---
id: 4824
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "cedf2ee"
commit: "42c8ba241930d9c7494658df96be6eca47539764"
version: "ccd7308ad9d95eeb31b9f66313e1a340"
build_date: "2018-09-16T00:53:04.850Z"
size_mb: 1841
size: 823902239
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/cedf2ee/2018-09-16-42c8ba24-ccd7308a/ccd7308ad9d95eeb31b9f66313e1a340.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/cedf2ee/2018-09-16-42c8ba24-ccd7308a/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/cedf2ee/2018-09-16-42c8ba24-ccd7308a/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:cedf2ee

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:cedf2ee
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
        git reset --hard cedf2ee

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

