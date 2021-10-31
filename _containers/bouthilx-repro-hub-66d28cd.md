---
id: 8062
name: "bouthilx/repro-hub"
branch: "master"
tag: "66d28cd"
commit: "54f1416ed8cdb36ad22e14f7997cf6255d6ae0a4"
version: "e905656f54d9b2b17f55b903c01189ad"
build_date: "2019-04-05T20:03:04.766Z"
size_mb: 2467
size: 1509203999
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/66d28cd/2019-04-05-54f1416e-e905656f/e905656f54d9b2b17f55b903c01189ad.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/66d28cd/2019-04-05-54f1416e-e905656f/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/66d28cd/2019-04-05-54f1416e-e905656f/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:66d28cd

```bash
$ singularity pull shub://bouthilx/repro-hub:66d28cd
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
        git reset --hard 66d28cd
 
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

