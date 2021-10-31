---
id: 5072
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "f5514a4"
commit: "6c2627253a61f9340f50d896e51eea1d036ff5cf"
version: "fe09a491b49493f979fc0c62ad175287"
build_date: "2018-10-01T22:51:28.800Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/f5514a4/2018-10-01-6c262725-fe09a491/fe09a491b49493f979fc0c62ad175287.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/f5514a4/2018-10-01-6c262725-fe09a491/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/f5514a4/2018-10-01-6c262725-fe09a491/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:f5514a4

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:f5514a4
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
        git reset --hard f5514a4

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

