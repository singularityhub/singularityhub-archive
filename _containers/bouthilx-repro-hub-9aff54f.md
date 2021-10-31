---
id: 5962
name: "bouthilx/repro-hub"
branch: "master"
tag: "9aff54f"
commit: "cf45edb24c4b87581b6b0b4e66533ce6322ff5f5"
version: "2c060d790bc8c21371b1e200f002fdb7"
build_date: "2018-12-13T19:47:26.927Z"
size_mb: 2498
size: 1521676319
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/9aff54f/2018-12-13-cf45edb2-2c060d79/2c060d790bc8c21371b1e200f002fdb7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/9aff54f/2018-12-13-cf45edb2-2c060d79/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/9aff54f/2018-12-13-cf45edb2-2c060d79/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:9aff54f

```bash
$ singularity pull shub://bouthilx/repro-hub:9aff54f
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
        git reset --hard 9aff54f

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

