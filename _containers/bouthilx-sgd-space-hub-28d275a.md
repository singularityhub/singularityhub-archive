---
id: 5017
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "28d275a"
commit: "161567db17390641ea766837788680aa156a1c68"
version: "75e7641aadd03e2b31e3e5fbce640f99"
build_date: "2018-09-28T07:34:32.165Z"
size_mb: 1903
size: 849719327
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/28d275a/2018-09-28-161567db-75e7641a/75e7641aadd03e2b31e3e5fbce640f99.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/28d275a/2018-09-28-161567db-75e7641a/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/28d275a/2018-09-28-161567db-75e7641a/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:28d275a

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:28d275a
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
        git reset --hard 28d275a

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

