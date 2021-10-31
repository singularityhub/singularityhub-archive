---
id: 8861
name: "bouthilx/repro-hub"
branch: "master"
tag: "88dc91b"
commit: "d67670a6d2da7b14f59a654d4d62e96848113cb8"
version: "5583c16624c90ae791c5297ea1297372"
build_date: "2019-05-06T15:37:41.443Z"
size_mb: 2458
size: 1503502367
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/88dc91b/2019-05-06-d67670a6-5583c166/5583c16624c90ae791c5297ea1297372.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/88dc91b/2019-05-06-d67670a6-5583c166/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/88dc91b/2019-05-06-d67670a6-5583c166/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:88dc91b

```bash
$ singularity pull shub://bouthilx/repro-hub:88dc91b
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
        git reset --hard 88dc91b
 
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

