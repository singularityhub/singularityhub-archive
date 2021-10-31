---
id: 5050
name: "bouthilx/sgd-space-hub"
branch: "master"
tag: "01ea4db"
commit: "ad7753857c0af1c1545902a16c2a7793fd20370f"
version: "4d647e370aaf8ecb04f8594b1b1b15c5"
build_date: "2018-10-01T08:41:33.971Z"
size_mb: 1932
size: 862253087
sif: "https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/01ea4db/2018-10-01-ad775385-4d647e37/4d647e370aaf8ecb04f8594b1b1b15c5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bouthilx/sgd-space-hub/01ea4db/2018-10-01-ad775385-4d647e37/
recipe: https://datasets.datalad.org/shub/bouthilx/sgd-space-hub/01ea4db/2018-10-01-ad775385-4d647e37/Singularity
collection: bouthilx/sgd-space-hub
---

# bouthilx/sgd-space-hub:01ea4db

```bash
$ singularity pull shub://bouthilx/sgd-space-hub:01ea4db
```

## Singularity Recipe

```singularity
BootStrap: shub
From: bouthilx/flow:pytorch.0.4.0

%labels
    AUTHOR xavier.bouthillier@umontreal.ca

% environment
    SGD_SPACE_DATA_PATH=/data

%post
    echo "------------------------------------------------------"
    echo "Fetching sgd-space"
    echo "------------------------------------------------------"
    cd /repos
    git clone https://gitlab.com/bouthilx/sgd-space.git
    cd sgd-space
        git fetch
        git checkout --track origin/dev
        git reset --hard 01ea4db

    cd ..

    echo "------------------------------------------------------"
    echo "Installing sgd-space"
    echo "------------------------------------------------------"
    pip3 install 'setuptools>=v40.1.0'
    pip3 install --process-dependency-links -e sgd-space[execute,configure,deploy]

    echo "------------------------------------------------------"
    echo "Cleaning up"
    echo "------------------------------------------------------"
    apt-get clean
    apt-get autoclean
    rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [bouthilx/sgd-space-hub](https://github.com/bouthilx/sgd-space-hub)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

