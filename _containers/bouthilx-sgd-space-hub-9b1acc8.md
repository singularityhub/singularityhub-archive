---
id: 5053
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "9b1acc8"
commit: "8dbc4e40204badba529ecb32593ae9dafad18da4"
version: "a7eac2b905fa8c3f60f96799a583c8f8"
build_date: "2018-10-01T08:41:33.957Z"
size_mb: 1932
size: 862257183
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9b1acc8/2018-10-01-8dbc4e40-a7eac2b9/a7eac2b905fa8c3f60f96799a583c8f8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/9b1acc8/2018-10-01-8dbc4e40-a7eac2b9/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9b1acc8/2018-10-01-8dbc4e40-a7eac2b9/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:9b1acc8

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:9b1acc8
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
        git reset --hard 9b1acc8

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

