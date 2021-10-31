---
id: 5300
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "b8cc468"
commit: "c8d21ef39b1aba5027e480b694ac28153d976aa9"
version: "924cf36f68a0e83c588a1a23848bfe00"
build_date: "2018-10-22T21:27:18.799Z"
size_mb: 1932
size: 862322719
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b8cc468/2018-10-22-c8d21ef3-924cf36f/924cf36f68a0e83c588a1a23848bfe00.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b8cc468/2018-10-22-c8d21ef3-924cf36f/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/b8cc468/2018-10-22-c8d21ef3-924cf36f/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:b8cc468

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:b8cc468
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
        git reset --hard b8cc468

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

