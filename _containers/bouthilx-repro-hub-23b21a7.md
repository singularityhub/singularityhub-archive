---
id: 8407
name: "bouthilx/repro-hub"
branch: "master"
tag: "23b21a7"
commit: "c0ce8648e140be83c2e131161ce8560871957cd9"
version: "fed757f2f604078bdc46abc502b0d9e9"
build_date: "2019-04-13T15:18:59.562Z"
size_mb: 2467
size: 1509302303
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/23b21a7/2019-04-13-c0ce8648-fed757f2/fed757f2f604078bdc46abc502b0d9e9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/23b21a7/2019-04-13-c0ce8648-fed757f2/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/23b21a7/2019-04-13-c0ce8648-fed757f2/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:23b21a7

```bash
$ singularity pull shub://bouthilx/repro-hub:23b21a7
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
        git reset --hard 23b21a7
 
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

