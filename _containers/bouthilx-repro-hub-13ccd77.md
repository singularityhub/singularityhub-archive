---
id: 8299
name: "bouthilx/repro-hub"
branch: "master"
tag: "13ccd77"
commit: "1005fdcf4783c90116ba2e3eda9f43524138a438"
version: "bd376477c622f935fd377b4f4f619ae0"
build_date: "2019-04-09T13:50:07.004Z"
size_mb: 2467
size: 1509208095
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/13ccd77/2019-04-09-1005fdcf-bd376477/bd376477c622f935fd377b4f4f619ae0.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/13ccd77/2019-04-09-1005fdcf-bd376477/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/13ccd77/2019-04-09-1005fdcf-bd376477/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:13ccd77

```bash
$ singularity pull shub://bouthilx/repro-hub:13ccd77
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
        git reset --hard 13ccd77
 
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

