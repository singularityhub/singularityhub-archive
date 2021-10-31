---
id: 8309
name: "bouthilx/repro-hub"
branch: "master"
tag: "a47dd9a"
commit: "f306a63322259ffbfaf140e5bf3d93caea83b242"
version: "5d047756558053f56b8f91ad9320ff65"
build_date: "2019-04-09T21:41:40.252Z"
size_mb: 2467
size: 1509294111
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/a47dd9a/2019-04-09-f306a633-5d047756/5d047756558053f56b8f91ad9320ff65.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/a47dd9a/2019-04-09-f306a633-5d047756/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/a47dd9a/2019-04-09-f306a633-5d047756/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:a47dd9a

```bash
$ singularity pull shub://bouthilx/repro-hub:a47dd9a
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
        git reset --hard a47dd9a
 
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

