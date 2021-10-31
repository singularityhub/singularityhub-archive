---
id: 5977
name: "bouthilx/repro-hub"
branch: "master"
tag: "4795953"
commit: "82b3d9b6562152a7f05059566372bb04ce7e256a"
version: "e8268f3c4e7a024c6de21bae80f415de"
build_date: "2018-12-15T06:55:31.583Z"
size_mb: 2499
size: 1521700895
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/4795953/2018-12-15-82b3d9b6-e8268f3c/e8268f3c4e7a024c6de21bae80f415de.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/4795953/2018-12-15-82b3d9b6-e8268f3c/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/4795953/2018-12-15-82b3d9b6-e8268f3c/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:4795953

```bash
$ singularity pull shub://bouthilx/repro-hub:4795953
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
        git reset --hard 4795953

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

