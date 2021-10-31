---
id: 5966
name: "bouthilx/repro-hub"
branch: "master"
tag: "7cfc7e9"
commit: "040f6bd4d6b204f8e5722c90a65f91ccccc87ce9"
version: "f5e41f2c93b1b419553f35648f941d78"
build_date: "2018-12-14T05:20:15.384Z"
size_mb: 2498
size: 1521676319
sif: "https://datasets.datalad.org/shub/bouthilx/repro-hub/7cfc7e9/2018-12-14-040f6bd4-f5e41f2c/f5e41f2c93b1b419553f35648f941d78.simg"
url: https://datasets.datalad.org/shub/bouthilx/repro-hub/7cfc7e9/2018-12-14-040f6bd4-f5e41f2c/
recipe: https://datasets.datalad.org/shub/bouthilx/repro-hub/7cfc7e9/2018-12-14-040f6bd4-f5e41f2c/Singularity
collection: bouthilx/repro-hub
---

# bouthilx/repro-hub:7cfc7e9

```bash
$ singularity pull shub://bouthilx/repro-hub:7cfc7e9
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
        git reset --hard 7cfc7e9

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

