---
id: 5302
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "98d61b9"
commit: "13d94be71014fc044a1d9a48dce6040f019e586e"
version: "22d5632c16cd9f101922c988826ffe62"
build_date: "2018-10-22T21:27:18.786Z"
size_mb: 1932
size: 862326815
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/98d61b9/2018-10-22-13d94be7-22d5632c/22d5632c16cd9f101922c988826ffe62.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/98d61b9/2018-10-22-13d94be7-22d5632c/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/98d61b9/2018-10-22-13d94be7-22d5632c/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:98d61b9

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:98d61b9
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
        git reset --hard 98d61b9

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

