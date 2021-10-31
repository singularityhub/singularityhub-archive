---
id: 4611
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "dev"
commit: "34d197a1c58402dcdf93c334967671e6147d834c"
version: "717652a8ee5ea78d56168dffe459c7e9"
build_date: "2018-09-06T01:51:16.626Z"
size_mb: 1836
size: 822480927
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dev/2018-09-06-34d197a1-717652a8/717652a8ee5ea78d56168dffe459c7e9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/dev/2018-09-06-34d197a1-717652a8/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/dev/2018-09-06-34d197a1-717652a8/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:dev

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:dev
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
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install -e sgd-space

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

