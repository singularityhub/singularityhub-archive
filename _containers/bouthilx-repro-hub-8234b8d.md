---
id: 6127
name: "bouthilx/repro-hub"
branch: "master"
tag: "8234b8d"
commit: "0e37feba137379dd15aac78a5367af6fb4081f39"
version: "e61bd7986d9b79dec6da8f920d613cda"
build_date: "2019-01-04T21:58:16.744Z"
size_mb: 2486
size: 1508565023
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/8234b8d/2019-01-04-0e37feba-e61bd798/e61bd7986d9b79dec6da8f920d613cda.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/8234b8d/2019-01-04-0e37feba-e61bd798/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/8234b8d/2019-01-04-0e37feba-e61bd798/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:8234b8d

```bash
$ singularity pull shub://bouthilx/repro-hub:8234b8d
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
        git reset --hard 8234b8d

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

