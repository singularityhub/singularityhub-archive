---
id: 6046
name: "bouthilx/repro-hub"
branch: "master"
tag: "7da5f4a"
commit: "9818f23e2b921ae6b0873b2960d15a39f83ed8cd"
version: "fbda15dde9941251fdd5ba601bc34bb2"
build_date: "2018-12-23T09:58:23.438Z"
size_mb: 2485
size: 1508438047
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/7da5f4a/2018-12-23-9818f23e-fbda15dd/fbda15dde9941251fdd5ba601bc34bb2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/repro-hub/7da5f4a/2018-12-23-9818f23e-fbda15dd/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/7da5f4a/2018-12-23-9818f23e-fbda15dd/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:7da5f4a

```bash
$ singularity pull shub://bouthilx/repro-hub:7da5f4a
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
        git reset --hard 7da5f4a

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

