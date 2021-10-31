---
id: 5974
name: "bouthilx/repro-hub"
branch: "master"
tag: "4440107"
commit: "7ef6b8e6a5c1e00c86af6732bbcadeb9f0277333"
version: "b030cded5fc4f72cecec8853826e70e7"
build_date: "2018-12-15T06:55:31.589Z"
size_mb: 2499
size: 1521696799
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/4440107/2018-12-15-7ef6b8e6-b030cded/b030cded5fc4f72cecec8853826e70e7.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/4440107/2018-12-15-7ef6b8e6-b030cded/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/4440107/2018-12-15-7ef6b8e6-b030cded/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:4440107

```bash
$ singularity pull shub://bouthilx/repro-hub:4440107
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.1.0.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    REPRO_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 4440107

    cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e repro[execute,configure,deploy]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/repro-hub](https://github.com/bouthilx/repro-hub)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

