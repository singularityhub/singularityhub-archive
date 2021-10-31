---
id: 6144
name: "bouthilx/repro-hub"
branch: "master"
tag: "6ecbbce"
commit: "4d781a9bff2cc2d2a8f5c5066decea39b25bfc3a"
version: "10af47c5ec7e2dee8735165c53c0904a"
build_date: "2019-01-08T15:14:13.276Z"
size_mb: 2486
size: 1508589599
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/6ecbbce/2019-01-08-4d781a9b-10af47c5/10af47c5ec7e2dee8735165c53c0904a.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/6ecbbce/2019-01-08-4d781a9b-10af47c5/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/6ecbbce/2019-01-08-4d781a9b-10af47c5/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:6ecbbce

```bash
$ singularity pull shub://bouthilx/repro-hub:6ecbbce
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
        git reset --hard 6ecbbce

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

