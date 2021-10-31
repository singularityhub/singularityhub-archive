---
id: 5075
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "2d113da"
commit: "58f5239a73fc55b7f0281d3a9fc28933945047f7"
version: "8715f52f2cbf7e93f8bc697d22ce65b1"
build_date: "2018-10-02T00:04:18.877Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d113da/2018-10-02-58f5239a-8715f52f/8715f52f2cbf7e93f8bc697d22ce65b1.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d113da/2018-10-02-58f5239a-8715f52f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2d113da/2018-10-02-58f5239a-8715f52f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:2d113da

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:2d113da
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
        git reset --hard 2d113da

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

