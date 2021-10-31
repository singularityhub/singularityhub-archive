---
id: 8388
name: "bouthilx/repro-hub"
branch: "master"
tag: "274a84b"
commit: "d181c1aba7828eb951246445cbeee5e834d536f5"
version: "e655893904479c0cab776173a150a1b5"
build_date: "2019-04-12T04:45:45.081Z"
size_mb: 2467
size: 1509302303
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/274a84b/2019-04-12-d181c1ab-e6558939/e655893904479c0cab776173a150a1b5.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/274a84b/2019-04-12-d181c1ab-e6558939/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/274a84b/2019-04-12-d181c1ab-e6558939/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:274a84b

```bash
$ singularity pull shub://bouthilx/repro-hub:274a84b
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
        git reset --hard 274a84b
 
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

