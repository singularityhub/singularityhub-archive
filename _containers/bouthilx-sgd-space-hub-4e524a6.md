---
id: 5118
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "4e524a6"
commit: "506842e5636ea5b1cf7ed3c1c89c08700ab4d20d"
version: "de94205fbcd5b3bfe0bd9455bd3c73d8"
build_date: "2018-10-04T05:19:39.743Z"
size_mb: 1932
size: 862294047
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4e524a6/2018-10-04-506842e5-de94205f/de94205fbcd5b3bfe0bd9455bd3c73d8.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4e524a6/2018-10-04-506842e5-de94205f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/4e524a6/2018-10-04-506842e5-de94205f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:4e524a6

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:4e524a6
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
        git reset --hard 4e524a6

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

