---
id: 4988
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "d42d2fd"
commit: "e26da6b394022a42807cc449942a38de9bfe1593"
version: "2078eeff788a150ace4f1f513fe2ea38"
build_date: "2018-09-26T06:55:03.594Z"
size_mb: 1903
size: 849715231
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/d42d2fd/2018-09-26-e26da6b3-2078eeff/2078eeff788a150ace4f1f513fe2ea38.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/d42d2fd/2018-09-26-e26da6b3-2078eeff/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/d42d2fd/2018-09-26-e26da6b3-2078eeff/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:d42d2fd

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:d42d2fd
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
        git reset --hard d42d2fd

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

