---
id: 4914
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "495d511"
commit: "19c5eeecffd44c621820b7890a276613bb757a82"
version: "dc090d53ac7940be075979b246e1044b"
build_date: "2018-09-19T22:54:40.200Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/495d511/2018-09-19-19c5eeec-dc090d53/dc090d53ac7940be075979b246e1044b.simg"
url: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/495d511/2018-09-19-19c5eeec-dc090d53/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/495d511/2018-09-19-19c5eeec-dc090d53/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:495d511

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:495d511
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
        git reset --hard 495d511

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

