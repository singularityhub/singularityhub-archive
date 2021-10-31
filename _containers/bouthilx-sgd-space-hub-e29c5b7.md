---
id: 5069
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "e29c5b7"
commit: "85fb7379a4ca57d9b672025c62d2027482b6a420"
version: "cec2c00653fdd9fdc177061134dd7a21"
build_date: "2018-10-01T22:51:28.806Z"
size_mb: 1932
size: 862281759
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e29c5b7/2018-10-01-85fb7379-cec2c006/cec2c00653fdd9fdc177061134dd7a21.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e29c5b7/2018-10-01-85fb7379-cec2c006/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/e29c5b7/2018-10-01-85fb7379-cec2c006/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:e29c5b7

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:e29c5b7
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
        git reset --hard e29c5b7

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

