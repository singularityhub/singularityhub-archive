---
id: 5210
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "b9586bf"
commit: "e006e117e1ea8405b4834bb84fcc65150e4f618b"
version: "f7e4f1e7f49d81bda78e432a39b6b044"
build_date: "2018-10-12T03:09:52.851Z"
size_mb: 1932
size: 862310431
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b9586bf/2018-10-12-e006e117-f7e4f1e7/f7e4f1e7f49d81bda78e432a39b6b044.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/b9586bf/2018-10-12-e006e117-f7e4f1e7/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b9586bf/2018-10-12-e006e117-f7e4f1e7/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:b9586bf

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:b9586bf
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
        git reset --hard b9586bf

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

