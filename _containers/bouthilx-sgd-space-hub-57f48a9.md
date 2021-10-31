---
id: 4971
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "57f48a9"
commit: "51ea733005ca2efea648cc4c399162e86843301c"
version: "a87368bacff8d171b589033a04e5c3ac"
build_date: "2018-09-25T05:46:39.915Z"
size_mb: 1903
size: 849588255
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/57f48a9/2018-09-25-51ea7330-a87368ba/a87368bacff8d171b589033a04e5c3ac.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/57f48a9/2018-09-25-51ea7330-a87368ba/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/57f48a9/2018-09-25-51ea7330-a87368ba/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:57f48a9

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:57f48a9
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
        git reset --hard 57f48a9

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

