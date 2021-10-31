---
id: 8636
name: "bouthilx/repro-hub"
branch: "master"
tag: "30f2b6d"
commit: "ddedd9f090edf905a772d8a894f12a644cbd4756"
version: "84d269e06c3794399dc2222fed10e231"
build_date: "2019-04-24T22:19:50.054Z"
size_mb: 2473
size: 1511477279
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/30f2b6d/2019-04-24-ddedd9f0-84d269e0/84d269e06c3794399dc2222fed10e231.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/30f2b6d/2019-04-24-ddedd9f0-84d269e0/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/30f2b6d/2019-04-24-ddedd9f0-84d269e0/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:30f2b6d

```bash
$ singularity pull shub://bouthilx/repro-hub:30f2b6d
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
        git reset --hard 30f2b6d
 
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

