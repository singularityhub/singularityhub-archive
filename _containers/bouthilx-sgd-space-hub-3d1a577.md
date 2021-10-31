---
id: 4924
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "3d1a577"
commit: "60a9a1daee8a8c8a0b4531a267f826dad89f157c"
version: "c1e8b3d9c725558d3b64278f37cb144a"
build_date: "2018-09-20T19:10:32.717Z"
size_mb: 1903
size: 849584159
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/3d1a577/2018-09-20-60a9a1da-c1e8b3d9/c1e8b3d9c725558d3b64278f37cb144a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/3d1a577/2018-09-20-60a9a1da-c1e8b3d9/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/3d1a577/2018-09-20-60a9a1da-c1e8b3d9/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:3d1a577

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:3d1a577
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
        git reset --hard 3d1a577

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

