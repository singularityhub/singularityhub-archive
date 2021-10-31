---
id: 5973
name: "bouthilx/repro-hub"
branch: "master"
tag: "0eff8ea"
commit: "f2cfd8ac8e7a21c92d0694514482e0b3bb9cf4d0"
version: "6b018b025680c6c23787a3a683f793ec"
build_date: "2018-12-15T06:55:31.595Z"
size_mb: 2498
size: 1521692703
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/0eff8ea/2018-12-15-f2cfd8ac-6b018b02/6b018b025680c6c23787a3a683f793ec.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/0eff8ea/2018-12-15-f2cfd8ac-6b018b02/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/0eff8ea/2018-12-15-f2cfd8ac-6b018b02/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:0eff8ea

```bash
$ singularity pull shub://bouthilx/repro-hub:0eff8ea
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
        git reset --hard 0eff8ea

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

