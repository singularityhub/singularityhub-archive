---
id: 8322
name: "bouthilx/repro-hub"
branch: "master"
tag: "242a1e3"
commit: "b61664838a1268011c84b851c3c4359312d89c79"
version: "25fd0a5ef9cd81577e7e9eb4d1261ffe"
build_date: "2019-04-10T11:51:49.525Z"
size_mb: 2467
size: 1509294111
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/242a1e3/2019-04-10-b6166483-25fd0a5e/25fd0a5ef9cd81577e7e9eb4d1261ffe.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/242a1e3/2019-04-10-b6166483-25fd0a5e/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/242a1e3/2019-04-10-b6166483-25fd0a5e/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:242a1e3

```bash
$ singularity pull shub://bouthilx/repro-hub:242a1e3
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
    echo "Installing Mahler"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install git+https://github.com/bouthilx/mahler.git

    echo "------------------------------------------------------"
    echo "Installing Mahler MongoDB Registry"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/mahler.registry.mongodb.git

    echo "------------------------------------------------------"
    echo "Installing forked visdom"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/visdom.git
 
    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 242a1e3
 
    cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e repro[execute,configure]

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

