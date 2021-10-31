---
id: 5303
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "95bb021"
commit: "0b496cec1c58917841a78cbebced396b379fc89a"
version: "02a9025ade12df589df01a6edc8f6272"
build_date: "2018-10-22T21:27:18.779Z"
size_mb: 1932
size: 862326815
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/95bb021/2018-10-22-0b496cec-02a9025a/02a9025ade12df589df01a6edc8f6272.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/95bb021/2018-10-22-0b496cec-02a9025a/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/95bb021/2018-10-22-0b496cec-02a9025a/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:95bb021

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:95bb021
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
        git reset --hard 95bb021

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

