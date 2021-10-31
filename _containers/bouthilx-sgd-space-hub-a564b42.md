---
id: 4967
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "a564b42"
commit: "d94440a72ffea8c3accd9090cbad3bb858c95d05"
version: "b84e17e376a42ade79027723942416d3"
build_date: "2018-09-25T05:46:39.936Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a564b42/2018-09-25-d94440a7-b84e17e3/b84e17e376a42ade79027723942416d3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/a564b42/2018-09-25-d94440a7-b84e17e3/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/a564b42/2018-09-25-d94440a7-b84e17e3/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:a564b42

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:a564b42
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
        git reset --hard a564b42

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

