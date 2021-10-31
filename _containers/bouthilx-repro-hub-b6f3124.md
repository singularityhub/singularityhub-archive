---
id: 8452
name: "bouthilx/repro-hub"
branch: "master"
tag: "b6f3124"
commit: "c860aa06acc2870d1e92dae7b4702d19fbb4b823"
version: "e032e0689a6d3c215e3a859e3b667d5b"
build_date: "2019-04-16T15:51:22.417Z"
size_mb: 2473
size: 1511350303
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/b6f3124/2019-04-16-c860aa06-e032e068/e032e0689a6d3c215e3a859e3b667d5b.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/b6f3124/2019-04-16-c860aa06-e032e068/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/b6f3124/2019-04-16-c860aa06-e032e068/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:b6f3124

```bash
$ singularity pull shub://bouthilx/repro-hub:b6f3124
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
        git reset --hard b6f3124
 
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

