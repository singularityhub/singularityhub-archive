---
id: 6042
name: "bouthilx/repro-hub"
branch: "master"
tag: "546db84"
commit: "2bba8e25e6c8cc3271776c06bcd0d03e0e5ecc6b"
version: "8e83ae124f0a6dcc0188511fab891840"
build_date: "2018-12-23T09:58:23.455Z"
size_mb: 2485
size: 1508417567
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/546db84/2018-12-23-2bba8e25-8e83ae12/8e83ae124f0a6dcc0188511fab891840.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/546db84/2018-12-23-2bba8e25-8e83ae12/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/546db84/2018-12-23-2bba8e25-8e83ae12/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:546db84

```bash
$ singularity pull shub://bouthilx/repro-hub:546db84
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
    echo "Fetching repro"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/repro.git
    cd repro
        git fetch
        git checkout --track origin/dev
        git reset --hard 546db84

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

