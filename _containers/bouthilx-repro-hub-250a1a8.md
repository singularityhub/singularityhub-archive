---
id: 8691
name: "bouthilx/repro-hub"
branch: "master"
tag: "250a1a8"
commit: "5833c7b51ed904e9a06f17f14db362d405a411e2"
version: "7721ac15c3422cea0901cc70a8d43c3d"
build_date: "2019-04-27T21:37:46.824Z"
size_mb: 2473
size: 1511514143
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/250a1a8/2019-04-27-5833c7b5-7721ac15/7721ac15c3422cea0901cc70a8d43c3d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/250a1a8/2019-04-27-5833c7b5-7721ac15/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/250a1a8/2019-04-27-5833c7b5-7721ac15/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:250a1a8

```bash
$ singularity pull shub://bouthilx/repro-hub:250a1a8
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
        git reset --hard 250a1a8
 
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

