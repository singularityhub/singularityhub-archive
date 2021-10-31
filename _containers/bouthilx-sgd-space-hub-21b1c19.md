---
id: 5120
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "21b1c19"
commit: "678af89b8c758cfcf070304c0508202554f9b56d"
version: "a2a2d3a9d9d36b2b802ab4a7af63d735"
build_date: "2018-10-04T05:19:39.729Z"
size_mb: 1932
size: 862298143
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/21b1c19/2018-10-04-678af89b-a2a2d3a9/a2a2d3a9d9d36b2b802ab4a7af63d735.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/21b1c19/2018-10-04-678af89b-a2a2d3a9/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/21b1c19/2018-10-04-678af89b-a2a2d3a9/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:21b1c19

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:21b1c19
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
        git reset --hard 21b1c19

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

