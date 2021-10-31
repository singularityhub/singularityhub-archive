---
id: 6715
name: "bouthilx/repro-hub"
branch: "master"
tag: "8a56e72"
commit: "4b1945108f5330af0fefb1d80bf2c5f72a2cdcec"
version: "027856b70ea769e4d50ac0a2a4da8c0a"
build_date: "2019-02-27T17:48:21.412Z"
size_mb: 2501
size: 1527447583
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/8a56e72/2019-02-27-4b194510-027856b7/027856b70ea769e4d50ac0a2a4da8c0a.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/8a56e72/2019-02-27-4b194510-027856b7/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/8a56e72/2019-02-27-4b194510-027856b7/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:8a56e72

```bash
$ singularity pull shub://bouthilx/repro-hub:8a56e72
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
        git reset --hard 8a56e72

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

