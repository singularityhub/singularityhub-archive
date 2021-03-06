---
id: 5043
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "cb12588"
commit: "8aef4ee74d0dcdabb6ccb99f9c779ddfe7938a8f"
version: "f8202657405edcaa12fcbccebebf213b"
build_date: "2018-09-29T10:40:22.787Z"
size_mb: 1903
size: 849739807
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/cb12588/2018-09-29-8aef4ee7-f8202657/f8202657405edcaa12fcbccebebf213b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/cb12588/2018-09-29-8aef4ee7-f8202657/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/cb12588/2018-09-29-8aef4ee7-f8202657/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:cb12588

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:cb12588
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
        git reset --hard cb12588

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

