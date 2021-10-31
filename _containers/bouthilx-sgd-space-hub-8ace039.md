---
id: 4953
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "8ace039"
commit: "b0938ee7d0a17d2b9239f2bb4c72516cde63972d"
version: "0a1fcea2f84be741646fbbe960a0a56c"
build_date: "2018-09-24T07:21:06.417Z"
size_mb: 1903
size: 849575967
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8ace039/2018-09-24-b0938ee7-0a1fcea2/0a1fcea2f84be741646fbbe960a0a56c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/8ace039/2018-09-24-b0938ee7-0a1fcea2/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/8ace039/2018-09-24-b0938ee7-0a1fcea2/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:8ace039

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:8ace039
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
        git reset --hard 8ace039

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

