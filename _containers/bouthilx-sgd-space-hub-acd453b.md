---
id: 4968
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "acd453b"
commit: "69ca11d9eb759cae779997b445f214f080f94dad"
version: "68f3dd10c272ccc845c3ee3cbc56c2ac"
build_date: "2018-09-25T05:46:39.929Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/acd453b/2018-09-25-69ca11d9-68f3dd10/68f3dd10c272ccc845c3ee3cbc56c2ac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/acd453b/2018-09-25-69ca11d9-68f3dd10/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/acd453b/2018-09-25-69ca11d9-68f3dd10/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:acd453b

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:acd453b
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
        git reset --hard acd453b

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

