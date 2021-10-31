---
id: 6214
name: "bouthilx/repro-hub"
branch: "master"
tag: "92121ef"
commit: "fc799f81b2eaf20ed52c8c3eca0ea259fd3ae322"
version: "f21a035226f7c7a973b5b6d0f8e3f493"
build_date: "2019-01-12T06:25:52.778Z"
size_mb: 2488
size: 1510342687
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/92121ef/2019-01-12-fc799f81-f21a0352/f21a035226f7c7a973b5b6d0f8e3f493.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/92121ef/2019-01-12-fc799f81-f21a0352/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/92121ef/2019-01-12-fc799f81-f21a0352/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:92121ef

```bash
$ singularity pull shub://bouthilx/repro-hub:92121ef
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
        git reset --hard 92121ef

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

