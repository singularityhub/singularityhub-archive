---
id: 4909
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "1a4016b"
commit: "e06cabbe04ce6a3dadb0e61065d1ba67fe1bc0c0"
version: "bf001e26bd0ab56043617a131919b627"
build_date: "2018-09-19T22:54:40.213Z"
size_mb: 1903
size: 849571871
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/1a4016b/2018-09-19-e06cabbe-bf001e26/bf001e26bd0ab56043617a131919b627.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/1a4016b/2018-09-19-e06cabbe-bf001e26/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/1a4016b/2018-09-19-e06cabbe-bf001e26/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:1a4016b

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:1a4016b
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
        git reset --hard 1a4016b

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

