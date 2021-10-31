---
id: 7677
name: "bouthilx/repro-hub"
branch: "master"
tag: "ac8c0ec"
commit: "adfa67c5dd92a6c7fce49a72ae05095bfda6f006"
version: "3185e2f22ef9ba67cfe58b49f1d6abd2"
build_date: "2019-03-10T08:32:53.955Z"
size_mb: 2491
size: 1515888671
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/ac8c0ec/2019-03-10-adfa67c5-3185e2f2/3185e2f22ef9ba67cfe58b49f1d6abd2.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/ac8c0ec/2019-03-10-adfa67c5-3185e2f2/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/ac8c0ec/2019-03-10-adfa67c5-3185e2f2/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:ac8c0ec

```bash
$ singularity pull shub://bouthilx/repro-hub:ac8c0ec
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
        git reset --hard ac8c0ec
 
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

