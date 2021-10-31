---
id: 8592
name: "bouthilx/repro-hub"
branch: "master"
tag: "3b3b4fa"
commit: "52f959080fa9f25b269c4c5d621fc51e7886d6c2"
version: "b25bb1ba9361bea70c6d866e2e410a21"
build_date: "2019-04-23T20:55:36.769Z"
size_mb: 2473
size: 1511477279
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/3b3b4fa/2019-04-23-52f95908-b25bb1ba/b25bb1ba9361bea70c6d866e2e410a21.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/3b3b4fa/2019-04-23-52f95908-b25bb1ba/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/3b3b4fa/2019-04-23-52f95908-b25bb1ba/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:3b3b4fa

```bash
$ singularity pull shub://bouthilx/repro-hub:3b3b4fa
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
        git reset --hard 3b3b4fa
 
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

