---
id: 6368
name: "bouthilx/repro-hub"
branch: "master"
tag: "59f41c3"
commit: "4b1945108f5330af0fefb1d80bf2c5f72a2cdcec"
version: "abaff024f5f0507c691a506078114aea"
build_date: "2019-02-27T17:48:21.326Z"
size_mb: 2501
size: 1527386143
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/59f41c3/2019-02-27-4b194510-abaff024/abaff024f5f0507c691a506078114aea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/59f41c3/2019-02-27-4b194510-abaff024/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/59f41c3/2019-02-27-4b194510-abaff024/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:59f41c3

```bash
$ singularity pull shub://bouthilx/repro-hub:59f41c3
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
        git reset --hard 59f41c3

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

