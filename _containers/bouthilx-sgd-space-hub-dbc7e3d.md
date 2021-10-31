---
id: 4925
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "dbc7e3d"
commit: "35e021e38de6a42a81ccbcaf50eb0f62e128c32c"
version: "f81c52bd7ee9feb17be58dbe335f361c"
build_date: "2018-09-21T02:27:50.663Z"
size_mb: 1903
size: 849588255
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dbc7e3d/2018-09-21-35e021e3-f81c52bd/f81c52bd7ee9feb17be58dbe335f361c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/dbc7e3d/2018-09-21-35e021e3-f81c52bd/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dbc7e3d/2018-09-21-35e021e3-f81c52bd/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:dbc7e3d

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:dbc7e3d
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
        git reset --hard dbc7e3d

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

