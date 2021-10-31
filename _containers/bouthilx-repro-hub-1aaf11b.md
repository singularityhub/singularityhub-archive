---
id: 7680
name: "bouthilx/repro-hub"
branch: "master"
tag: "1aaf11b"
commit: "9198f109cf61e8439fca977163e8c68637e90f53"
version: "7d7babdaac5e63c875eb1087409aef49"
build_date: "2019-03-10T21:28:13.525Z"
size_mb: 2491
size: 1515892767
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/1aaf11b/2019-03-10-9198f109-7d7babda/7d7babdaac5e63c875eb1087409aef49.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/1aaf11b/2019-03-10-9198f109-7d7babda/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/1aaf11b/2019-03-10-9198f109-7d7babda/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:1aaf11b

```bash
$ singularity pull shub://bouthilx/repro-hub:1aaf11b
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
        git reset --hard 1aaf11b
 
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

