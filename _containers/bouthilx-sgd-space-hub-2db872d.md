---
id: 4823
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "2db872d"
commit: "e75ea61337c3d09bd3848335fe7c60915a981294"
version: "b8f53504a5c6f72a61ad844d65d4c942"
build_date: "2018-09-16T00:53:04.855Z"
size_mb: 1841
size: 823898143
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2db872d/2018-09-16-e75ea613-b8f53504/b8f53504a5c6f72a61ad844d65d4c942.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2db872d/2018-09-16-e75ea613-b8f53504/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2db872d/2018-09-16-e75ea613-b8f53504/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:2db872d

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:2db872d
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
        git reset --hard 2db872d

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

