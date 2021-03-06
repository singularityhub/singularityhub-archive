---
id: 6125
name: "bouthilx/repro-hub"
branch: "master"
tag: "11e925e"
commit: "3b8f131ab9c37615f582a2870afda3aa26a4fa4f"
version: "26a79a4d30997d277bc8f482e9c9d501"
build_date: "2019-01-04T21:39:44.842Z"
size_mb: 2486
size: 1508565023
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/11e925e/2019-01-04-3b8f131a-26a79a4d/26a79a4d30997d277bc8f482e9c9d501.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/11e925e/2019-01-04-3b8f131a-26a79a4d/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/11e925e/2019-01-04-3b8f131a-26a79a4d/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:11e925e

```bash
$ singularity pull shub://bouthilx/repro-hub:11e925e
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
    echo "Installing Mahler Flow Scheduler"
    echo "------------------------------------------------------"
    pip3 install git+https://github.com/bouthilx/mahler.scheduler.flow.git

    echo "------------------------------------------------------"
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 11e925e

    cd ..

    echo "------------------------------------------------------"
    echo "Installing repro"
    echo "------------------------------------------------------"
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

