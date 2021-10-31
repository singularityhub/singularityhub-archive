---
id: 5218
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "0bfb161"
commit: "6e284ed5d4d317b2054818ae8d6415fa6d79aae0"
version: "eee25031b36b6137ea142676450fe0ba"
build_date: "2018-10-13T22:17:37.527Z"
size_mb: 1932
size: 862314527
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0bfb161/2018-10-13-6e284ed5-eee25031/eee25031b36b6137ea142676450fe0ba.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/0bfb161/2018-10-13-6e284ed5-eee25031/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/0bfb161/2018-10-13-6e284ed5-eee25031/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:0bfb161

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:0bfb161
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
        git reset --hard 0bfb161

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

