---
id: 6831
name: "bouthilx/repro-hub"
branch: "master"
tag: "64153f3"
commit: "4b1945108f5330af0fefb1d80bf2c5f72a2cdcec"
version: "c1ce1482f7dbd841eb4505672e8d605c"
build_date: "2019-02-27T17:48:21.384Z"
size_mb: 2502
size: 1527541791
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/64153f3/2019-02-27-4b194510-c1ce1482/c1ce1482f7dbd841eb4505672e8d605c.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/64153f3/2019-02-27-4b194510-c1ce1482/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/64153f3/2019-02-27-4b194510-c1ce1482/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:64153f3

```bash
$ singularity pull shub://bouthilx/repro-hub:64153f3
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
        git reset --hard 64153f3

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

