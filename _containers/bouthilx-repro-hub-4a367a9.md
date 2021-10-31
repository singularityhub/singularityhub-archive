---
id: 6044
name: "bouthilx/repro-hub"
branch: "master"
tag: "4a367a9"
commit: "5391b657b91af170f3a82c7ec030ab12c2a8e404"
version: "2460abfd8e6a72859e79e07c7276601c"
build_date: "2018-12-23T09:58:23.444Z"
size_mb: 2485
size: 1508438047
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/4a367a9/2018-12-23-5391b657-2460abfd/2460abfd8e6a72859e79e07c7276601c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/4a367a9/2018-12-23-5391b657-2460abfd/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/4a367a9/2018-12-23-5391b657-2460abfd/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:4a367a9

```bash
$ singularity pull shub://bouthilx/repro-hub:4a367a9
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
        git reset --hard 4a367a9

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

