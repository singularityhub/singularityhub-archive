---
id: 4955
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "f928eb8"
commit: "96e824cdc70b737dfc37b976bb5af6536bc01ae1"
version: "b78fca88eaf30aec479e419b2c7996be"
build_date: "2018-09-24T07:21:06.410Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/f928eb8/2018-09-24-96e824cd-b78fca88/b78fca88eaf30aec479e419b2c7996be.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/f928eb8/2018-09-24-96e824cd-b78fca88/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/f928eb8/2018-09-24-96e824cd-b78fca88/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:f928eb8

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:f928eb8
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
        git reset --hard f928eb8

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

