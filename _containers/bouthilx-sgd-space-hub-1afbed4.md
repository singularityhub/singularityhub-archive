---
id: 5074
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "1afbed4"
commit: "b0aea92c3b8e10ff6b2e92ab5fafe53f875e9508"
version: "451c9afaea810a78828fb7637c529911"
build_date: "2018-10-01T22:51:28.786Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/1afbed4/2018-10-01-b0aea92c-451c9afa/451c9afaea810a78828fb7637c529911.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/1afbed4/2018-10-01-b0aea92c-451c9afa/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/1afbed4/2018-10-01-b0aea92c-451c9afa/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:1afbed4

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:1afbed4
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
        git reset --hard 1afbed4

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

