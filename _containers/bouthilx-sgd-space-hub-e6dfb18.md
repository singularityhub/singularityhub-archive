---
id: 4809
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e6dfb18"
commit: "38fa490423be1ccf5557be4b1f0cc04783752b25"
version: "7dae0f273e5da9bcb3995162f4206601"
build_date: "2018-09-14T11:36:52.001Z"
size_mb: 1841
size: 823885855
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e6dfb18/2018-09-14-38fa4904-7dae0f27/7dae0f273e5da9bcb3995162f4206601.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/e6dfb18/2018-09-14-38fa4904-7dae0f27/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e6dfb18/2018-09-14-38fa4904-7dae0f27/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e6dfb18

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e6dfb18
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
        git reset --hard e6dfb18

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

