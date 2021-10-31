---
id: 4912
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "2446115"
commit: "a26e2bdb9fd1788afea32c83d969cfff87c31e5c"
version: "3ee244765a3cdf038e5d68e460db3879"
build_date: "2018-09-19T22:54:40.207Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2446115/2018-09-19-a26e2bdb-3ee24476/3ee244765a3cdf038e5d68e460db3879.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/2446115/2018-09-19-a26e2bdb-3ee24476/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/2446115/2018-09-19-a26e2bdb-3ee24476/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:2446115

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:2446115
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
        git reset --hard 2446115

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

