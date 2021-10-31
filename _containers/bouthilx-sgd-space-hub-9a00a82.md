---
id: 5038
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "9a00a82"
commit: "56b5d5bda3fe122c97321d49404131148fd78ff8"
version: "26baa8add03a461857483aabdb88518e"
build_date: "2018-09-29T10:40:22.807Z"
size_mb: 1903
size: 849727519
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9a00a82/2018-09-29-56b5d5bd-26baa8ad/26baa8add03a461857483aabdb88518e.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9a00a82/2018-09-29-56b5d5bd-26baa8ad/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/9a00a82/2018-09-29-56b5d5bd-26baa8ad/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:9a00a82

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:9a00a82
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
        git reset --hard 9a00a82

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

